# ADR 0004 — Mini-cérebro nativo + raiz mínima

**Status:** Parcialmente substituída pela [ADR 0006](0006-cerebro-em-claude.md)

> A ADR 0006 mudou apenas a **localização** do mini-cérebro (`ai/` → `.claude/`).
> O princípio do mini-cérebro nativo e o princípio da raiz mínima continuam
> **plenamente válidos**. Onde este documento diz `ai/`, leia `.claude/`.

## Contexto
Conhecimento de execução espalhado (na cabeça das pessoas, em docs externos, ou em
`_guia.md` soltos por pasta) faz o padrão depender de contexto que não viaja com o
repo. E raiz poluída esconde o que importa.

## Decisão
100% do conteúdo de IA mora em `ai/` (o "mini-cérebro nativo"): contexto, rules,
guias, skills. Na raiz, só ponteiros neutros (`AGENTS.md`, `CLAUDE.md`) e o que
tecnicamente precisa estar lá. Convenção legível por qualquer IA, não só Claude.

## Consequências
- Qualquer pessoa/IA que clone o repo encontra o padrão num lugar só e o segue sozinha.
- A raiz vira vitrine de ponteiros; o CI checa a raiz mínima.
- Proibido `_guia.md` espalhado por pasta ou regra fora de `ai/`.
