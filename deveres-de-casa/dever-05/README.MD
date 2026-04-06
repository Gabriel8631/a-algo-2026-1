Dever 05: Recursão e Complexidade

Este repositório contém a implementação do Dever 05 da disciplina de Análise de Algoritmos.

 Descrição da Tarefa

Implementação em Python da seguinte função recursiva:
F(n) = 2F(n-1) + n^2

Com o caso base: 
F(1) = 2

 Funcionalidades

O script solicita ao usuário um valor `n` e realiza duas abordagens para fins de análise:
1. Recursiva:Implementação da função chamando a si mesma até atingir o caso base. De forma intencional, a chamada é dividida para simular a árvore de execução com complexidade de tempo $O(2^n)$.
2. Fórmula Fechada: Resolução da relação de recorrência matematicamente, utilizando a biblioteca `math` do Python para cálculo com complexidade de tempo O(1). 
   Fórmula deduzida: F(n) = 13 \cdot 2^{n-1} - n^2 - 4n - 6

  Como executar

Certifique-se de ter o Python instalado em sua máquina.
Execute o seguinte comando no terminal:

```bash
python main.py
