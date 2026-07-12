# O que é este projeto

Este é o **esqueleto (boilerplate) canônico** para projetos de Ciência de Dados do
núcleo de dados da PoliJúnior. Ele NÃO é um projeto real: é o molde a partir do qual
cada projeto real nasce.

## Para que serve

Padronizar como um projeto de ciência de dados é estruturado, executado e evoluído,
de modo que qualquer pessoa (ou IA) que clone uma cópia dele entenda e siga o padrão
**sozinha**, sem depender de conhecimento externo.

## Princípio-guia: mini-cérebro nativo

Toda a inteligência de execução — contexto, rules, guias, skills — viaja DENTRO do
repo, como arquivos versionados em `ai/`. Se algo depende de conhecimento externo
(a cabeça de uma pessoa, um vault pessoal, um doc no Drive) para funcionar, está errado.

## Como se usa

1. **Copie** este esqueleto para um novo diretório (cópia independente — ver
   [decisoes.md](decisoes.md), decisão 0). Não há repo-mãe hospedando N projetos.
2. **Rode `tools/init.py` uma única vez.** Ele pergunta o toggle Databricks (S/N),
   poda a pasta `platform/` se Não, define o modo dos `entrypoints/` e nomeia o projeto.
3. **Comece a trabalhar** dentro da estrutura já pronta: config por modelo em `config/`,
   modelos em `models/<nome>/` (anatomia de 5 arquivos), lógica compartilhada em `common/`.

## O que ler antes de mexer

- [arquitetura.md](arquitetura.md) — a estrutura-alvo e os invariantes.
- [decisoes.md](decisoes.md) — as 6 decisões já ratificadas (não reabrir).
- `../rules/` — comportamento inegociável. **Leitura obrigatória antes de qualquer alteração.**
