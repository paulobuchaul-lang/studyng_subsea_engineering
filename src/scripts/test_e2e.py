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
import tempfile
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
    # a Home mostra a Trilha como mapa compacto (trail-point), nao cartoes completos
    card_class = page.locator(f'.trail-point[data-chapter-link="{chapter_id}"]').get_attribute("class")
    check(f"[{viewport_name}] ponto do capitulo concluido marcado na Home", "done" in (card_class or ""), card_class)

    if viewport_name == "mobile":
        home_height = page.evaluate("document.documentElement.scrollHeight")
        two_screens = viewport["height"] * 2
        check(
            f"[{viewport_name}] Home cabe em ~2 telas (checklist DESIGN_SYSTEM_V4 secao 9)",
            home_height <= two_screens * 1.15,  # 15% de folga
            f"{home_height}px vs {two_screens}px (2x{viewport['height']})",
        )

    page.goto(f"http://localhost:{PORT}/glossario.html")
    page.wait_for_load_state("networkidle")
    total_before = page.locator(".glossario-item:visible").count()
    page.fill("#glossario-filter", "ROV")
    time.sleep(0.2)
    total_after = page.locator(".glossario-item:visible").count()
    check(f"[{viewport_name}] filtro do glossario reduz resultados", 0 < total_after < total_before, f"{total_before} -> {total_after}")

    # --- Sprint 2: design system ---
    page.goto(f"http://localhost:{PORT}/capitulos/{chapter_id}.html")
    page.wait_for_load_state("networkidle")

    icon_svgs = page.locator("[data-icon] svg").count()
    check(f"[{viewport_name}] icones SVG renderizados", icon_svgs > 5, f"{icon_svgs} icones com svg")

    if viewport_name == "desktop":
        check(f"[{viewport_name}] sidebar desktop visivel", page.is_visible(".sidebar-desktop"))
        check(f"[{viewport_name}] tab bar mobile oculta", not page.is_visible(".tabbar-mobile"))
    else:
        check(f"[{viewport_name}] tab bar mobile visivel", page.is_visible(".tabbar-mobile"))
        check(f"[{viewport_name}] sidebar desktop oculta", not page.is_visible(".sidebar-desktop"))

    # abas do painel PM
    page.click('[data-pm-tab="ask"]')
    ask_visible = page.is_visible('[data-pm-box="ask"]')
    attn_hidden = not page.is_visible('[data-pm-box="attn"]')
    check(f"[{viewport_name}] abas do painel PM alternam conteudo", ask_visible and attn_hidden)

    # mobile: "Neste capitulo" em bottom sheet, ir direto ao Painel PM em 2 toques
    if viewport_name == "mobile":
        page.click("#chapterSheetOpen")  # toque 1
        sheet_visible = page.is_visible("#chapterSheet")
        check(f"[{viewport_name}] bottom sheet 'Neste capitulo' abre", sheet_visible)
        page.click('#chapterSheetSections a:has-text("Painel PM")')  # toque 2
        pm_visible = page.is_visible('.chapter-section[data-section-title="Painel PM"]')
        sheet_closed = not page.is_visible("#chapterSheet")
        check(f"[{viewport_name}] 2 toques leva ao Painel PM e fecha o sheet", pm_visible and sheet_closed)

    # tema escuro (botao diferente por viewport: sidebar no desktop, topbar no mobile)
    toggle_id = "#themeToggle" if viewport_name == "desktop" else "#themeToggleMobile"
    theme_toggle = page.locator(toggle_id)
    if theme_toggle.count() > 0:
        theme_toggle.click()
        theme_attr = page.evaluate("document.documentElement.getAttribute('data-theme')")
        check(f"[{viewport_name}] alternancia de tema aplica data-theme", theme_attr == "dark", theme_attr)
        bg_color = page.evaluate("getComputedStyle(document.body).backgroundColor")
        check(f"[{viewport_name}] fundo muda no tema escuro", "18, 27, 43" in bg_color or "11, 27, 43" in bg_color, bg_color)

    # --- Sprint 3: hubs reais (busca, referencias, biblioteca, progresso) ---
    page.goto(f"http://localhost:{PORT}/search.html")
    page.wait_for_load_state("networkidle")
    page.fill("#search-input", "pull in")
    direct_visible = page.is_visible("#search-direct")
    direct_href = page.locator("#search-direct-link").get_attribute("href") if direct_visible else ""
    check(
        f"[{viewport_name}] busca 'pull in' encontra resultado direto para o capitulo 17 (criterio de aceite do Sprint 3)",
        direct_visible and "m17.html" in (direct_href or ""),
        direct_href,
    )
    page.click("#search-input")
    page.press("#search-input", "Enter")
    page.wait_for_load_state("networkidle")
    check(f"[{viewport_name}] Enter na busca abre o capitulo 17", "m17.html" in page.url, page.url)

    page.goto(f"http://localhost:{PORT}/referencias.html")
    page.wait_for_load_state("networkidle")
    ref_items = page.locator(".ref-item").count()
    check(f"[{viewport_name}] Referencias lista itens extraidos dos capitulos", ref_items > 20, f"{ref_items} itens")

    page.goto(f"http://localhost:{PORT}/biblioteca.html")
    page.wait_for_load_state("networkidle")
    biblioteca_empty_visible = page.is_visible(".biblioteca-empty")
    check(f"[{viewport_name}] Biblioteca Visual mostra estado vazio claro (dados chegam no Sprint 7)", biblioteca_empty_visible)

    page.goto(f"http://localhost:{PORT}/progresso.html")
    page.wait_for_load_state("networkidle")
    resumo_text = page.locator("#progresso-resumo").inner_text()
    check(f"[{viewport_name}] Progresso mostra resumo com contagem", "24" in resumo_text, resumo_text)

    if viewport_name == "desktop":
        # export/import: exporta, limpa localStorage, importa de volta, confere que o progresso retorna
        with page.expect_download() as download_info:
            page.click("#export-progress-btn")
        download = download_info.value
        export_path = str(Path(tempfile.gettempdir()) / "subsea_progress_export_test.json")
        download.save_as(export_path)

        page.evaluate("localStorage.clear()")
        page.reload()
        page.wait_for_load_state("networkidle")
        resumo_zerado = page.locator("#progresso-resumo").inner_text()

        page.set_input_files("#import-progress-input", export_path)
        page.wait_for_timeout(500)  # leitura do arquivo (FileReader) e reload() sao assincronos
        page.wait_for_load_state("networkidle")
        resumo_restaurado = page.locator("#progresso-resumo").inner_text()
        check(
            f"[{viewport_name}] exportar/importar progresso restaura o estado (B-011)",
            "0 de 24" in resumo_zerado and resumo_restaurado == resumo_text,
            f"zerado='{resumo_zerado}' restaurado='{resumo_restaurado}' original='{resumo_text}'",
        )
        try:
            Path(export_path).unlink()
        except OSError:
            pass

    page.goto(f"http://localhost:{PORT}/treinamento.html")
    page.wait_for_load_state("networkidle")
    check(f"[{viewport_name}] Treinamento carrega sem erro JS", len(console_errors) == 0, str(console_errors))

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
