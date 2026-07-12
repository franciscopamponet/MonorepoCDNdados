# Decisões ratificadas

As 6 decisões abaixo estão **ratificadas**. Não reabrir, não questionar — apenas
obedecer. Cada uma tem um ADR correspondente em `docs/adr/` (0000 a 0005).

## 0. Distribuição por cópia

**Decisão:** um esqueleto canônico único; cada projeto real é uma **cópia
independente** dele. Sem repo-mãe hospedando N projetos, sem gerador externo. O
scaffolder é embutido (`tools/init.py`) e roda 1x após a cópia.

**Racional:** cópia independente é simples, sem acoplamento entre projetos e sem
infraestrutura extra. Cada projeto vira dono do seu destino no momento em que nasce.

## 1. Toggle Databricks

**Decisão:** `tools/init.py` pergunta "Databricks? S/N", poda a pasta `platform/` se
Não e seta o modo dos `entrypoints/`. O núcleo nunca é tocado.

**Racional:** mantém o núcleo neutro. Databricks é uma camada opcional, não uma
dependência estrutural. Um único toggle liga/desliga a casca inteira.

## 2. Fonte única de dependências

**Decisão:** `pyproject.toml` + `uv`, com `uv.lock` versionado. O `conda.yaml` /
requirements do Databricks são **GERADOS** a partir dele, nunca escritos à mão.

**Racional:** mata um bug real de um projeto anterior, onde `requirements` e `conda`
divergiram. Uma fonte só, um lockfile, zero drift.

## 3. Interface de dados neutra

**Decisão:** um `Protocol` `DataSource` definido em `common/`, com implementações
concretas (`SparkTableSource`, `ParquetSource`, `SQLSource`) em `data/sources/`,
escolhidas via config. O código de preparação só pede o dado à interface; nunca sabe
de onde ele vem.

**Racional:** desacopla a lógica do pipeline da origem física do dado. Trocar Parquet
por tabela Spark é trocar uma linha de config, não reescrever `prepare_data`.

## 4. Mini-cérebro + raiz mínima

**Decisão:** 100% do conteúdo de IA em `ai/`. Na raiz, só ponteiros (`AGENTS.md`,
`CLAUDE.md`). Nada de `_guia.md` espalhado por pasta. Convenção legível por qualquer
IA, não só Claude.

**Racional:** o conhecimento viaja com o repo e é encontrável num lugar só. Ponteiros
neutros (`AGENTS.md`) permitem que qualquer ferramenta descubra o padrão.

## 5. Evolução forward-only

**Decisão:** o esqueleto evolui pra frente; projetos futuros herdam melhorias,
projetos em andamento ficam congelados na versão em que nasceram. Sem `cruft`, sem
auto-sync, sem back-propagation.

**Racional:** back-propagation de mudanças de template para projetos vivos é fonte de
conflitos e quebras. Congelar na versão de nascimento dá estabilidade; melhorias valem
para quem nasce depois.
