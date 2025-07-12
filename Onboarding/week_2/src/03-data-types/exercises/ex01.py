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

min_number = numbers[0]
max_number = numbers[0]

for num in numbers:
    if num < min_number:
        min_number = num
    if num > max_number:
        max_number = num
#podemos usar min() e max() para simplificar
# min_number = min(numbers)
# max_number = max(numbers)

print(numbers)
print(f"Menor: {min_number}")
print(f"Maior: {max_number}")


