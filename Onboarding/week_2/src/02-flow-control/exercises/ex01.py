"""Exercise 01"""

# Solicite ao usuário 3 notas e calcule a média aritmética (sem usar sum())

grades = []
total = 0  

print("Digite três notas para calcular a média aritmética:")

while len(grades) < 3:
    grade = float(input(f"Nota {len(grades) + 1}: "))
    if 0 <= grade <= 10:
        grades.append(grade)
        total += grade  
    else:
        print("A nota deve estar entre 0 e 10. Tente novamente.")

average = total / len(grades)

print(f"A média aritmética das notas {grades} é: {average:.2f}")


