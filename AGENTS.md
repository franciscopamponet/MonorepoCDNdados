# AGENTS.md — Ponto de entrada para qualquer IA ou pessoa

Este repositório é um **esqueleto canônico** para projetos de Ciência de Dados do
núcleo de dados da PoliJúnior. Toda a inteligência de execução mora **dentro** do
repo, em `ai/` (o "mini-cérebro nativo"). Nada aqui depende de conhecimento externo.

**Antes de alterar qualquer coisa, a leitura de `ai/rules/` é OBRIGATÓRIA.**

Onde as coisas moram:

- `ai/context/` — o que é o projeto, arquitetura, decisões ratificadas, glossário.
- `ai/rules/`   — comportamento inegociável: o que você pode e não pode fazer. **Leia primeiro.**
- `ai/guides/`  — um guia por etapa do pipeline (config, data, models, common, entrypoints, platform).
- `ai/skills/`  — procedimentos reutilizáveis (`.md`).

Regra de ouro: se algo depende da cabeça de uma pessoa ou de um doc externo para
funcionar, está errado — traga para dentro de `ai/`.
