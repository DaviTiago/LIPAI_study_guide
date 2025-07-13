"""Exercise 04"""

# Implemente o `ex03.py` mas ao final do programa deve ser apresentado ao usuário todos os problemas que o identificador informado possui(implementar como list de erros):
#     - Ex: identificador informado: B9999999X
#     - erros
#     - O identificar não inicia com a sequencias ‘BR’
#     - O identificador não apresenta números inteiros entre 0001 e 9999

while True:
    identifier = input("Digite o identificador do funcionário (ex: BR0001X): ").strip()

    correct_len = len(identifier) == 7
    prefix_BR = identifier.startswith("BR")
    sulfix_X = identifier.endswith("X")
    is_number = identifier[2:6].isdigit()
    
    if is_number:
        is_valid_number = 1 <= int(identifier[2:6]) <= 9999
    else:
        is_valid_number = False
     
    erros = []

    
    if not correct_len:
        erros.append("Seu código não possui 7 dígitos")

    if not prefix_BR:
        erros.append("Seu prefixo é diferente de BR")

    if not sulfix_X:
        erros.append("Seu sufixo é diferente de X")

    if not is_number:
        erros.append("Os caracteres 3-6 não são números")
    elif not is_valid_number:
        erros.append("O número não está entre 0001 e 9999")

   
    if len(erros) == 0:
        print("Seu código é válido!")
        break  
    else:
        print("Seu código é inválido pois:")
        for erro in erros:
            print("- ", erro)
        print()  