# Guia — config/

## Propósito
Guardar a configuração por modelo que dirige o pipeline. Caminhos, tabelas,
hiperparâmetros, escolha de `DataSource` e nomes de experimento moram aqui — não no
código (ver Rule 07).

## Pode morar aqui
- Um arquivo de config por modelo, com nome batendo com o modelo (`config/<nome>.*` ↔
  `models/<nome>/`) — ver Rule 05.
- Valores de ambiente/execução que o pipeline lê em tempo de rodada.

## Não pode morar aqui
- Lógica Python de pipeline (isso é `models/` / `common/`).
- Segredos/credenciais versionados.

<!-- TODO: preencher quando a camada de config existir — formato escolhido (YAML/TOML),
schema, como o núcleo carrega e valida o config, exemplo comentado. -->
