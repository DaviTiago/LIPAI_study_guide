"""Exercise 01"""

# ex01.py solicite ao usuário 3 números, armazene esses elementos em uma lista e apresente no final o menor e maior elemento

numbers = []

print('Digite 3 números')
while len(numbers) < 3:
    entrada = input(f'Number {len(numbers) + 1}: ')
    
    if entrada.replace('.', '').replace('-', '').isdigit():
        number = float(entrada)
        numbers.append(number)
    else:
        print("Por favor, digite um número válido.")

minor = min(numbers)
maior = max(numbers)

print(numbers)
print(f"Menor: {minor}")
print(f"Maior: {maior}")


