# Rule 01 — MLflow é centralizado

Só o `orchestrator.py` fala com MLflow, e sempre através de `common/tracking.py`.

**Faça:** rotear todo logging de experimento pelo `orchestrator.py` → `common/tracking.py`.
**Não faça:** `import mlflow` em `prepare_data.py`, `build_model.py`, `train.py`,
`evaluate_model.py`, em `data/`, em `config/` ou em qualquer outro lugar. Nenhum
arquivo além de `common/tracking.py` importa mlflow diretamente.
