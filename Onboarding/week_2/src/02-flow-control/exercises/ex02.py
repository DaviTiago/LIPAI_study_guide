"""Exercise 02"""

# Solicita as notas em formato "n1, n2, ..., nm" e calcula a média e situação do aluno

grades_input = input(
    "Digite as notas separadas por vírgula, ex: n1, n2, n3, ..., nm: ")
grades_list = grades_input.split(",")

valid_grades = []
total = 0.0

for grade in grades_list:
    grade = grade.strip()
    if grade.replace('.', '', 1).isdigit():
        numeric_grade = float(grade)
        valid_grades.append(numeric_grade)
        total += numeric_grade

average = total / len(valid_grades) if valid_grades else 0

if average >= 6.0:
    status = "Aprovado"
elif 4.0 <= average < 6.0:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f"A média aritmética das notas é: {average:.2f} - Status: {status}")
