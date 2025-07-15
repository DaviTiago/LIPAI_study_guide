"""Exercise 01"""

# - Crie a função `carregar_dados_alunos` que recebe como parâmetro o nome de um arquivo que contém dados de alunos e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: prontuario, nome e email
# arquivo de dados:
# SP000001, Maria da Silva, maria@email.com
# SP000002, Pedro Gomes, pedro@email.com
# SP000003, João Santos, joao@email.com
# Formato de retorno da função python
# (
#     {
#         'prontuario': 'SP000001',
#         'nome': 'Maria da Silva',
#   		    'email': 'maria@email.com'
#     },
#     {
#         'prontuario': 'SP000002',
#         'nome': 'Pedro Gomes',
#   		    'email': 'pedro@email.com'
#     },
#     {
#         'prontuario': 'SP000003',
#         'nome': 'João Santos',
#   		    'email': 'joao@email.com'
#     },
# )


def carregar_dados_alunos(file_name):
    alunos = [] 

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')  
            parts = [p.strip() for p in parts]

            if len(parts) != 3:
                print(f"Line ignored (invalid format): {line.strip()}")
                continue

            prontuario, nome, email = parts

            student = {
                'prontuario': prontuario.strip(),
                'nome': nome.strip(),
                'email': email.strip()
            }
            alunos.append(student)  

    return tuple(alunos)  


# LIPAI_study_guide/Onboarding/src/week_3/06-files/exercises/prontuarios.txt
path = input("Digite o caminho do arquivo de prontuários: ")
prontuarios = carregar_dados_alunos(path)
for aluno in prontuarios:
    print(aluno)
