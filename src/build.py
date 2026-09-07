#!/usr/bin/env python3
"""Gera o site estático da Plataforma Subsea Rafaela a partir de src/content e src/data.

Uso: python3 src/build.py
Lê:  src/content/*.md, src/data/*.json, src/templates/*.html
Gera: index.html, ementa.html, treinamento.html, glossario.html, prompts.html,
      biblioteca.html, progresso.html, referencias.html, search.html,
      capitulos/*.html — todos na raiz do repositório (site publicado).

Regra do CLAUDE.md 0.4 item 3: nunca editar o HTML gerado à mão. Editar aqui,
em src/content, src/data ou src/templates, e rodar este script de novo.
"""
import json
import re
import sys
from pathlib import Path

import markdown as md_lib
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "src" / "content"
DATA_DIR = ROOT / "src" / "data"
TEMPLATES_DIR = ROOT / "src" / "templates"
OUT_DIR = ROOT
CAPITULOS_OUT = OUT_DIR / "capitulos"

REESCREVER_COMMENT_RE = re.compile(
    r"<!--\s*(REESCREVER|DIAGRAMA-INTERATIVO-ORIGINAL|IMAGEM-HOTLINK-ORIGINAL).*?-->",
    re.S,
)


def load_json(name):
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


def strip_dev_comments(text: str) -> str:
    return REESCREVER_COMMENT_RE.sub("", text)


def md_to_html(text: str) -> str:
    text = strip_dev_comments(text).strip()
    if not text:
        return ""
    return md_lib.markdown(text, extensions=["tables"])


def parse_chapter_md(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: front-matter YAML nao encontrado")
    front = yaml.safe_load(m.group(1))
    body = m.group(2)

    sections = {}
    for part in re.split(r"\n## ", "\n" + body)[1:]:
        heading, _, rest = part.partition("\n")
        sections[heading.strip()] = rest.strip()

    return front, sections


def parse_pm_panel(pm_section_text: str):
    sub = {}
    for part in re.split(r"\n### ", "\n" + pm_section_text)[1:]:
        heading, _, rest = part.partition("\n")
        sub[heading.strip()] = rest.strip()
    return (
        md_to_html(sub.get("Pontos de atenção", "")),
        md_to_html(sub.get("Perguntas que você deve fazer", "")),
        md_to_html(sub.get("Documentos que valem abrir", "")),
    )


def parse_quiz(quiz_section_text: str):
    clean = strip_dev_comments(quiz_section_text)
    questions = []
    blocks = re.split(r"\n### Pergunta \d+ \(id: ([^)]+)\)\n", "\n" + clean)
    # blocks[0] is preamble (empty after stripping comment); then pairs of (qid, body)
    it = iter(blocks[1:])
    for qid, body in zip(it, it):
        prompt_m = re.search(r"\*\*Enunciado:\*\*\s*(.+)", body)
        prompt = prompt_m.group(1).strip() if prompt_m else ""
        options = []
        answer_idx = None
        for i, line in enumerate(re.findall(r"^- \[( |x)\] (.+)$", body, re.M)):
            mark, text = line
            if mark == "x":
                answer_idx = i
            options.append((i, text.strip()))
        feedback_m = re.search(r"\*\*Feedback \(resposta correta\):\*\*\s*(.+)", body)
        feedback = feedback_m.group(1).strip() if feedback_m else ""
        questions.append(
            {"qid": qid, "prompt": prompt, "options": options, "answer_idx": answer_idx, "feedback": feedback}
        )
    return questions


def build_term_regex(glossario):
    terms = sorted({g["term"] for g in glossario if g.get("term")}, key=len, reverse=True)
    escaped = [re.escape(t) for t in terms]
    pattern = r"\b(" + "|".join(escaped) + r")\b"
    return re.compile(pattern, re.IGNORECASE), {g["term"].lower(): g for g in glossario}


TAG_OR_TEXT_RE = re.compile(r"(<[^>]+>)|([^<]+)")


def marcar_termos_no_html(html_fragment: str, term_re, term_map) -> str:
    if not html_fragment:
        return html_fragment

    def replace_in_text(text_piece):
        def sub_term(m):
            matched = m.group(0)
            data = term_map.get(matched.lower())
            if not data:
                return matched
            return f'<span class="term" data-term="{data["term"]}" tabindex="0" role="button">{matched}</span>'

        return term_re.sub(sub_term, text_piece)

    out = []
    for tag, text in TAG_OR_TEXT_RE.findall(html_fragment):
        if tag:
            out.append(tag)
        else:
            out.append(replace_in_text(text))
    return "".join(out)


def main():
    glossario = load_json("glossario.json")
    prompts = load_json("prompts.json")
    aliases = load_json("aliases.json")

    term_re, term_map = build_term_regex(glossario)
    glossario_json_inline = json.dumps(glossario, ensure_ascii=False)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)

    chapter_files = sorted(CONTENT_DIR.glob("m*.md"))
    chapters_meta = []
    parsed_chapters = []
    for cf in chapter_files:
        front, sections = parse_chapter_md(cf)
        chapters_meta.append({"id": front["id"], "n": front["n"], "title": front["title"], "subtitle": front["subtitle"]})
        parsed_chapters.append((front, sections))

    chapters_meta.sort(key=lambda c: c["n"])
    total_chapters = len(chapters_meta)

    CAPITULOS_OUT.mkdir(parents=True, exist_ok=True)
    capitulo_tpl = env.get_template("capitulo.html")

    for i, (front, sections) in enumerate(sorted(parsed_chapters, key=lambda p: p[0]["n"])):
        chapter_id = front["id"]
        express_html = marcar_termos_no_html(
            md_to_html(sections.get('Express (candidato a camada "5 minutos")', "")), term_re, term_map
        )
        corpo_html = marcar_termos_no_html(
            md_to_html(sections.get('Corpo técnico (candidato a camadas "Gerente de Projetos" e "Técnica")', "")),
            term_re,
            term_map,
        )
        pm_attn_html, pm_ask_html, pm_docs_html = parse_pm_panel(sections.get("Painel PM", ""))
        pm_attn_html = marcar_termos_no_html(pm_attn_html, term_re, term_map)
        pm_ask_html = marcar_termos_no_html(pm_ask_html, term_re, term_map)
        pm_docs_html = marcar_termos_no_html(pm_docs_html, term_re, term_map)
        redflags_html = marcar_termos_no_html(md_to_html(sections.get("Red flags", "")), term_re, term_map)
        llm_html = marcar_termos_no_html(md_to_html(sections.get("Assistente LLM", "")), term_re, term_map)
        quiz_questions = parse_quiz(sections.get("Mini quiz", ""))
        aprofundamento_html = md_to_html(sections.get('Aprofundamento (candidato a camada "Deep dive")', ""))

        prev_chapter = chapters_meta[i - 1] if i > 0 else None
        next_chapter = chapters_meta[i + 1] if i < total_chapters - 1 else None

        html_out = capitulo_tpl.render(
            page_title=front["title"],
            asset_prefix="../",
            chapter_id=chapter_id,
            glossario_json=glossario_json_inline,
            n=front["n"],
            level=front.get("level", ""),
            title=front["title"],
            subtitle=front["subtitle"],
            express_html=express_html,
            corpo_html=corpo_html,
            pm_attn_html=pm_attn_html,
            pm_ask_html=pm_ask_html,
            pm_docs_html=pm_docs_html,
            redflags_html=redflags_html,
            llm_html=llm_html,
            quiz_questions=quiz_questions,
            aprofundamento_html=aprofundamento_html,
            prev_chapter=prev_chapter,
            next_chapter=next_chapter,
            total_chapters=total_chapters,
        )
        (CAPITULOS_OUT / f"{chapter_id}.html").write_text(html_out, encoding="utf-8")
        print(f"OK capitulos/{chapter_id}.html")

    # Home
    home_tpl = env.get_template("home.html")
    (OUT_DIR / "index.html").write_text(
        home_tpl.render(
            page_title="Home",
            asset_prefix="",
            chapter_id=None,
            glossario_json=glossario_json_inline,
            chapters=chapters_meta,
        ),
        encoding="utf-8",
    )
    print("OK index.html")

    # Ementa
    lista_tpl = env.get_template("hub_lista_capitulos.html")
    (OUT_DIR / "ementa.html").write_text(
        lista_tpl.render(
            page_title="Ementa",
            asset_prefix="",
            chapter_id=None,
            glossario_json=glossario_json_inline,
            chapters=chapters_meta,
            intro="Os 24 capítulos do curso, em ordem.",
        ),
        encoding="utf-8",
    )
    print("OK ementa.html")

    # Glossario
    glossario_tpl = env.get_template("glossario.html")
    glossario_ordenado = sorted(glossario, key=lambda g: g["term"].lower())
    (OUT_DIR / "glossario.html").write_text(
        glossario_tpl.render(
            page_title="Glossário",
            asset_prefix="",
            chapter_id=None,
            glossario_json=glossario_json_inline,
            glossario=glossario_ordenado,
        ),
        encoding="utf-8",
    )
    print("OK glossario.html")

    # Prompts
    prompts_tpl = env.get_template("prompts.html")
    (OUT_DIR / "prompts.html").write_text(
        prompts_tpl.render(
            page_title="Prompts",
            asset_prefix="",
            chapter_id=None,
            glossario_json=glossario_json_inline,
            prompts=prompts,
        ),
        encoding="utf-8",
    )
    print("OK prompts.html")

    # Placeholders (conteudo completo e Sprint 3/7/8)
    placeholder_tpl = env.get_template("hub_placeholder.html")
    placeholders = [
        ("treinamento.html", "Treinamento", "Sprint 3"),
        ("biblioteca.html", "Biblioteca Visual", "Sprint 7 (licenciamento de imagens)"),
        ("progresso.html", "Progresso", "Sprint 8 (gamificação)"),
        ("referencias.html", "Referências", "Sprint 3"),
        ("search.html", "Buscar", "Sprint 3 (índice de busca com aliases)"),
    ]
    for filename, title, destino in placeholders:
        (OUT_DIR / filename).write_text(
            placeholder_tpl.render(
                page_title=title,
                asset_prefix="",
                chapter_id=None,
                glossario_json=glossario_json_inline,
                sprint_destino=destino,
            ),
            encoding="utf-8",
        )
        print(f"OK {filename}")

    print(f"\nBuild concluido: {total_chapters} capitulos + 9 hubs.")


if __name__ == "__main__":
    sys.exit(main())
