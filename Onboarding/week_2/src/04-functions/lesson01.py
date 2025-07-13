""" Lesson 01 - Introduction to Functions """

# Functions are blocks of code that perform specific tasks.
# Funções são blocos de código que executam tarefas específicas.

# Benefits:
# - Avoid repetition                / Evitam repetição
# - Make the code modular          / Tornam o código modular
# - Improve readability            / Melhoram a legibilidade
# - Make maintenance easier        / Facilitam a manutenção

# ------------------------------------------
# 1. Built-in Functions / Funções Embutidas
# ------------------------------------------

# These are functions that are already available in Python
# Funções já disponíveis na linguagem

print("Hello", 123, True)  # Display on screen / Exibe na tela

names = ['Alice', 'Bob', 'Carlos']
# Returns the size of the list / Retorna o tamanho da lista
length = len(names)
print("Names:", names, "Length:", length)

# ------------------------------------------
# 2. User-Defined Functions / Funções Definidas pelo Usuário
# ------------------------------------------

# You can define your own functions to solve parts of a problem.
# Podemos definir nossas próprias funções para resolver partes de um problema.

# Example 1 - No parameters and no return
# Exemplo 1 - Sem parâmetros e sem retorno


def greet():
    print("Hello! Welcome to our system.")


greet()
greet()

# Example 2 - With parameter, no return
# Exemplo 2 - Com parâmetro, sem retorno


def greet_user(name):
    print(f"Hello, {name}! Nice to see you.")


greet_user("João")
user = "Marina"
greet_user(user)

# Example 3 - With parameters and return value
# Exemplo 3 - Com parâmetros e valor de retorno


def calculate_average(n1, n2, n3):
    avg = (n1 + n2 + n3) / 3
    return avg


# Calling with literal values / Chamando com valores literais
average = calculate_average(7.5, 8.0, 9.0)
print("Average:", average)

# Calling with variables / Chamando com variáveis
a = 6.0
b = 5.0
c = 8.0
avg2 = calculate_average(a, b, c)
print("Average 2:", avg2)

# Example 4 - Function with logic / Com lógica condicional


def check_status(average):
    if average >= 6.0:
        return "Approved / Aprovado"
    elif average >= 4.0:
        return "Recovery / Recuperação"
    else:
        return "Failed / Reprovado"


status = check_status(avg2)
print("Status:", status)

# ------------------------------------------
# Summary / Resumo
# ------------------------------------------

# Functions are reusable blocks that help organize and simplify code.
# Funções são blocos reutilizáveis que ajudam a organizar e simplificar o código.

# In the next lessons we’ll see:
# Nas próximas aulas veremos:
# - Default parameter values        / Valores padrão
# - Variable number of arguments    / Número variável de argumentos
# - Scope of variables              / Escopo de variáveis
# - Nested functions                / Funções dentro de funções
