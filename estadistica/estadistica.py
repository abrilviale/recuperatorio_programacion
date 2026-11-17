def calcular_total(lista):
    '''
    Calcula el total de los elementos de la lista 
    '''
    total = 0
    for i in range (len(lista)):
        total = total + lista[i]
        return total


def calcular_porcentaje(ventas, total)-> float:

    '''
    Calcula que porcentajes representan las ventas sobre el total
    '''
    return (ventas * 100) / total


def calcular_promedio(lista):
    '''
    Calcula el promedio de los elementos de la lista
    '''
    return calcular_total(lista) / len(lista)