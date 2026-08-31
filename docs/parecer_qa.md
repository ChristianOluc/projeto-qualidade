# Parecer Final de QA — BiblioTech

## Requisitos avaliados

- RF01 — Permissão para empréstimo
- RF02 — Multa por atraso
- RF03 — Classificação de atraso

## Testes realizados

Foram realizados testes de caixa preta e caixa branca utilizando pytest.

Os testes contemplaram cenários positivos, negativos e valores de fronteira, incluindo a validação do limite de empréstimos ativos.

## Defeito encontrado

Durante os testes de caixa preta foi identificado um defeito no RF01 relacionado ao limite de empréstimos ativos.

O requisito determina que um usuário somente pode realizar um novo empréstimo quando possuir menos de 3 empréstimos ativos.

O comportamento incorreto permitia o empréstimo quando o usuário possuía exatamente 3 empréstimos ativos.

O defeito foi corrigido na implementação.

## Validação após correção

Após a correção, os testes automatizados foram executados novamente utilizando pytest.

A pipeline do GitHub Actions foi executada com sucesso, passando pelas etapas:

- Build
- Quality Gate
- Delivery

## Cobertura

Foi configurada a medição de cobertura utilizando pytest-cov e cobertura de branches.

A cobertura foi utilizada para verificar se os principais caminhos e decisões do código estavam sendo exercitados pelos testes.

## Parecer da equipe

[x] Recomendamos aprovação

[ ] Não recomendamos aprovação

### Justificativa

O defeito identificado no RF01 foi corrigido e os testes automatizados foram executados com sucesso após a correção.

Os requisitos RF01, RF02 e RF03 possuem casos de teste documentados e automatizados, com rastreabilidade entre requisitos e testes.

Com base nas evidências obtidas, a versão analisada está apta para liberação.
