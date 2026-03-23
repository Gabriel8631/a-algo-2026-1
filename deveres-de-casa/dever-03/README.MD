def is_palindrome_recursive(arr):
    # Caso base 1: Um array vazio ou com apenas 1 elemento sempre é palíndromo
    if len(arr) <= 1:
        return True
    
    # Caso base 2: Se o primeiro e o último elementos forem diferentes, não é palíndromo
    if arr[0] != arr[-1]:
        return False
    
    # Passo recursivo: Chama a função novamente ignorando o primeiro e o último elementos
    return is_palindrome_recursive(arr[1:-1])

# --- Testando os exemplos do dever de casa ---

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(f"array1: {is_palindrome_recursive(array1)}") # True (É palíndromo)
print(f"array2: {is_palindrome_recursive(array2)}") # True (É palíndromo)
print(f"array3: {is_palindrome_recursive(array3)}") # True (É palíndromo)
print(f"array4: {is_palindrome_recursive(array4)}") # False (Não é palíndromo)
