import pandas as pd

archivo = pd.read_csv('Taller_02.csv', sep= ';')

datos = {   'nombre': ['Maria', 'Luis', 'Rebeca', 'Carlos'], 
            'edad': [23, 19, 18, 20],
            'ciclo': ['Noveno', 'Tercero', 'Primero', 'Octavo'],
            'correo': ['maria@gmail.com', 'luis@gmail.com', 'rebeca@gmail.com', 'carlos@gmail.com']
            }
# datos2 = { 'nombre': archivo['Nombre'], 'correo': archivo['Correo']}

tabla = pd.DataFrame(datos)

print(tabla)

print(tabla.iloc[1, [0,1]])

# tabla2 = pd.DataFrame(datos2)

# tabla.to_csv('Taller_04.csv', sep=';')

# print(archivo.columns)

# print(tabla2)