# Crear dos listas una con cinco nombres y otra con cinco carreras

nombres = ['Juan', 'Alex', 'Rita', 'Lia', 'Samuel']
carreras = ['geología', 'derecho', 'matemática', 'física', 'medicina']
"""
    Juan estudia geología
    Alex estudia derecho
"""

# carreras.reverse()

nombres.sort()
carreras.sort()

for cr in range(5):
    print(nombres[cr], 'estudia', carreras[cr])

print(list(range(5)))