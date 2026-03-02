import time
import random

# 1. FUNÇÃO DE ORDENAÇÃO MANUAL (O que pode cair na prova)
def ordenar_por_insercao(lista):
    # Percorremos a lista a partir do segundo elemento (índice 1)
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        posicao = i - 1
        
        # "Empurra" os elementos maiores para a direita para abrir espaço
        while posicao >= 0 and lista[posicao] > valor_atual:
            lista[posicao + 1] = lista[posicao]
            posicao -= 1
        
        # Insere o valor na posição correta
        lista[posicao + 1] = valor_atual

# 2. CONFIGURAÇÃO DOS TESTES
tamanhos_n = [1000, 5000, 10000, 20000, 50000]

print("====================================================")
print("      DEVER DE CASA - A BARREIRA DO n²")
print("====================================================")

# 3. EXECUÇÃO DOS TESTES
for n in tamanhos_n:
    # Cria uma lista com 'n' números aleatórios
    lista_original = [random.randint(0, n) for _ in range(n)]
    
    # Teste 1: Insertion Sort (O método manual e mais lento)
    copia_manual = lista_original.copy()
    inicio = time.time()
    ordenar_por_insercao(copia_manual)
    tempo_manual = time.time() - inicio
    
    # Teste 2: sorted() do Python (O método nativo e mais rápido)
    copia_nativa = lista_original.copy()
    inicio = time.time()
    sorted(copia_nativa)
    tempo_nativo = time.time() - inicio
    
    # Exibe os resultados de forma organizada
    print(f"\nResultados para n = {n}:")
    print(f" > Insertion Sort (Manual): {tempo_manual:.4f} segundos")
    print(f" > sorted() do Python:     {tempo_nativo:.4f} segundos")
    print("-" * 40)
