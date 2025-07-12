"""Exercise 02"""

# - Solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
# - Exemplo: entrada 3 saída ‘Março’.
# - **Implementar com Tupla**

months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

while True:
    try:
        n_month = int(input('Digite o número do mês (1-12):'))
        if 1 <= n_month <= 12:
            print(f'O mês é: {months[n_month-1]}')
            break
        else:
            print('Digite um número válido entre 1 a 12')
    except ValueError:
        print('Entrada inválida. Digite um número inteiro')


        

