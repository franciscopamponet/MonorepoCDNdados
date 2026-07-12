# ADR 0000 — Distribuição por cópia

**Status:** Aceita

## Contexto
Precisamos distribuir um padrão de projeto de ciência de dados para vários projetos
futuros. As opções incluíam um repo-mãe hospedando N projetos, um gerador externo de
scaffolding (ex.: cookiecutter/cruft) ou cópia independente.

## Decisão
Manter um único **esqueleto canônico**. Cada projeto real nasce como uma **cópia
independente** dele. Sem repo-mãe, sem gerador externo. O scaffolder é embutido
(`tools/init.py`) e roda 1x após a cópia.

## Consequências
- Simplicidade: nenhum acoplamento entre projetos, nenhuma infraestrutura extra.
- Cada projeto é dono do seu destino a partir do nascimento.
- O preço é abrir mão de sincronização automática — coberto pela decisão forward-only
  (ADR 0005).
