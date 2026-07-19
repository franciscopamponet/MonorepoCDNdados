# ADR 0007 — As cancelas de CI sobrevivem ao toggle de plataforma

**Status:** Aceita

## Contexto
Ao transformar as rules em cancelas automáticas (scripts em `tools/` + CI), surgiu uma
pergunta que não estava respondida em nenhuma decisão anterior: quando o toggle
Databricks é **Não**, o `tools/init.py` poda `platform/` e os artefatos de plataforma —
as cancelas de verificação também deveriam ser podadas?

Até então, `tools/` continha apenas `init.py` (autodestrutivo) e `gen_conda.py`
(artefato de plataforma). A lógica do `init.py` assumia que, sem Databricks, `tools/`
desaparecia por inteiro. Ao adicionar `check_root.py`, `check_manifest.py`,
`check_mlflow.py`, `check_platform.py` e o agregador `check.py`, essa premissa deixou de
valer e um teste (`test_init_rejeita_segunda_execucao`) passou a falhar.

## Decisão
As cancelas de verificação são **infraestrutura de núcleo**, não artefatos de
plataforma. Elas **sobrevivem ao toggle** e continuam no projeto-cópia com ou sem
Databricks. Só `tools/gen_conda.py` (o gerador do `conda.yaml`) permanece como artefato
de plataforma podado quando o toggle é Não.

Para que isso seja coerente, `tools/check_manifest.py` **pula com sucesso** quando
`platform/` não existe (não há manifesto a checar). Assim, o mesmo
`.github/workflows/ci.yml` roda idêntico nos dois toggles — não existem duas versões do
CI.

## Consequências
- O CI é o mesmo com ou sem Databricks: uma regra escrita continua sendo uma cancela
  verificada em qualquer projeto-cópia, independentemente do toggle.
- `tools/` **não** desaparece mais quando o toggle é Não: retém as cancelas. O
  `init.py` só remove `tools/` se ela ficar vazia (o que não ocorre mais), e segue se
  autodestruindo normalmente.
- A lista `ARTEFATOS_DE_PLATAFORMA` do `init.py` é a fronteira explícita: o que está
  nela é podado; o que não está sobrevive. Adicionar um novo script de plataforma exige
  incluí-lo lá; um novo script de núcleo, não.
- Reforça o invariante central (o núcleo é idêntico com ou sem Databricks): a garantia
  de qualidade do núcleo não depende da presença da casca de plataforma.
