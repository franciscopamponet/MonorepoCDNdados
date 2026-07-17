# AGENTS.md — Ponto de entrada para qualquer IA ou pessoa

Este repositório é um **esqueleto canônico** para projetos de Ciência de Dados do
núcleo de dados da PoliJúnior. Toda a inteligência de execução mora **dentro** do
repo, em `.claude/` (o "mini-cérebro nativo"). Nada aqui depende de conhecimento externo.

**Antes de alterar qualquer coisa, a leitura de `.claude/rules/` é OBRIGATÓRIA.**

Onde as coisas moram:

- `.claude/context/` — o que é o projeto, arquitetura, decisões ratificadas, glossário.
- `.claude/rules/`   — comportamento inegociável: o que você pode e não pode fazer. **Leia primeiro.**
- `.claude/guides/`  — um guia por etapa do pipeline (config, data, models, common, entrypoints, platform).
- `.claude/skills/`  — procedimentos reutilizáveis (`.md`).

> Nota: `.claude/` é uma pasta **oculta**. Se você não a enxerga, use `ls -a`.
> Apesar do nome, o conteúdo é neutro e vale para qualquer IA ou pessoa — não só
> para o Claude (ver `docs/adr/0006-cerebro-em-claude.md`).

Regra de ouro: se algo depende da cabeça de uma pessoa ou de um doc externo para
funcionar, está errado — traga para dentro de `.claude/`.
