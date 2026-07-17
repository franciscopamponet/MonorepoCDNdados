# ADR 0006 — Mini-cérebro em `.claude/`

**Status:** Aceita

Substitui parcialmente a [ADR 0004](0004-mini-cerebro-e-raiz-minima.md) — apenas
quanto à **localização** do mini-cérebro. Os princípios de mini-cérebro nativo e de
raiz mínima seguem intactos.

## Contexto
A ADR 0004 colocou 100% do conteúdo de IA em `ai/`, com o argumento da neutralidade
("legível por qualquer IA, não só Claude"). Na prática, o Claude Code é a ferramenta
usada no dia a dia do núcleo, e `.claude/` é o diretório que ele reconhece por
convenção como área do projeto — o que reduz o atrito de uso.

Foi levantado, e registrado aqui por honestidade, que o rename **não** faz o Claude
carregar automaticamente o conteúdo: o carregamento automático vem do `CLAUDE.md` na
raiz, que aponta para o `AGENTS.md`. O ganho é de convenção e ergonomia, não de
carregamento automático.

## Decisão
Mover o mini-cérebro de `ai/` para `.claude/`, mantendo a estrutura interna
(`context/`, `rules/`, `guides/`, `skills/`) e todos os ponteiros atualizados.

## Consequências
- Alinhamento com a ferramenta de fato usada no núcleo; menor atrito no dia a dia.
- O conteúdo permanece **neutro**: qualquer IA ou pessoa lê os mesmos `.md`. O
  `AGENTS.md` na raiz continua sendo o ponto de entrada neutro e aponta para lá.
- **Trade-off aceito:** `.claude/` é uma pasta oculta — some de `ls` e da listagem do
  GitHub, o que reduz a descoberta por humanos. Mitigação: `AGENTS.md`, `CLAUDE.md` e
  `README.md` na raiz apontam explicitamente para ela.
- **Trade-off aceito:** o nome sugere acoplamento a uma ferramenta específica, apesar
  do conteúdo ser neutro. Se outra IA virar padrão no núcleo, o conteúdo se move sem
  reescrita — só os ponteiros mudam.
- A regra de raiz mínima é reforçada: `.claude/` não polui a raiz visível.
