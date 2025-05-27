# Refatoração - Problema da Mochila com Algoritmo Genético

## 🔍 Análise do Código Original

O código original resolvia o problema da mochila 0/1 com um algoritmo genético, mas apresentava os seguintes problemas:

- Mistura de responsabilidade entre cálculo e controle dentro de métodos como `run`.
- Falta de modularidade para testes unitários.
- Ausência de documentação clara para algumas funções.
- Não havia testes automatizados.
- Estrutura do código dificultava análise de partes individuais como seleção, crossover ou mutação.

## ✅ Refatorações Realizadas

- Separação clara das responsabilidades em métodos pequenos e bem nomeados.
- Inclusão de docstring na classe.
- Remoção de lógica duplicada e centralização do cálculo de fitness.
- Melhoria na coesão e acoplamento: cada método tem uma única responsabilidade.
- Preparo do código para testes unitários.
- Padronização de nomes e clareza de parâmetros.
- Inclusão de um método `plot_progress` para visualização do progresso evolutivo.

## 🛠 Técnicas Aplicadas

Baseadas no livro de Martin Fowler e nos sites Refactoring Guru e Refactoring Catalog:

- **Extract Method**: Extração de lógicas específicas (como elitismo, fitness, crossover).
- **Rename Method/Variable**: Para tornar o código mais legível.
- **Split Phase**: Separação de lógica de evolução (`evolve_population`) da lógica de controle geral (`run`).
- **Encapsulate Collection**: Uso de métodos auxiliares para acessar/modificar população.
- **Introduce Assertion**: Validação de entrada no `__init__`.

## 🧪 Testes Automatizados

- Utilização do `pytest` para validar comportamento individual de métodos:
  - Geração de população.
  - Cálculo de fitness com e sem ultrapassar a capacidade.
  - Execução do algoritmo e retorno das chaves esperadas.
- Todos os testes passaram com sucesso e garantem que a refatoração não alterou o comportamento esperado.

## 🔧 Ferramentas Utilizadas

- `pytest` para criação e execução de testes.
- `pylint` e `flake8` para análise de estilo e qualidade.
- Editor: VS Code.
- IA: ChatGPT para apoio técnico e organização do projeto.

