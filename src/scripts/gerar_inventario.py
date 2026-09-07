#!/usr/bin/env python3
"""
Gera um inventario tecnico da Plataforma Subsea Rafaela V3.

Varre os hubs e os 24 capitulos da V3 (HTML estatico) e produz um relatorio
estruturado em JSON com titulos, IDs, links, imagens, blocos textuais
caracteristicos e contagem de palavras de cada pagina, alem de um resumo
com IDs duplicados entre arquivos, total de imagens externas e capitulos
que estao sem algum dos blocos esperados.

Uso:
    python3 gerar_inventario.py

O caminho da pasta fonte da V3 e da saida podem ser ajustados nas
constantes V3_ROOT e SAIDA_JSON abaixo.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------

V3_ROOT = Path(
    "/tmp/claude-0/-home-user-studyng-subsea-engineering/"
    "de3352c6-6a11-5a28-bfa3-0339fdf515bf/scratchpad/v3full/"
    "Portal_Subsea_Rafaela_V3_COMPLETO"
)

SAIDA_JSON = Path("/home/user/studyng_subsea_engineering/INVENTARIO_V3.json")

# Nomes-padrao dos arquivos "hub" (tudo que nao esta em capitulos/).
# Se algum desses arquivos nao existir na pasta fonte, ele e simplesmente
# ignorado e o motivo e reportado no console (nao aborta a execucao).
HUBS_ESPERADOS = [
    "index.html",
    "ementa.html",
    "treinamento.html",
    "glossario.html",
    "prompts.html",
    "biblioteca.html",
    "progresso.html",
    "referencias.html",
    "search.html",
]

NUM_CAPITULOS = 24

# Marcadores textuais caracteristicos de blocos dos capitulos.
# A chave e o nome do bloco (usado no relatorio), o valor e a substring
# a procurar (case-insensitive) no texto visivel da pagina.
MARCADORES_BLOCOS = {
    "bloco_express": "se você precisa entender isto agora",
    "painel_pontos_de_atencao": "pontos de atenção",
    "painel_perguntas_que_voce_deve_fazer": "perguntas que você deve fazer",
    "painel_documentos_que_valem_abrir": "documentos que valem abrir",
    "painel_red_flags": "red flags",
    "assistente_llm": "aprofunde este tema com uma llm",
    "mini_quiz": "mini quiz",
}

TAGS_IGNORAR_TEXTO = {"script", "style"}


# ---------------------------------------------------------------------------
# Parser HTML
# ---------------------------------------------------------------------------


class InventarioParser(HTMLParser):
    """Extrai titulo, ids, links, imagens e texto visivel de uma pagina."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.titulo_partes: list[str] = []
        self.em_title = False

        self.ids: list[str] = []
        self.links_locais: list[str] = []
        self.links_externos: list[str] = []
        self.imagens: list[dict] = []

        self.texto_partes: list[str] = []
        self._pilha_ignorar_texto: list[str] = []

    # -- helpers ------------------------------------------------------

    @staticmethod
    def _classificar_href(href: str) -> str:
        """Retorna 'externo', 'local' ou 'ignorar' para um valor de href."""
        href_strip = href.strip()
        if href_strip == "#":
            return "ignorar"
        lower = href_strip.lower()
        if lower.startswith("http://") or lower.startswith("https://"):
            return "externo"
        if lower.startswith("mailto:"):
            return "ignorar"
        return "local"

    # -- HTMLParser hooks -----------------------------------------------

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs_dict = dict(attrs)

        if tag.lower() == "title":
            self.em_title = True

        if tag.lower() in TAGS_IGNORAR_TEXTO:
            self._pilha_ignorar_texto.append(tag.lower())

        if "id" in attrs_dict and attrs_dict["id"]:
            self.ids.append(attrs_dict["id"])

        if tag.lower() == "a" and attrs_dict.get("href"):
            href = attrs_dict["href"]
            classe = self._classificar_href(href)
            if classe == "externo":
                self.links_externos.append(href)
            elif classe == "local":
                self.links_locais.append(href)
            # 'ignorar' -> nao entra em nenhuma lista

        if tag.lower() == "img":
            src = attrs_dict.get("src", "")
            is_externa = src.lower().startswith("http://") or src.lower().startswith(
                "https://"
            )
            self.imagens.append({"src": src, "is_externa": is_externa})

    def handle_startendtag(self, tag: str, attrs) -> None:
        # Cobre tags auto-fechadas, ex: <img ... />
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.em_title = False
        if tag.lower() in TAGS_IGNORAR_TEXTO and self._pilha_ignorar_texto:
            if self._pilha_ignorar_texto[-1] == tag.lower():
                self._pilha_ignorar_texto.pop()

    def handle_data(self, data: str) -> None:
        if self.em_title:
            self.titulo_partes.append(data)
        if not self._pilha_ignorar_texto:
            self.texto_partes.append(data)

    # -- resultado ------------------------------------------------------

    @property
    def titulo(self) -> str:
        return "".join(self.titulo_partes).strip()

    @property
    def texto_visivel(self) -> str:
        return " ".join(p.strip() for p in self.texto_partes if p.strip())


# ---------------------------------------------------------------------------
# Processamento de uma pagina
# ---------------------------------------------------------------------------


def processar_pagina(caminho_absoluto: Path, caminho_relativo: str) -> dict:
    html = caminho_absoluto.read_text(encoding="utf-8", errors="replace")

    parser = InventarioParser()
    parser.feed(html)
    parser.close()

    tipo = "capitulo" if caminho_relativo.startswith("capitulos/") else "hub"
    texto_visivel = parser.texto_visivel
    texto_visivel_lower = texto_visivel.lower()

    blocos_presentes: dict = {}
    if tipo == "capitulo":
        for nome_bloco, marcador in MARCADORES_BLOCOS.items():
            blocos_presentes[nome_bloco] = marcador in texto_visivel_lower

    contagem_palavras = len(texto_visivel.split())

    return {
        "arquivo": caminho_relativo,
        "tipo": tipo,
        "titulo": parser.titulo,
        "ids_html": parser.ids,
        "links_locais": parser.links_locais,
        "links_externos": parser.links_externos,
        "imagens": parser.imagens,
        "blocos_presentes": blocos_presentes,
        "contagem_palavras_texto_visivel": contagem_palavras,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def descobrir_arquivos(v3_root: Path) -> list[str]:
    """Retorna a lista de caminhos relativos (hubs + capitulos) a processar."""
    relativos: list[str] = []

    for nome_hub in HUBS_ESPERADOS:
        if (v3_root / nome_hub).is_file():
            relativos.append(nome_hub)
        else:
            print(f"[aviso] hub esperado nao encontrado: {nome_hub}", file=sys.stderr)

    # Se a lista fixa de hubs nao bateu com o que existe de fato na pasta,
    # complementa com quaisquer outros *.html soltos na raiz (fallback de
    # seguranca, ver instrucoes de investigacao no enunciado da tarefa).
    htmls_raiz_reais = {p.name for p in v3_root.glob("*.html")}
    faltando = htmls_raiz_reais - set(HUBS_ESPERADOS)
    for extra in sorted(faltando):
        print(f"[aviso] arquivo .html na raiz nao esperado, incluindo: {extra}", file=sys.stderr)
        relativos.append(extra)

    pasta_capitulos = v3_root / "capitulos"
    capitulos_encontrados = sorted(pasta_capitulos.glob("m*.html"))
    for caminho in capitulos_encontrados:
        relativos.append(f"capitulos/{caminho.name}")

    if len(capitulos_encontrados) != NUM_CAPITULOS:
        print(
            f"[aviso] esperado {NUM_CAPITULOS} capitulos, encontrado "
            f"{len(capitulos_encontrados)}",
            file=sys.stderr,
        )

    return relativos


def montar_inventario(v3_root: Path) -> dict:
    caminhos_relativos = descobrir_arquivos(v3_root)

    paginas = []
    for rel in caminhos_relativos:
        abs_path = v3_root / rel
        paginas.append(processar_pagina(abs_path, rel))

    paginas.sort(key=lambda p: p["arquivo"])

    # --- resumo: ids duplicados entre arquivos --------------------------
    ocorrencias_por_id: dict[str, set] = defaultdict(set)
    for pagina in paginas:
        for id_html in pagina["ids_html"]:
            ocorrencias_por_id[id_html].add(pagina["arquivo"])

    ids_duplicados_entre_arquivos = sorted(
        id_html for id_html, arquivos in ocorrencias_por_id.items() if len(arquivos) > 1
    )

    # --- resumo: total de imagens externas ------------------------------
    total_imagens_externas = sum(
        1
        for pagina in paginas
        for imagem in pagina["imagens"]
        if imagem["is_externa"]
    )

    # --- resumo: capitulos sem cada bloco --------------------------------
    capitulos_sem_bloco: dict[str, list[str]] = defaultdict(list)
    for pagina in paginas:
        if pagina["tipo"] != "capitulo":
            continue
        capitulo_id = Path(pagina["arquivo"]).stem  # ex: 'm05'
        for nome_bloco, presente in pagina["blocos_presentes"].items():
            if not presente:
                capitulos_sem_bloco[nome_bloco].append(capitulo_id)

    capitulos_sem_bloco_final = {
        nome_bloco: sorted(ids)
        for nome_bloco, ids in capitulos_sem_bloco.items()
        if ids
    }

    inventario = {
        "gerado_em": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_paginas": len(paginas),
        "paginas": paginas,
        "resumo": {
            "ids_duplicados_entre_arquivos": ids_duplicados_entre_arquivos,
            "total_imagens_externas": total_imagens_externas,
            "capitulos_sem_bloco": capitulos_sem_bloco_final,
        },
    }
    return inventario


def checagem_de_sanidade(inventario: dict) -> None:
    paginas = inventario["paginas"]
    total_capitulos = sum(1 for p in paginas if p["tipo"] == "capitulo")
    total_hubs = sum(1 for p in paginas if p["tipo"] == "hub")

    print(f"Total de paginas processadas: {len(paginas)}")
    print(f"  capitulos: {total_capitulos}")
    print(f"  hubs: {total_hubs}")

    if total_capitulos != NUM_CAPITULOS:
        print(
            f"[ERRO] esperado {NUM_CAPITULOS} capitulos, encontrado {total_capitulos}",
            file=sys.stderr,
        )
    if total_hubs != len(HUBS_ESPERADOS):
        print(
            f"[ERRO] esperado {len(HUBS_ESPERADOS)} hubs, encontrado {total_hubs}",
            file=sys.stderr,
        )
    if total_capitulos == NUM_CAPITULOS and total_hubs == len(HUBS_ESPERADOS):
        print("Checagem de sanidade: OK (24 capitulos + 9 hubs = 33 paginas).")


def main() -> None:
    if not V3_ROOT.is_dir():
        print(f"[ERRO] pasta da V3 nao encontrada: {V3_ROOT}", file=sys.stderr)
        sys.exit(1)

    inventario = montar_inventario(V3_ROOT)

    SAIDA_JSON.write_text(
        json.dumps(inventario, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Revalida lendo de volta o JSON gerado.
    with SAIDA_JSON.open("r", encoding="utf-8") as f:
        releitura = json.load(f)

    print(f"JSON valido, salvo em: {SAIDA_JSON}")
    checagem_de_sanidade(releitura)

    resumo = releitura["resumo"]
    print(f"IDs duplicados entre arquivos: {len(resumo['ids_duplicados_entre_arquivos'])}")
    print(f"Total de imagens externas: {resumo['total_imagens_externas']}")
    print("Capitulos sem bloco (por bloco):")
    if resumo["capitulos_sem_bloco"]:
        for nome_bloco, ids in resumo["capitulos_sem_bloco"].items():
            print(f"  - {nome_bloco}: {ids}")
    else:
        print("  (nenhum bloco faltando em nenhum capitulo)")


if __name__ == "__main__":
    main()
