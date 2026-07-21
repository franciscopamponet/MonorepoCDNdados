# Rule 04 — Raiz mínima

A raiz é uma vitrine de ponteiros. Só fica na raiz o que tecnicamente não funciona em
outro lugar (ver a tabela em `docs/context/arquitetura.md`).

**Faça:** colocar qualquer novo arquivo dentro da subpasta certa (`docs/` para doc do
molde, `.claude/` para contexto do projeto, `tools/`, etc.).
**Não faça:** criar arquivo na raiz sem requisito técnico que o obrigue a estar lá.
Documentação do molde mora em `docs/`; contexto do projeto, em `.claude/`. O CI checa a
raiz mínima.
