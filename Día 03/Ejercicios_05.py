# *************************** DICCIONARIOS ************************************

usuario1 = dict({'Nombre': 'Raquel', 'Edad': 34, 'Cédula': '1100000000'})
usuario2 = dict({'Nombre': 'Juan', 'Edad': 43, 'Cédula': '1140000000'})
usuario3 = dict({'Nombre': 'Elena', 'Edad': 12, 'Cédula': '1100600000'})
usuario4 = dict({'Nombre': 'Samanta', 'Edad': 19, 'Cédula': '1100050000'})
usuario5 = dict({'Nombre': 'Marco', 'Edad': 20, 'Cédula': '1100400000'})

"""
    Raquel de 34 años con cédula 1100000000
    Juan de 43 años con cédula 11400000000
"""

lista_usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5]

print(usuario1.values())

for user in lista_usuarios:
    for k in user.keys():
        print(user[k], end=" ")
    print("")

