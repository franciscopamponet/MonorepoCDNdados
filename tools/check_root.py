#!/usr/bin/env python3
"""Cancela: RAIZ MÍNIMA (Rule 04).

A raiz é uma vitrine de ponteiros, não um depósito. Só fica na raiz o que
tecnicamente não funciona em outro lugar. Este script mantém a allowlist explícita
e falha se aparecer qualquer coisa nova solta na raiz.

Stdlib only: roda sem `uv sync`.

Uso:
    python3 tools/check_root.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Cada entrada tem um motivo TÉCNICO para estar na raiz. Ver a tabela em
# .claude/context/arquitetura.md. Adicionar algo aqui é uma decisão de arquitetura,
# não uma conveniência — se não há requisito técnico, o arquivo vai para uma subpasta.
ARQUIVOS_PERMITIDOS = {
    "AGENTS.md": "tool discovery: como uma IA descobre o padrão ao clonar o repo",
    "CLAUDE.md": "tool discovery: ponteiro para o AGENTS.md",
    "README.md": "é o que o GitHub renderiza na página do repo",
    "pyproject.toml": "o uv só procura na raiz",
    "uv.lock": "o uv só procura na raiz",
    ".gitignore": "o Git só lê neste caminho exato",
}

PASTAS_PERMITIDAS = {
    ".github": "o GitHub Actions só executa a partir daqui",
    ".claude": "mini-cérebro nativo: 100% do conteúdo de IA (ADR 0006)",
    "common": "lógica compartilhada entre modelos",
    "config": "config por modelo (pipeline config-driven)",
    "data": "implementações concretas da interface de dados",
    "docs": "documentação e ADRs",
    "entrypoints": "launchers finos",
    "models": "modelos, na anatomia de 5 arquivos",
    "platform": "casca opcional de plataforma (podada se toggle = Não)",
    "tests": "testes",
    "tools": "scripts de scaffolding e verificação",
}

# Para onde mandar o intruso, conforme o tipo.
SUGESTOES = {
    ".md": "docs/ (ou .claude/context/ se for contexto de IA)",
    ".py": "tools/ se for script; common/ se for lógica compartilhada",
    ".yaml": "config/ se for config de modelo; platform/ se for de plataforma",
    ".yml": "config/ se for config de modelo; platform/ se for de plataforma",
    ".txt": "docs/ — e se for requirements, ele NÃO existe aqui (Rule 02)",
    ".sh": "tools/",
    ".ipynb": "não versione notebooks soltos; use models/<nome>/ ou docs/",
}


def entradas_versionadas() -> set[str]:
    """Entradas de primeiro nível rastreadas pelo git.

    Usar o git evita falso positivo com artefato gerado (mlruns/, .venv/, mlflow.db):
    o que importa é o que está COMMITADO na raiz.
    """
    try:
        saida = subprocess.run(
            ["git", "ls-files"],
            cwd=RAIZ,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return entradas_do_filesystem()

    return {linha.split("/")[0] for linha in saida.splitlines() if linha.strip()}


def entradas_do_filesystem() -> set[str]:
    """Fallback sem git: ignora o que sabidamente é gerado/ignorado."""
    gerados = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        "mlruns",
        "mlartifacts",
        "mlflow.db",
        "dist",
        "build",
        ".DS_Store",
        ".idea",
        ".vscode",
        ".uv_cache",
        ".env",
    }
    return {p.name for p in RAIZ.iterdir() if p.name not in gerados}


def main() -> int:
    permitidas = set(ARQUIVOS_PERMITIDOS) | set(PASTAS_PERMITIDAS)
    intrusos = sorted(entradas_versionadas() - permitidas)

    if not intrusos:
        print("OK: raiz mínima respeitada (Rule 04).")
        return 0

    print("ERRO: RAIZ MÍNIMA VIOLADA (Rule 04)\n")
    print("A raiz deste repo é uma VITRINE DE PONTEIROS, não um depósito. Só pode")
    print("ficar na raiz o que tecnicamente não funciona em outro lugar — o critério")
    print("é requisito técnico, não conveniência. Ver .claude/context/arquitetura.md.\n")
    print("Encontrei na raiz, sem permissão:\n")

    for nome in intrusos:
        destino = SUGESTOES.get(Path(nome).suffix, "a subpasta correspondente ao seu papel")
        print(f"  - {nome}")
        print(f"      -> mova para: {destino}")

    print("\nSe você acredita que este arquivo TEM um requisito técnico que o obriga")
    print("a estar na raiz, adicione-o à allowlist em tools/check_root.py junto com o")
    print("motivo técnico — e registre a decisão em docs/adr/.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
