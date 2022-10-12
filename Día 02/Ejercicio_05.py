# ******************* ESTRUCTURA FOR ************************

cadena = 'Estrategia de control'
contador = 0

for x in range(len(cadena)):
    if cadena[x] == 'í':
        break
    if cadena[x].lower() == 'o':
        contador += 1
else:
    print('El FOR termino de forma correcta')
if contador == 0:
    print('No existe la letra o en la palabra, ', cadena)
else:
    print('La letra O se repite ', contador, ' veces')


# print(list(range(5, 16)))