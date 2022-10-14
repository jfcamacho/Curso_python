# ************************************ FUNCIONES ****************************************
# Aquellas que reciben y retornan valores
# Aquellas que reciben y no retornan valores
# Aquellas que no reciben y retornan valores
# Aquellas que no reciben y no retornan valores

# **************** Aquellas que reciben y retornan valores ***************************

def conversor(*argumentos):
    print('Convirtiendo.....')
    lista = list(argumentos)
    return lista

listaTrabajada = conversor('a', 'e', 'i', 'o', 'u')

print('El resultado es.:', listaTrabajada)