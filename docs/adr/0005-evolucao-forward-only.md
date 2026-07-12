# ADR 0005 — Evolução forward-only

**Status:** Aceita

## Contexto
Templates que fazem back-propagation de mudanças para projetos vivos (ex.: `cruft`
update) geram conflitos e quebras em código já em andamento. Precisamos de um modelo de
evolução previsível.

## Decisão
O esqueleto evolui **pra frente**. Projetos futuros herdam melhorias no momento em que
nascem. Projetos em andamento ficam **congelados** na versão do esqueleto em que
nasceram. Sem `cruft`, sem auto-sync, sem back-propagation.

## Consequências
- Estabilidade: um projeto vivo nunca é surpreendido por uma mudança de template.
- Melhorias valem para quem nasce depois; não há re-sync automático.
- Combina com a distribuição por cópia (ADR 0000): cópia independente, destino próprio.
