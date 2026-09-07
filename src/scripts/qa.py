#!/usr/bin/env python3
"""QA automatizado do site gerado (Sprint 1 do ROADMAP_V4.md).

Verifica: links locais quebrados, IDs duplicados dentro de cada página,
blocos obrigatórios por capítulo, <img> apontando para domínio externo,
HTML parseável, e uma checagem heurística de cobertura de glossário
(siglas maiúsculas no texto que não têm entrada no glossário — D-019).

Overflow em 360px/1440px NÃO é testado aqui: exige navegador real ou
headless browser, que não faz parte deste script. Ver D-009 — teste em
dispositivo real continua sendo responsabilidade do Paulo antes do release.

Uso: python3 src/scripts/qa.py
Saída: 0 se tudo passou, 1 se algum erro foi encontrado (útil para CI).
"""
import html.parser
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT / "src" / "data"

REQUIRED_BLOCKS = [
    ("chapter-head", 'class="chapter-head"'),
    ("layer-control", 'class="layer-control"'),
    ("express (data-layer=5min)", 'data-layer="5min"'),
    ("pm-panel", 'class="pm-panel"'),
    ("pm-attn", 'data-pm-box="attn"'),
    ("pm-ask", 'data-pm-box="ask"'),
    ("pm-docs", 'data-pm-box="docs"'),
    ("redflags", 'class="chapter-section redflags"'),
    ("llm-helper", 'class="chapter-section llm-helper"'),
    ("mini-quiz", 'class="chapter-section mini-quiz"'),
    ("deep-dive", 'class="chapter-section deep-dive"'),
]


class SanityHTMLParser(html.parser.HTMLParser):
    def error(self, message):
        raise ValueError(message)


def check_html_parseable(path: Path, errors: list):
    text = path.read_text(encoding="utf-8")
    try:
        SanityHTMLParser().feed(text)
    except Exception as e:
        errors.append(f"{path.relative_to(ROOT)}: HTML nao parseavel: {e}")
    return text


def check_duplicate_ids(path: Path, text: str, errors: list):
    ids = re.findall(r'\bid="([^"]+)"', text)
    counts = Counter(ids)
    dupes = [i for i, c in counts.items() if c > 1]
    if dupes:
        errors.append(f"{path.relative_to(ROOT)}: IDs duplicados dentro da mesma pagina: {dupes}")


def check_external_images(path: Path, text: str, errors: list):
    imgs = re.findall(r'<img[^>]*\bsrc="([^"]+)"', text)
    external = [src for src in imgs if src.startswith("http://") or src.startswith("https://")]
    if external:
        errors.append(f"{path.relative_to(ROOT)}: <img> externo encontrado (viola D-007): {external}")


def check_required_blocks(path: Path, text: str, errors: list):
    if "capitulos" not in str(path.parent.name):
        return
    for name, marker in REQUIRED_BLOCKS:
        if marker not in text:
            errors.append(f"{path.relative_to(ROOT)}: bloco obrigatorio ausente: {name}")
    n_quiz = text.count('class="quiz-question"')
    if n_quiz == 0:
        errors.append(f"{path.relative_to(ROOT)}: nenhuma pergunta de quiz encontrada")


def check_local_links(all_files: dict, errors: list):
    for path, text in all_files.items():
        hrefs = re.findall(r'href="([^"]+)"', text)
        for href in hrefs:
            if href.startswith(("http://", "https://", "#", "mailto:", "javascript:", "data:")):
                continue
            target_path = href.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: link local quebrado -> {href}")


ACRONYM_RE = re.compile(r"\b[A-Z]{2,6}(?:/[A-Z]{2,6})?\b")
COMMON_NON_TERMS = {
    "PM", "LLM", "TQ", "RFI", "TBD", "TBC", "V4", "V3", "CSS", "JS", "HTML", "URL", "ID",
    "OK", "XP",
    # palavras comuns em portugues que calham de aparecer maiusculas (titulos,
    # placeholders como "MINHA DUVIDA:"), nao sao siglas tecnicas:
    "AQUI", "MINHA", "UMA", "PENSAR", "TUBO", "ET",
}


def check_glossario_coverage(errors_or_warnings: list):
    glossario = json.loads((DATA_DIR / "glossario.json").read_text(encoding="utf-8"))
    known_terms_upper = {g["term"].upper() for g in glossario}
    content_dir = ROOT / "src" / "content"
    gaps = {}
    for md_file in sorted(content_dir.glob("m*.md")):
        text = md_file.read_text(encoding="utf-8")
        text_no_comments = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        candidates = set(ACRONYM_RE.findall(text_no_comments))
        missing = sorted(
            c for c in candidates
            if c not in known_terms_upper and c not in COMMON_NON_TERMS and len(c) >= 2
        )
        if missing:
            gaps[md_file.stem] = missing
    return gaps


def main():
    errors = []
    all_files = {}

    html_files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "capitulos").glob("*.html"))
    for path in html_files:
        text = check_html_parseable(path, errors)
        all_files[path] = text
        check_duplicate_ids(path, text, errors)
        check_external_images(path, text, errors)
        check_required_blocks(path, text, errors)

    check_local_links(all_files, errors)

    gaps = check_glossario_coverage(errors)

    print(f"Paginas verificadas: {len(html_files)}")
    print(f"Erros encontrados: {len(errors)}")
    for e in errors:
        print(f"  ERRO: {e}")

    print(f"\nCobertura de glossario (heuristica, D-019): {len(gaps)} capitulo(s) com siglas candidatas sem entrada")
    total_gap_terms = 0
    for cid, terms in gaps.items():
        total_gap_terms += len(terms)
        print(f"  {cid}: {terms}")
    print(f"Total de siglas candidatas sem entrada no glossario: {total_gap_terms}")
    print(
        "(Isso e uma checagem heuristica, nao bloqueante: cataloga candidatos para o "
        "trabalho de B-031/D-019 nos Sprints 4-6, nao reprova o build.)"
    )

    if errors:
        print(f"\nQA FALHOU: {len(errors)} erro(s) bloqueante(s).")
        return 1
    print("\nQA OK: zero erros bloqueantes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
