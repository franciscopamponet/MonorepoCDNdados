#!/usr/bin/env python3
"""Roda TODAS as cancelas de uma vez — o portão local antes do commit.

É o mesmo conjunto de verificações que o `.github/workflows/ci.yml` roda: se este
script passa na sua máquina, o CI passa no PR. Existe para você não descobrir a
falha só depois de dar push.

Ao contrário do CI (que para no primeiro erro), este script roda TODAS as etapas
até o fim e imprime um resumo — você vê todas as falhas de uma vez.

Stdlib only: delega a `uv run` (ruff/pytest) e ao próprio Python (as cancelas de
tools/), sem importar nada além da biblioteca padrão.

Uso:
    python3 tools/check.py            # roda tudo em modo verificação (igual ao CI)
    python3 tools/check.py --fix      # aplica ruff format + ruff check --fix antes
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = sys.executable


# Cada etapa é (rótulo, comando). A ordem espelha o ci.yml.
def etapas(fix: bool) -> list[tuple[str, list[str]]]:
    ruff = (
        [
            ("ruff format", ["uv", "run", "ruff", "format", "."]),
            ("ruff check --fix", ["uv", "run", "ruff", "check", "--fix", "."]),
        ]
        if fix
        else [
            ("ruff check", ["uv", "run", "ruff", "check", "."]),
            ("ruff format --check", ["uv", "run", "ruff", "format", "--check", "."]),
        ]
    )
    return [
        *ruff,
        ("pytest", ["uv", "run", "pytest"]),
        ("raiz mínima (Rule 04)", [PY, "tools/check_root.py"]),
        ("manifesto em sync (Rules 02/03)", [PY, "tools/check_manifest.py"]),
        ("mlflow centralizado (Rule 01)", [PY, "tools/check_mlflow.py"]),
        ("plataforma isolada (Rule 06)", [PY, "tools/check_platform.py"]),
    ]


def rodar(rotulo: str, comando: list[str]) -> bool:
    print(f"\n{'=' * 70}\n▶ {rotulo}\n{'=' * 70}")
    try:
        resultado = subprocess.run(comando, cwd=RAIZ)
    except FileNotFoundError:
        print(f"ERRO: comando não encontrado: {comando[0]!r}.")
        if comando[0] == "uv":
            print("Instale o uv (https://docs.astral.sh/uv/) — o repo depende dele.")
        return False
    return resultado.returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Roda todas as cancelas (portão local pré-commit)."
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Aplica ruff format e ruff check --fix antes de verificar.",
    )
    args = parser.parse_args()

    resultados = [(rotulo, rodar(rotulo, cmd)) for rotulo, cmd in etapas(args.fix)]

    print(f"\n{'=' * 70}\nRESUMO\n{'=' * 70}")
    for rotulo, ok in resultados:
        print(f"  {'OK  ' if ok else 'FALHOU'}  {rotulo}")

    falharam = [rotulo for rotulo, ok in resultados if not ok]
    if falharam:
        print(f"\n{len(falharam)} cancela(s) reprovaram. Corrija antes de commitar.")
        if not args.fix:
            print("Dica: `python3 tools/check.py --fix` resolve estilo automaticamente.")
        return 1

    print("\nTudo verde. Pode commitar com segurança.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
