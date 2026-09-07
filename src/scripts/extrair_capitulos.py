#!/usr/bin/env python3
"""Extrai os 24 capítulos da V3 (HTML) para Markdown estruturado em src/content/.

Fonte: pasta completa da V3 descompactada (passada via --v3-dir).
Saída: src/content/mNN.md, um por capítulo, com front-matter YAML e seções
nomeadas (express, corpo, painel PM, red flags, assistente LLM, quiz,
aprofundamento), preservando o conteúdo integralmente e marcando com
comentários HTML os pontos que a auditoria de conteúdo (Sessão 2, ver
governanca/AUDITORIA_CONTEUDO_DIDATICA_V4.md) já identificou como candidatos
a reescrita nos Sprints 4 a 6. Não decide nem reescreve conteúdo técnico.
"""
import argparse
import html as html_module
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


def find_tag_span(source: str, class_name: str, start_from: int = 0):
    """Acha (start, end) do bloco <tag ...class="...class_name...">...</tag>,
    contando aninhamento da mesma tag. Retorna None se não encontrar."""
    pattern = re.compile(
        r"<(\w+)([^>]*\bclass=\"[^\"]*\b" + re.escape(class_name) + r"\b[^\"]*\"[^>]*)>"
    )
    m = pattern.search(source, start_from)
    if not m:
        return None
    tag = m.group(1)
    depth = 1
    pos = m.end()
    open_re = re.compile(r"<" + tag + r"(\s[^>]*)?>")
    close_re = re.compile(r"</" + tag + r">")
    while depth > 0:
        nxt_open = open_re.search(source, pos)
        nxt_close = close_re.search(source, pos)
        if not nxt_close:
            return None
        if nxt_open and nxt_open.start() < nxt_close.start():
            depth += 1
            pos = nxt_open.end()
        else:
            depth -= 1
            pos = nxt_close.end()
    return (m.start(), pos, m.end())


def all_tag_spans(source: str, class_name: str):
    spans = []
    pos = 0
    while True:
        span = find_tag_span(source, class_name, pos)
        if not span:
            break
        spans.append(span)
        pos = span[1]
    return spans


class BodyToMarkdown(HTMLParser):
    """Converte um fragmento de HTML (o 'corpo livre' entre .express e
    .pm-panel) em Markdown, tratando especialmente diagram-pro (diagrama
    interativo original) e photo-strip/photo-study (cartão de foto)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.stack = []
        self.skip_depth = 0
        self.list_stack = []
        self.cell_buf = None
        self.table_rows = None
        self.row_buf = None
        self.diagram_mode = None
        self.diagram_data = None
        self.photo_mode = None
        self.photo_data = None
        self.photo_items = []
        self.text_buf = []

    def _flush_text(self):
        if self.text_buf:
            text = "".join(self.text_buf).strip()
            self.text_buf = []
            return text
        return ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "")

        if "diagram-pro" in classes.split():
            self.diagram_mode = "in"
            self.diagram_data = {"title": "", "rationale": "", "steps": []}
            self.stack.append(("diagram-pro", None))
            return
        if self.diagram_mode:
            if tag == "h3":
                self.stack.append(("diagram-h3", None))
            elif "animation-rationale" in classes.split():
                self.stack.append(("diagram-rationale", None))
            elif tag == "button" and attrs.get("data-step"):
                self.stack.append(("diagram-step", None))
            else:
                self.stack.append((tag, None))
            return

        if "photo-strip" in classes.split():
            self.photo_mode = "strip"
            self.photo_items = []
            self.stack.append(("photo-strip", None))
            return
        if self.photo_mode == "strip" and tag == "article" and "photo-study" in classes.split():
            self.photo_data = {"titulo": "", "observar": "", "fonte_nome": "", "fonte_url": "", "img_src": "", "img_alt": ""}
            self.stack.append(("photo-study", None))
            return
        if self.photo_data is not None:
            if tag == "img":
                self.photo_data["img_src"] = attrs.get("src", "")
                self.photo_data["img_alt"] = attrs.get("alt", "")
                self.stack.append((tag, None))
                return
            if tag in ("h3", "a", "p"):
                self.text_buf = []
            self.stack.append((tag, attrs.get("href") if tag == "a" else None))
            return

        if tag == "table":
            self.table_rows = []
            self.stack.append((tag, None))
            return
        if tag == "tr" and self.table_rows is not None:
            self.row_buf = []
            self.stack.append((tag, None))
            return
        if tag in ("td", "th") and self.row_buf is not None:
            self.cell_buf = []
            self.stack.append((tag, None))
            return

        if "callout" in classes.split() and "pm" in classes.split():
            self.out.append("\n> ")
            self.stack.append(("callout", None))
            return

        if tag == "details" and "quiz" in classes.split():
            self.stack.append(("faq-details", None))
            self._pending_faq_q = None
            return
        if tag == "summary" and self.stack and self.stack[-1][0] == "faq-details":
            self.stack.append(("faq-summary", None))
            self.text_buf = []
            return

        if tag == "p":
            self.out.append("\n")
        elif tag == "div":
            self.out.append(" ")
        elif tag == "h3":
            self.out.append("\n### ")
        elif tag == "h4":
            self.out.append("\n#### ")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("*")
        elif tag == "ul":
            self.list_stack.append("ul")
        elif tag == "ol":
            self.list_stack.append("ol")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "a":
            self.stack.append(("a", attrs.get("href", "")))
            self.out.append("[")
            return
        self.stack.append((tag, None))

    def handle_endtag(self, tag):
        if not self.stack:
            return
        top_tag, top_data = self.stack.pop() if self.stack else (tag, None)

        if top_tag == "diagram-pro":
            steps = ", ".join(self.diagram_data["steps"]) if self.diagram_data["steps"] else "(sem etapas nomeadas)"
            self.out.append(
                f"\n\n<!-- DIAGRAMA-INTERATIVO-ORIGINAL: \"{self.diagram_data['title']}\". "
                f"Por que existe: {self.diagram_data['rationale']} Etapas: {steps}. "
                f"Este diagrama era SVG+JS interativo na V3; recriar como componente de diagrama "
                f"conforme DESIGN_SYSTEM_V4.md secao 5 (frame de diagrama) nos Sprints 4-6, nao "
                f"copiar o SVG bruto. -->\n\n"
            )
            self.diagram_mode = None
            self.diagram_data = None
            return
        if top_tag == "diagram-h3":
            self.diagram_data["title"] = self._flush_text()
            return
        if top_tag == "diagram-rationale":
            self.diagram_data["rationale"] = self._flush_text()
            return
        if top_tag == "diagram-step":
            step_text = self._flush_text()
            if step_text:
                self.diagram_data["steps"].append(step_text)
            return
        if self.diagram_mode:
            self._flush_text()
            return

        if top_tag == "photo-strip":
            for item in self.photo_items:
                self.out.append(
                    f"\n\n**Cartão de foto/fonte — {item['titulo']}**\n"
                    f"O que observar: {item['observar']}\n"
                    f"Fonte oficial: [{item['fonte_nome'] or 'abrir'}]({item['fonte_url']})\n"
                    f"<!-- IMAGEM-HOTLINK-ORIGINAL: {item['img_src']} (alt: \"{item['img_alt']}\"). "
                    f"Hotlink externo, provavelmente quebrado (bloqueio de referrer/CORS) e sem "
                    f"licenca de uso confirmada. Tratar conforme D-007 no Sprint 7: copiar local "
                    f"com credito se houver licenca aberta, ou manter como cartao de fonte sem "
                    f"tag img, como esta aqui. -->\n\n"
                )
            self.photo_mode = None
            self.photo_items = []
            return
        if top_tag == "photo-study":
            self.photo_items.append(self.photo_data)
            self.photo_data = None
            return
        if self.photo_data is not None:
            text = self._flush_text()
            if top_tag == "h3":
                self.photo_data["titulo"] = text
            elif top_tag == "a":
                self.photo_data["fonte_nome"] = text or "abrir"
                self.photo_data["fonte_url"] = top_data or ""
            elif top_tag == "p" and not self.photo_data["observar"] and text:
                self.photo_data["observar"] = re.sub(r"^O que observar:\s*", "", text)
            return

        if top_tag == "table":
            lines = []
            if self.table_rows:
                header, *rest = self.table_rows
                lines.append("| " + " | ".join(header) + " |")
                lines.append("|" + "|".join(["---"] * len(header)) + "|")
                for row in rest:
                    lines.append("| " + " | ".join(row) + " |")
            self.out.append("\n\n" + "\n".join(lines) + "\n\n")
            self.table_rows = None
            return
        if top_tag == "tr":
            if self.row_buf is not None and self.table_rows is not None:
                self.table_rows.append(self.row_buf)
            self.row_buf = None
            return
        if top_tag in ("td", "th"):
            text = self._flush_text()
            if self.row_buf is not None:
                self.row_buf.append(text)
            self.cell_buf = None
            return

        if top_tag == "callout":
            self.out.append(self._flush_text() + "\n")
            return

        if top_tag in ("p", "div", "h3", "h4", "button", "details", "summary"):
            self.out.append("\n")
            return

        if top_tag == "faq-summary":
            self._pending_faq_q = self._flush_text()
            self.out.append(f"\n**Pergunta:** {self._pending_faq_q}\n")
            return
        if top_tag == "faq-details":
            return

        if top_tag == "a":
            self.out.append(f"]({top_data})")
            return
        if top_tag in ("strong", "b"):
            self.out.append("**")
            return
        if top_tag in ("em", "i"):
            self.out.append("*")
            return
        if top_tag == "ul" or top_tag == "ol":
            if self.list_stack:
                self.list_stack.pop()
            self.out.append("\n")
            return

    def handle_data(self, data):
        in_faq_summary = self.stack and self.stack[-1][0] == "faq-summary"
        if self.diagram_mode or self.photo_data is not None or self.table_rows is not None or in_faq_summary:
            self.text_buf.append(data)
            return
        self.out.append(data)

    def get_markdown(self):
        text = "".join(self.out)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n[ \t]+", "\n", text)
        return text.strip()


def html_fragment_to_markdown(fragment: str) -> str:
    parser = BodyToMarkdown()
    parser.feed(fragment)
    return parser.get_markdown()


def strip_tags_simple(fragment: str) -> str:
    """Extrai texto puro de um fragmento simples (sem estrutura rica)."""
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = html_module.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_list_items(fragment: str):
    return [strip_tags_simple(m) for m in re.findall(r"<li>(.*?)</li>", fragment, re.S)]


def extract_pm_box(chapter_html: str, box_class: str):
    span = find_tag_span(chapter_html, f"pm-box {box_class}")
    if not span:
        # a classe real e "pm-box attn" com espaco, precisa casar como substring
        span = find_tag_span(chapter_html, box_class)
    if not span:
        return []
    start, end, _ = span
    return extract_list_items(chapter_html[start:end])


def extract_quiz(chapter_html: str):
    span = find_tag_span(chapter_html, "mini-quiz")
    if not span:
        return []
    start, end, _ = span
    block = chapter_html[start:end]
    questions = []
    for qm in re.finditer(
        r'<div class="quiz-q" data-answer="(\d+)" data-feedback="([^"]*)" data-qid="([^"]*)">(.*?)</div>\s*(?=(?:<div class="quiz-q"|$))',
        block,
        re.S,
    ):
        answer_idx, feedback, qid, body = qm.groups()
        prompt_m = re.search(r"<p>(.*?)</p>", body, re.S)
        prompt = strip_tags_simple(prompt_m.group(1)) if prompt_m else ""
        options = re.findall(r'<button class="quiz-option" data-choice="(\d+)">(.*?)</button>', body, re.S)
        options = [(int(idx), strip_tags_simple(text)) for idx, text in options]
        questions.append(
            {
                "qid": qid,
                "prompt": prompt,
                "options": options,
                "answer_idx": int(answer_idx),
                "feedback": html_module.unescape(feedback),
            }
        )
    return questions


def extract_resources(chapter_html: str):
    span = find_tag_span(chapter_html, "resources")
    if not span:
        return []
    start, end, _ = span
    block = chapter_html[start:end]
    items = []
    for m in re.finditer(
        r'<a class="resource" href="([^"]*)"[^>]*>\s*<span class="rtype">([^<]*)</span>\s*<strong>([^<]*)</strong>',
        block,
        re.S,
    ):
        href, rtype, title = m.groups()
        items.append({"href": href, "tipo": rtype.strip(), "titulo": html_module.unescape(title.strip())})
    return items


def extract_express(chapter_html: str):
    span = find_tag_span(chapter_html, "express")
    if not span:
        return ""
    start, end, _ = span
    fragment = chapter_html[start:end]
    # remove o icone decorativo (express-icon, ex: "⚡") e o h3 fixo "Se você
    # precisa entender isto agora", que ja aparece como titulo da secao no
    # template — manter os dois duplicaria a mesma frase.
    icon_span = find_tag_span(fragment, "express-icon")
    if icon_span:
        fragment = fragment[: icon_span[0]] + fragment[icon_span[1] :]
    fragment = re.sub(r"<h3>.*?</h3>", "", fragment, count=1, flags=re.S)
    return html_fragment_to_markdown(fragment)


def extract_llm_helper(chapter_html: str):
    span = find_tag_span(chapter_html, "llm-helper")
    if not span:
        return ""
    start, end, _ = span
    body_span = find_tag_span(chapter_html, "llm-body", start)
    if body_span and body_span[0] < end:
        b_start, b_end, _ = body_span
        return html_fragment_to_markdown(chapter_html[b_start:b_end])
    return html_fragment_to_markdown(chapter_html[start:end])


def extract_chapter_head(chapter_html: str):
    n_m = re.search(r'<span class="chapter-no">(\d+)</span>', chapter_html)
    level_m = re.search(r'<span class="level">([^<]*)</span>', chapter_html)
    title_m = re.search(r"<h2>(.*?)</h2>", chapter_html, re.S)
    subtitle_m = re.search(r'<p class="subtitle">(.*?)</p>', chapter_html, re.S)
    return {
        "n": int(n_m.group(1)) if n_m else None,
        "level": level_m.group(1).strip() if level_m else "",
        "title": strip_tags_simple(title_m.group(1)) if title_m else "",
        "subtitle": strip_tags_simple(subtitle_m.group(1)) if subtitle_m else "",
    }


def extract_corpo(chapter_html: str):
    express_span = find_tag_span(chapter_html, "express")
    pm_span = find_tag_span(chapter_html, "pm-panel")
    if not express_span or not pm_span:
        return ""
    corpo_start = express_span[1]
    corpo_end = pm_span[0]
    fragment = chapter_html[corpo_start:corpo_end]
    return html_fragment_to_markdown(fragment)


def yaml_escape(text: str) -> str:
    return text.replace('"', '\\"')


def build_markdown(chapter_id: str, chapter_html: str) -> str:
    head = extract_chapter_head(chapter_html)
    express_md = extract_express(chapter_html)
    corpo_md = extract_corpo(chapter_html)
    attn = extract_pm_box(chapter_html, "attn")
    ask = extract_pm_box(chapter_html, "ask")
    docs = extract_pm_box(chapter_html, "docs")
    redflags_span = find_tag_span(chapter_html, "redflags")
    redflags = extract_list_items(chapter_html[redflags_span[0]:redflags_span[1]]) if redflags_span else []
    llm_md = extract_llm_helper(chapter_html)
    quiz = extract_quiz(chapter_html)
    resources = extract_resources(chapter_html)

    lines = []
    lines.append("---")
    lines.append(f'id: "{chapter_id}"')
    lines.append(f'n: {head["n"]}')
    lines.append(f'level: "{yaml_escape(head["level"])}"')
    lines.append(f'title: "{yaml_escape(head["title"])}"')
    lines.append(f'subtitle: "{yaml_escape(head["subtitle"])}"')
    lines.append("---")
    lines.append("")
    lines.append("## Express (candidato a camada \"5 minutos\")")
    lines.append("")
    lines.append(
        "<!-- REESCREVER(profundidade): ver AUDITORIA_CONTEUDO_DIDATICA_V4.md secao 3.1 e D-016. "
        "Nos Sprints 4-6 esta camada ganha conteudo proprio completo (~150 palavras), nao apenas "
        "este paragrafo introdutorio herdado da V3. -->"
    )
    lines.append("")
    lines.append(express_md)
    lines.append("")
    lines.append('## Corpo técnico (candidato a camadas "Gerente de Projetos" e "Técnica")')
    lines.append("")
    lines.append(
        "<!-- REESCREVER(profundidade): ver AUDITORIA_CONTEUDO_DIDATICA_V4.md secao 3.1 e D-016. "
        "Na V3 este bloco unico serve as duas camadas ao mesmo tempo; nos Sprints 4-6 deve virar "
        "duas secoes com conteudo proprio e profundidade completa (~300 e ~400 palavras). -->"
    )
    lines.append("")
    lines.append(corpo_md)
    lines.append("")
    lines.append("## Painel PM")
    lines.append("")
    lines.append("### Pontos de atenção")
    lines.append("")
    for item in attn:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("### Perguntas que você deve fazer")
    lines.append("")
    for item in ask:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("### Documentos que valem abrir")
    lines.append("")
    for item in docs:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Red flags")
    lines.append("")
    for item in redflags:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Assistente LLM")
    lines.append("")
    lines.append(llm_md)
    lines.append("")
    lines.append('## Mini quiz')
    lines.append("")
    lines.append(
        "<!-- REESCREVER(quiz): ver AUDITORIA_CONTEUDO_DIDATICA_V4.md secao 3.2 e D-008. Revisar "
        "distratores triviais/binarios e adicionar feedback por opcao errada (hoje so ha um "
        "feedback unico atrelado a resposta correta, data-feedback). -->"
    )
    lines.append("")
    for i, q in enumerate(quiz, start=1):
        lines.append(f"### Pergunta {i} (id: {q['qid']})")
        lines.append("")
        lines.append(f"**Enunciado:** {q['prompt']}")
        lines.append("")
        for idx, text in q["options"]:
            mark = "x" if idx == q["answer_idx"] else " "
            lines.append(f"- [{mark}] {text}")
        lines.append("")
        lines.append(f"**Feedback (resposta correta):** {q['feedback']}")
        lines.append("")
    lines.append('## Aprofundamento (candidato a camada "Deep dive")')
    lines.append("")
    for r in resources:
        lines.append(f"- [{r['tipo']}] [{r['titulo']}]({r['href']})")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v3-dir", required=True, help="Pasta raiz da V3 completa (Portal_Subsea_Rafaela_V3_COMPLETO)")
    ap.add_argument("--out-dir", default="src/content", help="Pasta de saída dos .md")
    args = ap.parse_args()

    v3_dir = Path(args.v3_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    capitulos_dir = v3_dir / "capitulos"
    chapter_files = sorted(capitulos_dir.glob("m*.html"))
    if len(chapter_files) != 24:
        print(f"AVISO: esperado 24 capitulos, encontrado {len(chapter_files)}", file=sys.stderr)

    report = []
    for cf in chapter_files:
        chapter_id = cf.stem
        chapter_html = cf.read_text(encoding="utf-8")
        try:
            md = build_markdown(chapter_id, chapter_html)
        except Exception as e:
            print(f"ERRO em {chapter_id}: {e}", file=sys.stderr)
            raise
        out_path = out_dir / f"{chapter_id}.md"
        out_path.write_text(md + "\n", encoding="utf-8")
        report.append({"id": chapter_id, "chars_out": len(md), "quiz_questions": md.count("**Enunciado:**")})
        print(f"OK {chapter_id} -> {out_path} ({len(md)} chars)")

    print(json.dumps({"total": len(report), "capitulos": report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
