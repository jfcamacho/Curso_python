import pandas as pd

datos = {   'nombre': ['Maria', 'Luis', 'Rebeca', 'Carlos'], 
            'edad': [23, 19, 18, 20],
            'ciclo': ['Noveno', 'Tercero', 'Primero', 'Octavo'],
            'correo': ['maria@gmail.com', 'luis@gmail.com', 'rebeca@gmail.com', 'carlos@gmail.com']
            }

tabla = pd.DataFrame(datos)

tabla2 = pd.DataFrame([['Maria', 23], ['Luis', 19], ['Rebeca', 18]], columns=['Nombre', 'Edad'])

# serie = pd.Series([....])

# serie.dropna()

print(tabla2)