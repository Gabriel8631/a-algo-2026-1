import time
import random

# Implementação do Insertion Sort O(n²)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Tamanhos n para teste
tamanhos = [1000, 5000, 10000, 20000, 50000]

print(f"{'n':<10} | {'Insertion (s)':<15} | {'Sorted (s)':<15}")
print("-" * 45)

for n in tamanhos:
    # Cria lista aleatória
    lista_base = [random.randint(0, n) for _ in range(n)]
    
    # Medindo o Insertion Sort
    copia_ins = lista_base.copy()
    inicio = time.time()
    insertion_sort(copia_ins)
    fim = time.time()
    tempo_ins = fim - inicio
    
    # Medindo o sorted() nativo do Python (Timsort)
    copia_nat = lista_base.copy()
    inicio = time.time()
    sorted(copia_nat)
    fim = time.time()
    tempo_nat = fim - inicio
    
    print(f"{n:<10} | {tempo_ins:<15.4f} | {tempo_nat:<15.4f}")
