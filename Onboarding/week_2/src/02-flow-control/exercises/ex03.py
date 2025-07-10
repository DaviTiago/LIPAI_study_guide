"""Exercise 03"""

# O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X. Exemplos válidos: BR0001X BR1236X BR9999X
# Exemplos inválidos: br0001X BR126X BR99999X BR9999Y
# Crie um programa em python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

identifier = input("Digite o identificador do funcionário (ex: BR0001X): ").strip()

correct_len = len(identifier) == 7
prefix_BR = identifier.startswith("BR")
sulfix_X = identifier.endswith("X")
is_number = identifier[2:6].isdigit()
is_valid_number = is_number and 1 <= int(identifier[2:6]) <= 9999

if correct_len and prefix_BR and sulfix_X and is_valid_number:
    print("Identificador valido")
else:
    print("Identificador invalido")