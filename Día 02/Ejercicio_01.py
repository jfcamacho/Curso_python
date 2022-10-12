# ****************** ESTRUCTURAS DE PROGRAMACIÓN CON PYTHON **********************
# ************************* ESTRUCTURAS CONDICIONALES ****************************

# Identación es necesaria para subcontener una línea de código

# x = int(input('Ingrese el valor de x.: '))
# y = int(input('Ingrese el valor de y.: '))

# if x > y and  10 < x < 20 and x % 4 != 0:
#     print('El valor de x es correcto')
#     # if 10 < x < 20:
#     #     print('El valor de x está entre 10 y 20')
# else:
#     print('El valor de x es incorrecto')

# print('Fin del código')

# Un estudiante desea saber si esta aprobado para lo cual se debe validar que tenga una nota superior o igual 
# a 7 y que cumpla con el 80 por ciento o más de asistencias

nota = float(input('Ingrese la nota.: '))
asistencia = float(input('Ingrese la asistencia.: 8'))

if nota >= 7 and asistencia >= 80:
    print('El estudiante ha aprobado')
else:
    print('El estudiante ha reprobado')