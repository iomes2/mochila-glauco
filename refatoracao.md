# Plano de Refatoração

## Análise do Código Original
- Principais problemas identificados:
  - Exemplo: Código duplicado no algoritmo genético.
  - Exemplo: Função `fitness()` faz mais de uma coisa.

## O que será Refatorado
- Refatorar a função `fitness()` para separar cálculo e avaliação.
- Renomear variáveis e funções com nomes mais descritivos.
- Modularizar a criação da população inicial.

## Justificativas
- Melhorar legibilidade e manutenção do código.
- Reduzir complexidade e acoplamento.
- Permitir testes unitários mais precisos.

## Técnicas Usadas
- **Extract Function** (Martin Fowler)
- **Rename Variable**
- **Split Phase**
- Fontes: Refactoring Guru, Livro de Fowler
