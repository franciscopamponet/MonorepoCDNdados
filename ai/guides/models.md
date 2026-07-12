# Guia — models/

## Propósito
Abrigar cada modelo em `models/<nome>/`, seguindo a **anatomia de 5 arquivos**
(Rule 00). É o coração do núcleo do pipeline.

## Pode morar aqui
- Uma pasta por modelo, em `snake_case`, com **exatamente** os 5 arquivos:
  `prepare_data.py`, `build_model.py`, `train.py`, `evaluate_model.py`,
  `orchestrator.py`.
- Lógica específica daquele modelo.

## Não pode morar aqui
- Um 6º arquivo, renomeações ou fusões dos 5 (Rule 00).
- `import mlflow` fora do fluxo `orchestrator.py` → `common/tracking.py` (Rule 01).
- Lógica compartilhada entre modelos (isso é `common/`).
- Caminhos/hiperparâmetros hardcoded (Rule 07).

<!-- TODO: preencher quando o primeiro modelo existir — responsabilidade de cada um dos
5 arquivos, contrato de entrada/saída entre eles, como o orchestrator amarra tudo. -->
