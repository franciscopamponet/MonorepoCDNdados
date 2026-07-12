# ADR 0001 — Toggle Databricks

**Status:** Aceita

## Contexto
Alguns projetos rodam em Databricks, outros não. Não queremos que a dependência de
plataforma contamine o núcleo do pipeline nem que existam duas versões do esqueleto.

## Decisão
`tools/init.py` pergunta "Databricks? S/N". Se Não, poda a pasta `platform/`. Também
seta o modo dos `entrypoints/` (local vs. serverless). O núcleo nunca é tocado pelo
toggle.

## Consequências
- O núcleo permanece neutro e idêntico em ambos os cenários.
- `platform/` é a casca inteira que o toggle liga/desliga (invariante central).
- Nada do núcleo pode importar de `platform/` (ADR/Rule de plataforma opcional).
