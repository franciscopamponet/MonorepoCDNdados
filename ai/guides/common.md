# Guia — common/

## Propósito
Abrigar a lógica compartilhada entre modelos: contratos, tracking e splits. É onde mora
o que todos os modelos reutilizam.

## Pode morar aqui
- O `Protocol` `DataSource` (definição da interface neutra de dados).
- `tracking.py` — **único** módulo que fala com MLflow (Rule 01).
- Utilidades de split, contratos e helpers usados por mais de um modelo.

## Não pode morar aqui
- Lógica específica de um único modelo (isso é `models/<nome>/`).
- Implementações concretas de fonte de dados (isso é `data/sources/`).
- Import de `platform/` (Rule 06).

<!-- TODO: preencher quando a camada common existir — assinatura do Protocol DataSource,
API de common/tracking.py, utilitários de split disponíveis. -->
