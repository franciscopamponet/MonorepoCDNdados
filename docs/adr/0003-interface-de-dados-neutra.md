# ADR 0003 — Interface de dados neutra

**Status:** Aceita

## Contexto
A origem física do dado varia por projeto e por ambiente (tabela Spark no Databricks,
Parquet local, banco SQL). Acoplar `prepare_data` à origem torna o pipeline rígido e
difícil de testar.

## Decisão
Definir um `Protocol` `DataSource` em `common/`. As implementações concretas
(`SparkTableSource`, `ParquetSource`, `SQLSource`) moram em `data/sources/` e são
escolhidas via config. O código de preparação só pede o dado à interface; nunca sabe de
onde ele vem.

## Consequências
- Trocar a origem do dado é trocar uma linha de config, não reescrever código.
- Testar o pipeline fica fácil (implementação de fonte fake/local).
- A definição do `Protocol` fica em `common/`; as implementações, em `data/sources/`.
