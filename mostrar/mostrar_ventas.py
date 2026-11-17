
from estadistica.estadistica import calcular_total, calcular_porcentaje 


def mostrar_ventas(ventas):
    '''
    muestra las ventas de cada pais y el porcentaje que representa 
    cada uno sobre el total
    
    '''
    total = calcular_total (ventas)
    compradoras = 0

    for i in range (len(ventas)):
        porcentaje = calcular_porcentaje (ventas[i], total)
        print("Region", i+1, ventas[i], porcentaje, "%")
        if ventas[i] > 0:
            compradoras = compradoras + 1

    print("Regiones compradoras ", compradoras)
    print("Total de prodcutos vendidos", total)


def mostrar_porcentaje(ventas, limite):
    '''
    busca los paises con porcentajes de ventas sea menor o igual al limite dado
    '''

    total= calcular_total(ventas)
    acumulado = 0
    encontrados = 0

    for i in range (len(ventas)):
        porcentaje = calcular_porcentaje(ventas[i], total)
        if porcentaje < limite:
            print("Region", i + 1, ventas[i], porcentaje, "%")
            encontrados = encontrados + 1

    if encontrados == 0:
        print("")
    else:
        print("Porcentaje acumulado", acumulado, "%")
