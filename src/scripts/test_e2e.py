#!/usr/bin/env python3
"""Teste E2E do site gerado, num navegador real (Chromium via Playwright).

Complementa src/scripts/qa.py (que só olha o HTML como texto): aqui a página
roda de verdade, com JavaScript, em dois viewports (desktop e mobile), e o
teste verifica que a interatividade funciona — controle de camadas, quiz,
popover de termo, progresso persistente, filtro do glossário — e que não há
erro de JS nem overflow horizontal.

IMPORTANTE: isso NÃO substitui o teste em dispositivo real do Paulo antes de
qualquer release (D-009 em governanca/DECISOES.md). É uma rede de segurança
automatizada antes de pedir esse teste humano, não um substituto dele.

Depende de `playwright` (pacote Python) e de um Chromium instalado. Em
sessões futuras do Claude Code, o ambiente já traz um Chromium pré-instalado
em /opt/pw-browsers — ajuste CHROMIUM_PATH abaixo se o caminho mudar. Rode
`pip install playwright` se o pacote Python não estiver disponível (não é
preciso rodar `playwright install`, o browser já existe).

Uso: primeiro rode `python3 src/build.py`, depois `python3 src/scripts/test_e2e.py`.
Saída: 0 se tudo passou, 1 se alguma checagem falhou.
"""
import http.server
import socketserver
import sys
import threading
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Pacote 'playwright' nao instalado. Rode: pip install playwright")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
PORT = 8850
CHROMIUM_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
]


def find_chromium():
    for path in CHROMIUM_CANDIDATES:
        if Path(path).exists():
            return path
    return None  # deixa o Playwright usar o padrao dele, se houver


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, *args):
        pass


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


results = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    results.append((status, name, detail))
    print(f"[{status}] {name} {detail}")


def run_checks_for_viewport(browser, viewport_name, viewport, chapter_id="m17"):
    page = browser.new_page(viewport=viewport)
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: console_errors.append(str(exc)))

    page.goto(f"http://localhost:{PORT}/capitulos/{chapter_id}.html")
    page.wait_for_load_state("networkidle")

    check(f"[{viewport_name}] {chapter_id} carrega sem erro JS", len(console_errors) == 0, str(console_errors))

    overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 2")
    check(f"[{viewport_name}] sem overflow horizontal", not overflow)

    page.click('[data-layer-btn="5min"]')
    visible_5min = page.is_visible('.chapter-section[data-layer="5min"]')
    hidden_deepdive = not page.is_visible('.chapter-section[data-layer="deepdive"]')
    check(f"[{viewport_name}] filtro de camada 5min funciona", visible_5min and hidden_deepdive)

    page.click('[data-layer-btn="all"]')
    check(f"[{viewport_name}] Ver tudo restaura visibilidade", page.is_visible('.chapter-section[data-layer="deepdive"]'))

    first_q = page.locator(".quiz-question").first
    answer_idx = first_q.get_attribute("data-answer")
    first_q.locator(f'.quiz-option[data-choice="{answer_idx}"]').click()
    feedback_text = first_q.locator(".quiz-feedback").inner_text()
    check(f"[{viewport_name}] quiz mostra feedback ao acertar", len(feedback_text) > 0, feedback_text[:80])

    term = page.locator(".term").first
    term.click()
    popover_visible = page.locator("#term-popover").is_visible()
    popover_text = page.locator("#term-popover .term-title").inner_text() if popover_visible else ""
    check(f"[{viewport_name}] popover de termo abre com conteudo", popover_visible and len(popover_text) > 0, popover_text)

    page.click(".mark-done")
    done_text = page.locator(".mark-done").inner_text()
    check(f"[{viewport_name}] marcar como estudado muda o texto do botao", "Estudado" in done_text, done_text)

    page.reload()
    page.wait_for_load_state("networkidle")
    done_after = page.locator(".mark-done").inner_text()
    check(f"[{viewport_name}] progresso persiste apos reload", "Estudado" in done_after, done_after)

    page.goto(f"http://localhost:{PORT}/index.html")
    page.wait_for_load_state("networkidle")
    card_class = page.locator(f'.chapter-card[data-chapter-link="{chapter_id}"]').get_attribute("class")
    check(f"[{viewport_name}] card do capitulo concluido marcado na Home", "done" in (card_class or ""), card_class)

    page.goto(f"http://localhost:{PORT}/glossario.html")
    page.wait_for_load_state("networkidle")
    total_before = page.locator(".glossario-item:visible").count()
    page.fill("#glossario-filter", "ROV")
    time.sleep(0.2)
    total_after = page.locator(".glossario-item:visible").count()
    check(f"[{viewport_name}] filtro do glossario reduz resultados", 0 < total_after < total_before, f"{total_before} -> {total_after}")

    page.close()


def main():
    httpd = ReusableTCPServer(("", PORT), Handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    time.sleep(0.3)

    chromium_path = find_chromium()
    with sync_playwright() as p:
        launch_kwargs = {"executable_path": chromium_path} if chromium_path else {}
        browser = p.chromium.launch(**launch_kwargs)
        for viewport_name, viewport in [("desktop", {"width": 1440, "height": 900}), ("mobile", {"width": 390, "height": 844})]:
            run_checks_for_viewport(browser, viewport_name, viewport)
        browser.close()

    httpd.shutdown()

    n_fail = sum(1 for s, _, _ in results if s == "FAIL")
    print(f"\n{'=' * 40}\nTOTAL: {len(results)} checagens, {n_fail} falhas")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
