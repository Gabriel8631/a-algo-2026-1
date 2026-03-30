import math
import sys

# Aumenta o limite de recursão padrão do Python (opcional, para testes um pouco maiores)
sys.setrecursionlimit(2000)

def f_recursivo(n):
    """Calcula F(n) usando recursividade O(2^n)."""
    # Caso base
    if n == 1:
        return 2
    
    # Passo recursivo: F(n) = 2*F(n-1) + n^2
    return 2 * f_recursivo(n - 1) + n**2

def f_formula_fechada(n):
    """Calcula F(n) usando a fórmula fechada O(1)."""
    # Fórmula: 13 * 2^(n-1) - n^2 - 4n - 6
    termo_exponencial = 13 * math.pow(2, n - 1)
    termo_polinomial = math.pow(n, 2) + 4 * n + 6
    
    return termo_exponencial - termo_polinomial

# --- Programa Principal ---
try:
    # Solicita o valor de n ao usuário
    n = int(input("Digite o valor de n (inteiro positivo): "))
    
    if n < 1:
        print("O valor de n deve ser maior ou igual a 1 (devido ao caso base F(1)).")
    else:
        # Só executa a recursão se n não for absurdamente grande para evitar travar o PC
        if n <= 900: 
            resultado_recursao = f_recursivo(n)
            print(f"\n-> Resultado usando Recursão F({n}): {resultado_recursao}")
        else:
            print(f"\n-> O valor de n={n} é muito grande para a recursão (causaria erro de limite de memória).")
            
        # Calcula pela fórmula fechada (funciona para qualquer N instantaneamente)
        resultado_matematico = f_formula_fechada(n)
        print(f"-> Resultado usando Fórmula Fechada (math) F({n}): {int(resultado_matematico)}")

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números inteiros.")
