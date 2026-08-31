# Roteiro de Testes — BiblioTech

## RF01 — Permissão para empréstimo

| ID | Usuário ativo | Pendência | Empréstimos ativos | Resultado esperado |
|---|---|---|---:|---|
| CT01 | Sim | Não | 0 | True |
| CT02 | Sim | Não | 2 | True |
| CT03 | Sim | Não | 3 | False |
| CT04 | Sim | Não | 4 | False |
| CT05 | Não | Não | 0 | False |
| CT06 | Sim | Sim | 0 | False |

## RF02 — Multa por atraso

| ID | Dias de atraso | Resultado esperado |
|---|---:|---:|
| CT07 | 0 | R$ 0,00 |
| CT08 | 3 | R$ 6,00 |
| CT09 | 7 | R$ 14,00 |
| CT10 | 8 | R$ 17,00 |
| CT11 | 10 | R$ 23,00 |

## RF03 — Classificação de atraso

| ID | Dias de atraso | Resultado esperado |
|---|---:|---|
| CT12 | 0 | sem atraso |
| CT13 | 1 | atraso leve |
| CT14 | 7 | atraso leve |
| CT15 | 8 | atraso moderado |
| CT16 | 30 | atraso moderado |
| CT17 | 31 | atraso grave |

## Resultado

Os casos devem ser executados posteriormente como testes automatizados com pytest.
