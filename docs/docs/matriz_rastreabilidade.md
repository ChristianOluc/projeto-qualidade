# Matriz de Rastreabilidade — BiblioTech

## Objetivo

Relacionar os requisitos funcionais do BiblioTech aos casos de teste
implementados, garantindo que todos os requisitos possuam cobertura.

## Matriz

| Requisito | CT01 | CT02 | CT03 | CT04 | CT05 | CT06 | CT07 | CT08 | CT09 | CT10 | CT11 | CT12 |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|
| RF01      | X    | X    | X    | X    | X    |      |      |      |      |      |      |      |
| RF02      |      |      |      |      |      | X    | X    | X    | X    |      |      |      |
| RF03      |      |      |      |      |      |      |      |      |      | X    | X    | X    |

## Requisitos

### RF01 — Permissão para empréstimo

O usuário poderá realizar um novo empréstimo quando:

- estiver ativo;
- não possuir pendências;
- possuir menos de 3 empréstimos ativos.

Casos relacionados:

- CT01 — Usuário ativo, sem pendência e sem empréstimos ativos.
- CT02 — Usuário inativo.
- CT03 — Usuário com pendência.
- CT04 — Usuário com quantidade de empréstimos abaixo do limite.
- CT05 — Usuário com 3 empréstimos ativos.

### RF02 — Multa por atraso

A multa deverá seguir as seguintes regras:

- 0 dias ou menos → R$ 0,00;
- 1 a 7 dias → R$ 2,00 por dia;
- acima de 7 dias → R$ 14,00 + R$ 3,00 por dia excedente.

Casos relacionados:

- CT06 — Sem atraso.
- CT07 — Atraso de 1 dia.
- CT08 — Atraso de 7 dias.
- CT09 — Atraso acima de 7 dias.

### RF03 — Classificação de atraso

A classificação deverá seguir:

- 0 dias ou menos → "sem atraso";
- 1 a 7 dias → "atraso leve";
- 8 a 30 dias → "atraso moderado";
- mais de 30 dias → "atraso grave".

Casos relacionados:

- CT10 — Sem atraso.
- CT11 — Atraso leve.
- CT12 — Atraso moderado/grave.

## Verificação de rastreabilidade

Todos os requisitos funcionais possuem pelo menos um caso de teste associado.

- RF01 → possui testes associados.
- RF02 → possui testes associados.
- RF03 → possui testes associados.

Não existem requisitos sem cobertura de testes dentro do escopo definido.
