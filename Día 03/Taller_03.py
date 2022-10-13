# **************** INSCRIPCIÓN DE PERSONAS ********************

lista_estudiantes = []

while True:
    print("""
        ********** Registro de estudiantes ********
        1.- Ingresar estudiante
        2.- Mostar estudiantes
        3.- Salir
    """)

    menu = int(input('Seleccione una opción.: '))
    if menu == 1:
        nombre = input('Ingrese un nombre.: ')
        apellido = input('Ingrese un apellido.: ')
        cedula = input('Ingrese la cédula.: ')
        estudiante = dict({'Nombre': nombre, 'Apellido': apellido, 'Cédula': cedula})
        lista_estudiantes.append(estudiante)
    elif menu == 2:
        for user in lista_estudiantes:
            for k in user.keys():
                print(user[k], end=" ")
            print("")
    elif menu == 3:
        break
    else:
        print('Seleccione una opción correcta...')