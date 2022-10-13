# **************** COLAS CON LISTAS ***********************************

from collections import deque


lista = ['Anibal', 'Raquel', 'Celeste', 'Susana', 'Ricardo', 'Daniel']

nombres = deque(lista)

print(nombres)

nombres.append('Sofia')

print(nombres)

nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()
nombres.popleft()

print(nombres)