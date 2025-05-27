# Processo da Equipe - Refatoração do Problema da Mochila

## 🧠 Organização da Equipe

A equipe recebeu o código de outra equipe e iniciou a análise funcional e estrutural. Como o tempo era limitado, optamos por realizar a refatoração e testes **localmente**, sem o uso de forks ou branches.

## 🔄 Como Garantimos a Integridade do Código Original

- O código original foi colocado na pasta `original/` e **não foi alterado**.
- A refatoração foi feita em um novo arquivo na pasta `refatorado/`.
- Todas as melhorias foram feitas com base no comportamento original observado.

## 🧪 Abordagem de Testes

- Criamos um arquivo `test_genetic_knapsack.py` usando `pytest`.
- Os testes cobrem:
  - Inicialização e formato da população.
  - Cálculo de fitness com e sem exceder a capacidade.
  - Execução do algoritmo (`run`) e validação da estrutura do resultado.
- Rodamos todos os testes e capturamos os resultados como evidência da manutenção do comportamento.

## 🛠 Ferramentas Utilizadas

- Python 3.10+
- `pytest` para testes automatizados
- `pylint` e `flake8` para análise de qualidade
- ChatGPT para apoio na organização e refatoração
- Editor de código: VS Code

## 👥 Contribuições da Equipe

- Membro 1: Refatoração de funções principais
- Membro 2: Escrita e execução de testes
- Membro 3: Documentação (`.md` e slides)



