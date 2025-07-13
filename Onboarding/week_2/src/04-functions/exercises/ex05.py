"""Exercise 05"""

# Utilizando as diretrizes de Índice de Massa Corporal(IMC) da Organização Mundial de Saúde(OMS), crie uma calculadora em python que solicita ao usuário seu peso(Kg) e sua altura(m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação atual do indivíduo('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal.

# Dados das classificações em uma estrutura mais eficiente
BMI_CLASSIFICATIONS = [
    (18.5, "Baixo peso", "Ganhar Peso"),
    (24.9, "Peso normal", "Normal"),
    (29.9, "Excesso de peso", "Perder Peso"),
    (34.9, "Obesidade de Classe 1", "Perder Peso"),
    (39.9, "Obesidade de Classe 2", "Perder Peso"),
    (float('inf'), "Obesidade de Classe 3", "Perder Peso")
]

def calculate_bmi(weight, height):
    """Calcula o IMC e retorna arredondado para 2 casas decimais"""
    return round(weight / (height ** 2), 2)

def get_bmi_info(bmi):
    """Retorna classificação e situação baseado no IMC"""
    for max_bmi, classification, situation in BMI_CLASSIFICATIONS:
        if bmi <= max_bmi:
            return classification, situation
    
def get_user_input():
    """Solicita e valida entrada do usuário"""
    while True:
        try:
            weight = float(input("Digite seu peso (Kg): "))
            height = float(input("Digite sua altura (m): "))
            
            if weight <= 0 or height <= 0:
                print("Peso e altura devem ser valores positivos. Tente novamente.")
                continue
                
            return weight, height
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

def main():
    """Função principal do programa"""
    print("=== Calculadora de IMC ===")
    
    # Obter dados do usuário
    weight, height = get_user_input()
    
    # Calcular IMC e obter informações
    bmi = calculate_bmi(weight, height)
    classification, situation = get_bmi_info(bmi)
    
    # Exibir resultados
    print(f"\n=== RESULTADOS ===")
    print(f"Seu IMC é: {bmi}")
    print(f"Classificação: {classification}")
    print(f"Situação: {situation}")

# Executar programa
if __name__ == "__main__":
    main()
