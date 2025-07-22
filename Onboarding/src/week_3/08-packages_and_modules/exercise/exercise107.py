from moeda import *
p = float(input("Digite o valor: R$"))
print(f"Aumentando 10%: {moeda(aumentar(p))}")
print(f"Diminuindo 13%: {moeda(diminuir(p))}")
print(f"A metade de {moeda(p)} é {moeda(metade(p))}")
print(f"O dobro de {moeda(p)} é {moeda(dobro(p))}")
print(f"Valor formatado: {moeda(p)}")