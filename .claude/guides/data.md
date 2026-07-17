# Guia — data/

## Propósito
Abrigar as **implementações concretas** da interface de dados neutra `DataSource`
(definida em `common/`). É a camada que sabe DE ONDE o dado vem; o resto do pipeline não.

## Pode morar aqui
- `data/sources/` com implementações concretas: `SparkTableSource`, `ParquetSource`,
  `SQLSource`, etc., cada uma cumprindo o `Protocol` `DataSource`.
- Adaptadores de leitura/escrita específicos de uma origem.

## Não pode morar aqui
- A definição do `Protocol` `DataSource` (isso mora em `common/`).
- Lógica de modelo (isso é `models/`).
- Caminhos/tabelas hardcoded — eles vêm do config (Rule 07).

<!-- TODO: preencher quando a camada de dados existir — assinatura do Protocol,
implementações disponíveis, como o config seleciona uma fonte, exemplo de uso. -->
