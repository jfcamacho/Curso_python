# ************************************ FUNCIONES ****************************************
# Aquellas que reciben y retornan valores
# Aquellas que reciben y no retornan valores
# Aquellas que no reciben y retornan valores
# Aquellas que no reciben y no retornan valores

# **************** Aquellas que reciben y no retornan valores ***************************

# Posición -> Posicionales
# Nombre -> Nombrados
# Indeterminado -> (Tuplas, Diccionarios)

def funcionA(a, b = 3, c = 2, *argumento):
    print('El valor de a es.:', a)
    print('El valor de b es.:', b)
    print('El valor de c es.:', c)
    # tupla = list(argumento)
    print('El argumento indeterminado es.: ', argumento)

funcionA(23, 45, 15, 49, 46, 53, 75, 48, 15)

def funcionB(a, b = 3, c = 2,*tupla,  **argumento):
    print('El valor de a es.:', a)
    print('El valor de b es.:', b)
    print('El valor de c es.:', c)
    # tupla = list(argumento)
    print('El argumento indeterminado tupla es.: ', tupla)
    print('El argumento indeterminado diccionario es.: ', argumento)

funcionB(23, 45, 15, 49, 46, 53, h=75, i=48, f=15)