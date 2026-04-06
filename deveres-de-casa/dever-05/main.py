import math
import sys

# Aumentando o limite de recursão por segurança, caso teste números um pouco maiores
sys.setrecursionlimit(2000)

def f_recursivo(n):
    """
    Calcula F(n) recursivamente.
    O enunciado diz que a complexidade de tempo é O(2^n). 
    Para demonstrar isso na prática (formando uma árvore binária de chamadas),
    chamamos a função duas vezes em vez de multiplicar por 2.
    """
    # Caso base
    if n == 1:
        return 2
    
    # Chamada recursiva que gera O(2^n): F(n-1) + F(n-1) + n^2
    # (Se usássemos 2 * f_recursivo(n-1), a complexidade de tempo seria O(n))
    return f_recursivo(n - 1) + f_recursivo(n - 1) + (n ** 2)

def f_formula_fechada(n):
    """
    Calcula F(n) usando a fórmula matemática fechada.
    F(n) = 13 * 2^(n-1) - n^2 - 4n - 6
    """
    # Utilizando math.pow conforme a dica do dever
    termo_exponencial = 13 * math.pow(2, n - 1)
    resultado = termo_exponencial - math.pow(n, 2) - (4 * n) - 6
    
    return int(resultado)

def main():
    print("="*40)
    print("Dever 05 - Análise de Algoritmos")
    print("F(n) = 2F(n-1) + n^2")
    print("="*40)
    
    try:
        n_str = input("\nDigite um valor inteiro para n (ex: 1, 5, 10): ")
        n = int(n_str)
        
        if n < 1:
            print("Por favor, insira um valor onde n >= 1 (o caso base é F(1)=2).")
            return

        print(f"\nCalculando F({n})...")
        
        # 1. Cálculo por Fórmula Fechada (O(1))
        res_fechado = f_formula_fechada(n)
        print(f"Resultado (Fórmula Fechada): {res_fechado}")
        
        # 2. Cálculo por Recursão (O(2^n))
        # Adicionamos um aviso porque O(2^n) trava o PC rápido se 'n' for alto
        if n > 25:
            print("\n[Aviso] O valor de 'n' é muito grande para a recursão O(2^n).")
            print("O cálculo recursivo pode demorar muito tempo para finalizar!")
            confirmar = input("Deseja rodar a recursão mesmo assim? (s/n): ")
            if confirmar.lower() != 's':
                print("Cálculo recursivo abortado pelo usuário.")
                return

        res_recursivo = f_recursivo(n)
        print(f"Resultado (Recursão):        {res_recursivo}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
