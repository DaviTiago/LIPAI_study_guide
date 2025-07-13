"""Exercise 03"""

# - Solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
# - Exemplo: entrada 3 saída ‘Março’.
# - **Implementar com Dicionário**

months ={
    '1' : 'Janeiro',
    '2' : 'Fevereiro',
    '3' : 'Março',
    '4' : 'Abril',
    '5' : 'Maio',
    '6' : 'Junho',
    '7' : 'Julho',
    '8' : 'Agosto',
    '9' : 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}

while True:
    n_month = input('Digite o número do mês (1-12): ')
    if n_month in months:
        print(f'O mês é: {months[n_month]}')
        break
    else:
        print('Digite um número válido entre 1 a 12')