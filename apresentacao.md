# Tópicos para a Apresentação: Refatoração do Problema da Mochila

---

## 1. Introdução

* **Boas-vindas e Contexto:**
    * Breve apresentação da equipe.
    * Relembrar o objetivo da atividade: **refatorar o código do Problema da Mochila** recebido de outra equipe.
    * Por que a refatoração é importante (manutenibilidade, legibilidade, escalabilidade).
* **O Problema da Mochila:**
    * Rápida descrição do problema para nivelar o conhecimento da turma.
    * Mencionar que o código recebido utilizava algoritmos bio-inspirados.

---

## 2. Análise do Código Original

* **Visão Geral do Código Recebido:**
    * De quem recebemos o código? (Sem focar em críticas, mas no contexto).
    * Qual era a estrutura inicial do código?
* **Pontos de Melhoria Identificados:**
    * **Código Duplicado:** Onde encontramos repetições e como isso impactava a manutenção.
    * **Falta de Coesão:** Partes do código que faziam muitas coisas ou não tinham responsabilidades claras.
    * **Acoplamento Excessivo:** Módulos ou classes que dependiam muito uns dos outros, dificultando mudanças.
    * **Falta de Testes:** A ausência de testes como um desafio para garantir a não regressão.
    * **Nomeação Inadequada:** Variáveis, funções ou classes com nomes pouco descritivos.
    * **Problemas de Estrutura/Lógica:** Seções do código que poderiam ser mais claras ou eficientes.
    * *Opcional: Resultados da análise de qualidade pré-refatoração (ex: SonarQube, flake8, pylint - mostrar métricas se tiver).*

---

## 3. Planejamento da Refatoração

* **Nosso Processo de Trabalho:**
    * Como garantimos que o código original não seria afetado (ex: **Fork do repositório**, **branch específica** `feature/refatoracao`).
    * A importância do arquivo **`processo.md`** para documentar isso.
* **Definição das Refatorações Prioritárias:**
    * O que decidimos refatorar primeiro e por quê (maior impacto, menor risco).
    * Apresentar os principais pontos do arquivo **`refatoracao.md`**:
        * **O que será refatorado:** (Ex: Extrair métodos, renomear variáveis, criar classes).
        * **Porquê será refatorado:** (Ex: Melhorar legibilidade, reduzir complexidade, aumentar coesão).
        * **Qual técnica será utilizada:** (Citar técnicas baseadas em Martin Fowler, Refactoring Guru, Refactoring Catalog – ex: *Extract Method*, *Rename Variable*, *Introduce Explaining Variable*).

---

## 4. Criação de Testes

* **A Importância dos Testes antes da Refatoração:**
    * Como os testes nos deram **confiança** para alterar o código.
    * Garantia de que o **comportamento original** seria mantido.
* **Framework Utilizado:**
    * Mencionar o **`pytest`** (ou outro framework) e por que foi escolhido.
* **Exemplos de Testes Criados:**
    * Mostrar um ou dois exemplos simples de testes que vocês escreveram.

---

## 5. A Refatoração na Prática

* **Técnicas Aplicadas e Resultados:**
    * **Extração de Métodos/Funções:** Mostrar um exemplo de um método grande que foi dividido em menores.
    * **Renomeação:** Exemplos de variáveis/funções com nomes melhores.
    * **Introdução de Classes/Módulos:** Se aplicável, como a criação de novas estruturas melhorou a organização.
    * **Simplificação de Lógica:** Como trechos complexos foram simplificados.
    * *Opcional: Comparar trechos de código "antes" e "depois" para ilustrar as melhorias visivelmente.*
* **Ferramentas de Análise de Qualidade:**
    * Como **`SonarQube`**, **`flake8`**, **`pylint`** foram usados durante o processo.
    * **Resultados pós-refatoração:** Mostrar as **métricas de qualidade** (se possível, um comparativo antes/depois para demonstrar a melhoria).
* **Uso de Inteligência Artificial (IA) como Apoio:**
    * Como o **`ChatGPT`** ou **`Copilot`** foram utilizados:
        * Sugestões de refatoração.
        * Entendimento de trechos de código.
        * Ajuda na escrita de testes.
        * Geração de documentação.

---

## 6. Desafios e Aprendizados

* **Desafios Encontrados:**
    * Dificuldade em entender a lógica original de partes do código.
    * Garantir a cobertura de testes em áreas complexas.
    * Gerenciamento de tempo e comunicação na equipe.
* **Principais Aprendizados:**
    * A importância da **comunicação** e **colaboração em equipe**.
    * Como a refatoração é um processo contínuo e incremental.
    * A confiança que os testes trazem para alterações de código.
    * O valor de ferramentas de qualidade e IA no desenvolvimento.

---

## 7. Conclusão

* **Sumário das Melhorias:**
    * Recapitular os principais ganhos: código mais limpo, mais testável, mais fácil de manter e entender.
* **Visão Futura:**
    * O que ainda poderia ser melhorado (se houver).
* **Perguntas:**
    * Abrir para perguntas da turma.

1 - Extração de Métodos

Antes, funções longas faziam várias tarefas juntas (ex: avaliação, seleção, mutação e cruzamento misturados).

Agora, cada etapa do algoritmo genético está em um método específico, como initialize_population(), fitness(), selection(), crossover(), mutation(), e elitism(). Isso facilita o entendimento e a manutenção.

2 - Nomeação mais clara

Variáveis como fit, val e wt passaram a ser mais bem documentadas nos retornos e comentários, e métodos têm nomes que descrevem exatamente a função, melhorando a legibilidade.

3 - Redução de Código Duplicado

Antes, cálculos da função fitness poderiam estar repetidos. Agora, o método fitness() centraliza essa lógica, usada por toda a classe.

4- Modularização e Coesão

Cada método tem uma responsabilidade clara, reduzindo acoplamento. Por exemplo, evolve_population() apenas orquestra as operações, sem misturar detalhes internos.

5 - Uso de Bibliotecas Eficientes

O código utiliza numpy para operações vetoriais, aumentando a eficiência no cálculo dos pesos e valores da população.

6 - Testabilidade Melhorada

Com métodos pequenos e claros, fica mais fácil escrever testes unitários para cada parte, garantindo que alterações futuras não quebrem o código.

7 - Documentação e Comentários

A classe tem docstrings explicativas, ajudando qualquer desenvolvedor a entender o propósito das funções.

8 - Controle da População com Elitismo

O método elitism() garante que os melhores indivíduos sejam preservados entre gerações, melhorando a performance do algoritmo.

