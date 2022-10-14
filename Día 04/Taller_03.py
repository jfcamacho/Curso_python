import Funciones

while True:
    Funciones.menu()

    menu = int(input('Seleccione una opción.: '))
    a = int(input('Ingrese el valor de a.:'))
    b = int(input('Ingrese el valor de b.:'))

    if menu == 1:
        print(Funciones.funcionSuma(a,b))
    elif menu == 2:
        print(Funciones.funcionResta(a,b))
    elif menu == 3:
        print(Funciones.funcionMult(a,b))
    elif menu == 4:
        print(Funciones.funcionDiv(a,b))
    elif menu == 5:
        break
    else:
        print('Opción incorrecta...')