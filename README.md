# <!-- PREENCHER: nome do projeto -->

> **Template.** Este README é herdado do esqueleto canônico de projetos de Ciência de
> Dados do núcleo de dados da PoliJúnior. Os trechos marcados com
> `<!-- PREENCHER: ... -->` devem ser completados por cada projeto-cópia.

<!-- PREENCHER: uma frase dizendo o que este projeto faz. -->

## O que é

Este projeto nasceu como **cópia independente** do esqueleto canônico. Toda a
inteligência de execução (contexto, rules, guias) mora em [`ai/`](ai/) — o
"mini-cérebro nativo". Comece por [`AGENTS.md`](AGENTS.md).

## Como começar (a partir do esqueleto)

1. **Copie** o esqueleto para um novo diretório (cópia independente, sem vínculo com o
   esqueleto original).
2. **Rode o scaffolder uma única vez:**
   ```bash
   uv run tools/init.py
   ```
   Ele pergunta o toggle Databricks (S/N), poda `platform/` se Não, define o modo dos
   `entrypoints/` e nomeia o projeto.
3. **Instale as dependências:**
   ```bash
   uv sync
   ```
4. Comece a trabalhar dentro da estrutura pronta.

## Como rodar

<!-- PREENCHER: comando(s) para rodar o pipeline deste projeto (entrypoint, config). -->

## Onde ficam as regras

**A leitura de [`ai/rules/`](ai/rules/) é obrigatória antes de qualquer alteração.**

- Contexto e arquitetura: [`ai/context/`](ai/context/)
- Rules (o que pode/não pode): [`ai/rules/`](ai/rules/)
- Guias por etapa: [`ai/guides/`](ai/guides/)
- Decisões de arquitetura: [`docs/adr/`](docs/adr/)

## Estrutura

Ver [`ai/context/arquitetura.md`](ai/context/arquitetura.md) para a estrutura-alvo
completa e os invariantes.

---

<!-- PREENCHER: seção de contato/responsáveis do projeto, se aplicável. -->
