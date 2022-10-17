# archivo = open('Taller_01.txt', 'a')

# archivo.write("\nBienvenidos al curso de python")
# archivo.close()

# archivo.

archivo = open('Taller_01.txt', 'r')

for data in archivo.readlines():
    print(data)

archivo.close()
