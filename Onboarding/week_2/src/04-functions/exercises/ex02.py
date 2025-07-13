"""Exercise 02"""

# Crie uma função que recebe três números como parâmetro(n1, n2, n3) e retorna a soma dos números

import random

def sum_numbers(n1, n2, n3):
    total = n1+n2+n3
    return total


numbers = [random.randint(1, 100) for _ in range(3)]
print(f"Números gerados: {numbers}")
n1, n2, n3 = numbers
print(f"A soma dos números {n1}, {n2} e {n3} é: {sum_numbers(n1, n2, n3)}")

