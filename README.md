# <!-- PREENCHER: nome do projeto -->

> **Template.** Este README é herdado do esqueleto canônico de projetos de Ciência de
> Dados do núcleo de dados da PoliJúnior. Os trechos marcados com
> `<!-- PREENCHER: ... -->` devem ser completados por cada projeto-cópia.

<!-- PREENCHER: uma frase dizendo o que este projeto faz. -->

## O que é

Este projeto nasceu como **cópia independente** do esqueleto canônico. Toda a
inteligência de execução (contexto, rules, guias) mora em [`.claude/`](.claude/) — o
"mini-cérebro nativo". Comece por [`AGENTS.md`](AGENTS.md).

## Como começar (a partir do esqueleto)

1. **Copie** o esqueleto para um novo diretório (cópia independente, sem vínculo com o
   esqueleto original).
2. **Rode o scaffolder uma única vez** (usa só a stdlib — roda ANTES do `uv sync`):
   ```bash
   python3 tools/init.py
   ```
   Ele pergunta o toggle Databricks (S/N), poda `platform/` se Não, define o modo dos
   `entrypoints/` e nomeia o projeto. Ao terminar, se autodestrói.
3. **Instale as dependências:**
   ```bash
   uv sync
   ```
4. Comece a trabalhar dentro da estrutura pronta. Passo a passo completo na skill
   [`iniciar-projeto-novo-a-partir-do-esqueleto.md`](.claude/skills/iniciar-projeto-novo-a-partir-do-esqueleto.md).

## Como rodar

O pipeline é dirigido pelo config do modelo (Rule 07). Execução local:

```bash
uv run python entrypoints/run_local.py --config config/<modelo>.yaml
# saída: run_id: ... / métricas: {'accuracy': ..., 'f1': ...}
```

Antes de commitar, rode as cancelas (mesmo conjunto do CI):

```bash
python3 tools/check.py     # ruff + pytest + raiz mínima + manifesto + isolamentos
```

<!-- PREENCHER: se este projeto tem um comando/entrypoint próprio além do acima, descreva-o. -->

## Onde ficam as regras

**A leitura de [`.claude/rules/`](.claude/rules/) é obrigatória antes de qualquer alteração.**

- Contexto e arquitetura: [`.claude/context/`](.claude/context/)
- Rules (o que pode/não pode): [`.claude/rules/`](.claude/rules/)
- Guias por etapa: [`.claude/guides/`](.claude/guides/)
- Skills (procedimentos passo a passo): [`.claude/skills/`](.claude/skills/)
- Decisões de arquitetura: [`docs/adr/`](docs/adr/)

> `.claude/` é uma pasta oculta — use `ls -a` para enxergá-la.

## Estrutura

Ver [`.claude/context/arquitetura.md`](.claude/context/arquitetura.md) para a estrutura-alvo
completa e os invariantes.

---

<!-- PREENCHER: seção de contato/responsáveis do projeto, se aplicável. -->
