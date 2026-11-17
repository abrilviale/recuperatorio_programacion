from cargar.cargar_ventas import cargar_ventas
from mostrar.mostrar_ventas import mostrar_ventas, mostrar_porcentaje


ventas=[]
cargado = False
salir = False

while salir == False:

    print("")
    print("1. Cargar ventas")
    print("2. Mostrar ventas ")
    print("3. Regiones con menos del 5%")
    print("4. Regiones con menos del 25%")
    print("5. Regiones con mas de 500 ventas")
    print("6. Regiones con mas de 3000 ventas")
    print("7. Regiones por encima del promedio")
    print("8. Regiones mas compradoras")


    print("0. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        ventas = cargar_ventas()
        cargado = True
    elif opcion == "0":
        salir = True 
        print("Salida exitosa")
    elif cargado == False:
        print("Primero debe cargar las ventas (opcion 1)")
    elif opcion == "2":
        mostrar_ventas (ventas)
    elif opcion == "3":
        mostrar_porcentaje(ventas, 5)
    elif opcion == "4":
        mostrar_porcentaje(ventas, 25)

