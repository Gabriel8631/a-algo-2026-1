import time

# Função recursiva para calcular o fatorial
def fatorial(n):
    """
    Calcula o fatorial de n usando recursão.
    Caso base: fatorial de 0 ou 1 é 1.
    Caso recursivo: n * fatorial(n-1)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


# Lista de valores para teste
valores = [10, 100, 500, 1000]

# Testando o tempo de execução
for n in valores:
    inicio = time.time()  # marca o início
    
    resultado = fatorial(n)
    
    fim = time.time()  # marca o fim
    tempo_execucao = fim - inicio
    
    print(f"n = {n}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
    print("-" * 40)
