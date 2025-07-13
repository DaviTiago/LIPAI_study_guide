"""Exercise 05"""

# Utilizando as diretrizes de Índice de Massa Corporal(IMC) da Organização Mundial de Saúde(OMS), crie uma calculadora em python que solicita ao usuário seu peso(Kg) e sua altura(m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação atual do indivíduo('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal.

user = {
    'weight': 0,
    'height': 0,
    'bmi': 0,
    'classification': '',
    'situation': '' ,  
}

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def get_classify(bmi):
    if bmi < 18.5:
        return "Baixo peso"
    elif 18.5 <= bmi <= 24.9:
        return "Peso normal"
    elif 25.0 <= bmi <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= bmi <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= bmi <= 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def user_sitution(bmi):
    if bmi < 18.5:
        return "Ganhar Peso"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    else:
        return "Perder Peso"
    
while True:
    try:
        user['weight'] = float(input("Digite seu peso (Kg): "))
        user['height'] = float(input("Digite sua altura (m): "))
        if user['weight'] <= 0 or user['height'] <= 0:
            print("Peso e altura devem ser valores positivos. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
user['bmi'] = calculate_bmi(user['weight'], user['height'])
user['classification'] = get_classify(user['bmi'])
user['situation'] = user_sitution(user['bmi'])

print(f"\nSeu IMC é: {user['bmi']}")
print(f"Classificação: {user['classification']}")
print(f"Situação: {user['situation']}")
