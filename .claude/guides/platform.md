# Guia — platform/

## Propósito
Abrigar a casca **opcional** de Databricks. Só sobrevive se o toggle for SIM; o
`tools/init.py` poda a pasta inteira se for Não (Rule 06). O núcleo é idêntico com ou
sem ela.

## Pode morar aqui
- `databricks.yml`, `resources/`, `MLProject`.
- `conda.yaml` — **gerado** a partir do `pyproject.toml`, nunca escrito à mão (Rule 02, 03).

## Não pode morar aqui
- Qualquer coisa que o núcleo importe (o núcleo nunca depende de `platform/` — Rule 06).
- `conda.yaml`/requirements editados manualmente.

<!-- TODO: preencher quando a camada de plataforma existir — o que o init.py gera aqui,
como o conda.yaml é derivado do pyproject, como os resources mapeiam para o pipeline. -->
