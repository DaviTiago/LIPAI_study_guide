"""Exercise 06"""
# - Crie um programa em python que recebe como entrada o comprimento, altura e a largura(cm) de um aquário e calcule as seguintes informações.
# - O volume do aquário em litros
# - A potência do termostato necessária para manter a temperatura adequada dentro do aquário
# - A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
# - Neste exercício você deve definir a estrutura de dados que represente as entradas do usuário e também as funções que resolvam os diferentes cálculos e apresentar os resultados finais para o usuário.


def calculate_volume(length, height, width):
    aquarium['length'] = length  
    aquarium['height'] = height
    aquarium['width'] = width
    volume = (length * height * width) / 1000  
    aquarium['volume'] = volume  
    return volume


def calculate_thermostat_power(volume, desired_temp, ambient_temp):
    power = volume * 0.05 * (desired_temp - ambient_temp)
    return power


def calculate_filtration(volume):
    filtration_min = volume * 2
    filtration_max = volume * 3
    return filtration_min, filtration_max


aquarium = {
    'length': 0,
    'height': 0,
    'width': 0,
    'volume': 0,
}

length = float(input("Digite o comprimento do aquário (cm): ")) 
height = float(input("Digite a altura do aquário (cm): "))
width = float(input("Digite a largura do aquário (cm): "))
desired_temp = float(input("Digite a temperatura desejada (°C): "))
ambient_temp = float(input("Digite a temperatura ambiente (°C): "))

volume = calculate_volume(length, height, width)
thermostat_power = calculate_thermostat_power(volume, desired_temp, ambient_temp)
filtration_min, filtration_max = calculate_filtration(volume)
print(f"\nVolume do aquário: {volume:.2f} litros")
print(f"Potência do termostato necessária: {thermostat_power:.2f} W")
print(f"Quantidade de filtragem por hora: {filtration_min:.2f} a {filtration_max:.2f} litros")

