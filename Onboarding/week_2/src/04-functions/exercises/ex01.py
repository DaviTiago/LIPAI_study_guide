"""Exercise 01"""

# Crie uma função que recebe três números como parâmetro(n1, n2, n3) e imprime na saída padrão a soma dos números

import random


def sum_numbers(n1, n2, n3):
    total = n1 + n2 + n3
    print(f"A soma dos números {n1}, {n2} e {n3} é: {total}")

numbers = [random.randint(1, 100) for _ in range(3)]
print(f"Números gerados: {numbers}")
n1, n2, n3 = numbers
sum_numbers(n1, n2, n3)

