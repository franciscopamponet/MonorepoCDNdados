# ADR 0002 — Fonte única de dependências

**Status:** Aceita

## Contexto
Num projeto anterior, `requirements.txt` e `conda.yaml` divergiram, causando builds
inconsistentes entre ambiente local e Databricks. Manter duas listas de dependências à
mão é fonte garantida de drift.

## Decisão
`pyproject.toml` + `uv` são a **fonte única** de dependências, com `uv.lock`
versionado. Os artefatos de plataforma (`conda.yaml`, requirements) são **gerados** a
partir do `pyproject.toml`, nunca escritos à mão.

## Consequências
- Uma fonte só, um lockfile, zero divergência.
- Mudar dependência exige regerar os artefatos de plataforma no mesmo commit (ADR 0003
  / manifesto em sync), o que o CI verifica.
- Editar `conda.yaml` à mão passa a ser proibido.
