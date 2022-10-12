# **************************** CONDICIONES MÚLTIPLES ***************************
nota = float(input('ingrese la nota.: '))

if nota >= 7:
    print('Aprobado')
elif nota < 2.5 and nota > 0:
    print('Reprobado')
elif nota == 0:
    print('Retirado')
else:
    print('Supletorio')