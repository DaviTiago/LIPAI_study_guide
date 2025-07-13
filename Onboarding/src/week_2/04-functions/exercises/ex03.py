"""Exercise 03"""

# Crie uma função que recebe uma tupla de números como parâmetro(numeros) e retorna a soma dos números

def sum_numbers(numbers):
    total = sum(numbers)
    return total

numbers = (1, 2, 3)
print(f"Números: {numbers}")
print(f"A soma dos números {numbers} é: {sum_numbers(numbers)}")
