# ************************ INTRODUCCIÓN A PYTHON ****************************

# -- Instalación de python

        # -- Descarga de Python.:  https://www.python.org/downloads/
        # -- Descarga de visual studio code.: https://code.visualstudio.com/download

# ****************** INGRESO DE DATOS ***********************************
# input()


# *********************** VARIABLE **************************************
# a = 10

# nombre = input('Introduzca un nombre.: ')
# apellido = input('Introduzca un apellido.: ')
# edad = int(input('Ingrese su edad.: '))
# print('HOLA', nombre, apellido, ' y mi edad es.: '+ str(edad/2))

# ***************** TIPOS DE DATOS **************************************

# int -> Entero [-5, 25, 49, 7548]
# float -> Decimal [3.14, 89.4567, 8.6]
# string -> "Camilo", 'Camilo'
# char -> 'a', '1'
# bool -> True, False

# import math

# valorPi = math.pi

# print("{:.4f}".format(valorPi))

# print(4**2)

# ****************** Expresiones *********************************
# Expresones matemáticas ,/, *, **, +, -
# Expresions relacionales <, >, <=, >=, ==, != 
# Expresiones Booleanas and, or, not

# True -> 1
# False -> 0


# print(48 + 59 and 56 + 36 >= 56 * 2)

# print(45/5)
num_1 = int(input('Ingresar número 1.: '))
num_2 = int(input('Ingresar número 2.: '))
num_3 = int(input('Ingresar número 3.: '))

relacion_1 = num_2 < num_1 > num_3
relacion_2 = num_1 < num_2 > num_3
relacion_3 = num_2 < num_3 > num_1

print('El valor mayor es.:'.center(50, '*'))
print('Número 1', relacion_1)
print('Número 2', relacion_2)
print('Número 3', relacion_3)
# print(True and 45/(5 * 3) > 56 and 72)


