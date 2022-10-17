from turtle import color
import pandas as pd
import matplotlib.pyplot as plt 

archivo = pd.read_csv('Taller_02.csv', sep=';')

nombres = archivo['Nombre']
edades = archivo['Edad']

edades2 = []

for x in range(len(nombres)):
    edades2.append(edades.mean())

plt.bar(nombres, edades, color='tab:green')
plt.plot(nombres, edades2, color='tab:blue')

plt.title('ESTUDIANTES DE ELECTRICIDAD')

plt.ylabel('Edades')

plt.xlabel('Nombres')

plt.show()