import pandas as pd

diccionario = {'Matemáticas': 10, 'Historia':6, 'Geografía':8, 'Programación':9}

serie = pd.Series(diccionario)

serie2 = pd.Series(data=[1, 2, 4, 5, 6, 7, 8, 1])

print(serie2[serie2 > 4])