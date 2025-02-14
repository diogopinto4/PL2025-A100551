import sys

def somador_on_off(texto):
    estado = False
    soma = 0
    i = 0

    while i < len(texto):
        if texto[i].isdigit():
            valor = 0
            while i < len(texto) and texto[i].isdigit():
                valor = valor * 10 + int(texto[i])
                i += 1
            if estado:
                soma += valor
        elif texto[i:i+2].lower() == 'on':
            estado = True
            i += 2
        elif texto[i:i+3].lower() == 'off':
            estado = False
            i += 3
        elif texto[i] == '=':
            print(soma)
            i += 1
        else:
            i += 1


for linha in sys.stdin:
    somador_on_off(linha)
