"""Exercise 04"""

#  Crie uma função que recebe vários argumentos numéricos através do * args retorna a soma dos números
def sum_arguments(*args):
    return sum(args)

print(f"Números fornecidos: {1, 2, 3, 4, 5}")
print(f"A soma dos números é: {sum_arguments(1, 2, 3, 4, 5)}")