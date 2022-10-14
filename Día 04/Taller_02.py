from datetime import datetime

fecha = datetime.now()

def calcularEdad(anio, mes, dia):
    year = fecha.year - anio
    if mes > fecha.month:
        year -= 1
    elif mes == fecha.month:
        if dia > fecha.day:
            year -= 1

    return year