# ******************* continue, break, pass;*************************
# valor = 0

# while valor <= 5:
#     valor += 1
#     if valor % 2 != 0:
#         print('El valor es impar.: ', valor)
#         continue
#     print('El valor es.: ', valor)

# while True:
#     valor += 0.01
#     print('El valor es.: ', valor)
#     if valor >= 10:
#         break

# El programa me va a solicitar las notas de los estudiantes y solo se
# terminará si ingreso el valor de 20

nota = 0

while nota <= 10:
    salir = input('Desea finalizar el programa y/n.: ')
    if salir.lower() == 'y':
        break

    nota = float(input('Ingrese la nota.: '))
    if 10 >= nota >= 7:
        print('Aprobado')
    elif 0 < nota < 7:
        print('Reprobado')
    else: 
        print('Ingrese un valor correcto.: ')
else:
    print('Findel programa en el Else...')
