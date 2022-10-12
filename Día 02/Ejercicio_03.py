# ****************** ESTRUCTURAS REPETITIVAS ***************
# *************************** WHILE ************************

valor = 5

while valor <= 15:
    if valor % 2 == 0:
        if valor % 4 != 0:
            print(valor, 'El valor es par.: ')
        else:
            print(valor, 'El valor es par y es múltiplo de 4')
    else:
        print(valor, 'El valor es impar.: ')
    valor += 1

while valor <= 15:
    if valor % 2 == 0 and valor % 4 == 0:
        print(valor, 'El valor es par y es múltiplo de 4')
    elif valor % 2 == 0:
        print(valor, 'El valor es par.: ')
    else:
        print(valor, 'El valor es impar.: ')
    valor += 1
    # 5 El valor es impar
    # 6 El valor es par
    # 7 El valor es impar
    # 8 El valor es par y es múltiplo de 4
    # .
    # .
    # .