# ************** LISTAS, TUPLAS, DICCIONARIOS *****************************
# ----- TUPLAS ------------------------------------------------------------

tupla = ('Juan', 'Miguel', 'Ana', 2, 4, 5, 6, 7, 2, 8, 2)

numero = tupla[3]

print(numero*4)

longitudTupla = len(tupla)

print(tupla.count(2))

print('La longitud de la tupla es.: ', longitudTupla)

for tp in range(len(tupla)):
    print('En la posición ', tp, 'está', tupla[tp])