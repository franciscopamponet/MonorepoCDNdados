"""Único ponto de contato do repo com MLflow (Rule 01).

Nenhum outro arquivo importa mlflow diretamente. Só o `orchestrator.py` de cada
modelo usa este wrapper, e este wrapper é quem encapsula a diferença entre rodar
dentro e fora do Databricks.

# TODO — PENDÊNCIA CONHECIDA, AINDA NÃO VALIDADA EMPIRICAMENTE
# O comportamento FORA do Databricks precisa de validação empírica antes de ser
# cravado. Pontos em aberto:
#   - Model Registry fora do Databricks exige um backend store configurado; ainda
#     não validamos qual configuração mínima funciona de ponta a ponta.
#   - A convenção de experiment_name com path '/Shared/...' é específica do
#     Databricks e NÃO se aplica localmente (usamos nome simples).
# Por isso este wrapper é DEFENSIVO: o comportamento LOCAL (tracking em ./mlruns,
# experimento por nome simples) é o default seguro; o comportamento Databricks fica
# atrás da flag `tracking.databricks` vinda do config. Não cravar certezas sobre o
# caminho Databricks até validar em ambiente real.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from common.config import TrackingConfig


class Tracker:
    """Wrapper fino sobre MLflow, configurado a partir de `TrackingConfig`.

    Uso típico (no `orchestrator.py`):

        tracker = Tracker(config.tracking)
        with tracker.start_run():
            tracker.log_params(params)
            tracker.log_metrics(metrics)
            tracker.log_model(model, "model")
    """

    def __init__(self, config: TrackingConfig) -> None:
        import mlflow

        self._mlflow = mlflow
        self.config = config

        if config.databricks:
            # Caminho Databricks: NÃO validado empiricamente (ver TODO no topo).
            # Deixamos o tracking_uri/registry_uri a cargo do ambiente Databricks,
            # sobrescrevendo apenas se o config trouxer valores explícitos.
            if config.tracking_uri and config.tracking_uri != "./mlruns":
                mlflow.set_tracking_uri(config.tracking_uri)
            if config.registry_uri:
                mlflow.set_registry_uri(config.registry_uri)
        else:
            # Caminho LOCAL (default seguro): tracking em ./mlruns, nome simples.
            mlflow.set_tracking_uri(config.tracking_uri)
            if config.registry_uri:
                mlflow.set_registry_uri(config.registry_uri)

        mlflow.set_experiment(config.experiment_name)

    @contextmanager
    def start_run(self, run_name: str | None = None, **kwargs: Any):
        with self._mlflow.start_run(run_name=run_name, **kwargs) as run:
            yield run

    def log_params(self, params: dict[str, Any]) -> None:
        self._mlflow.log_params(params)

    def log_metrics(self, metrics: dict[str, float], step: int | None = None) -> None:
        self._mlflow.log_metrics(metrics, step=step)

    def log_model(self, model: Any, artifact_path: str, **kwargs: Any) -> None:
        # sklearn como flavor default do esqueleto; modelos com outro flavor
        # sobrescrevem via kwargs/uso direto no orchestrator.
        self._mlflow.sklearn.log_model(model, artifact_path, **kwargs)

    def set_experiment(self, experiment_name: str) -> None:
        self._mlflow.set_experiment(experiment_name)
