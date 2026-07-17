# Guia — entrypoints/

## Propósito
Abrigar os **launchers finos** que disparam o pipeline. São casca de entrada: leem o
config, escolhem o modelo e chamam o `orchestrator.py`. O modo (local vs. serverless)
é definido pelo toggle no `tools/init.py`.

## Pode morar aqui
- Launchers finos por modo de execução (local / serverless).
- Parsing de argumentos de linha de comando que apenas repassa ao núcleo.

## Não pode morar aqui
- Lógica de pipeline (prepare/build/train/evaluate) — isso é `models/`.
- Regra de negócio ou tracking direto de MLflow (Rule 01).
- Dependência que quebre com `platform/` inexistente quando o toggle for Não (Rule 06).

<!-- TODO: preencher quando os entrypoints existirem — como o toggle define o modo,
assinatura do launcher, exemplo de invocação local e serverless. -->
