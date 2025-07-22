
def aumentar(valor):
    return valor * 1.10 

def diminuir(valor):
    return valor * 0.87

def  metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2

def moeda(valor):
    valor = round(valor, 2)
    return f'R${valor:.2f}'.replace('.', ',') 
