# ************************************ FUNCIONES ****************************************
# Aquellas que reciben y retornan valores
# Aquellas que reciben y no retornan valores
# Aquellas que no reciben y retornan valores
# Aquellas que no reciben y no retornan valores

# ************* Aquellas que no reciben y retornan valores ***************************

def mostrarMenu():
    print("""
    ********** MENU DE HERRAMIENTAS DE SOFTWARE *************
    1.- Microsoft
    2.- Poware point
    3.- AutoCad
    4.- Notepad
    5.- Salir
    """)

    data = int(input('Seleccione una opción.: '))

    return [1, 2, 3, 4, 5]

menu = mostrarMenu()

print('La opción seleccionada es.: ', menu)