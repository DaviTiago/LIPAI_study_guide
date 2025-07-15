"""Exercise 02"""

# Crie a função carregar_dados_projetos que recebe como parâmetro o nome de um arquivo que contém dados de projetos e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: codigo(número inteiro que representa o código do projeto), titulo e responsável(nome do professor responsável pelo projeto). Não utilizar bibliotecas ou funções prontas para leitura do arquivo.

def carregar_dados_projetos(file_name):
    projetos = [] 

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')  
            parts = [p.strip() for p in parts]

            if len(parts) != 3:
                print(f"Line ignored (invalid format): {line.strip()}")
                continue

            codigo, titulo, responsavel = parts
            try:
                codigo = int(codigo.strip())
            except ValueError:
                print(f"Invalid code format: {codigo.strip()}")
                continue

            projeto = {
                'codigo': codigo,
                'titulo': titulo.strip(),
                'responsavel': responsavel.strip()
            }
            projetos.append(projeto)  

    return tuple(projetos)

# LIPAI_study_guide/Onboarding/src/week_3/06-files/exercises/projeto.txt
path = input("Digite o caminho do arquivo de projetos: ")
projetos = carregar_dados_projetos(path)
for projeto in projetos:
    print(projeto)

    
