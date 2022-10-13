# ***************** DETERMINAR EL MAYOR DE TRES NÚMEROS **************************

valores = (-497, 10, -155, 45, -3203, -65, 23, 57, 6, 464)
numero = -10000000

for val in valores:
    if val > numero:
        numero = val

print('El valor mayor es.: ', numero)
