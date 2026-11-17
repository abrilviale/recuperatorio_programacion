from validaciones.validaciones import validar_datos

def cargar_ventas():
    '''
    Solicita las ventas de las regiones
    Valida que los datos ingresados sean numeros mayores a 0
    '''
    ventas = [0] * 6
    for i in range (len(ventas)):
        print("Pais", i + 1)
        numero = input("Ingrese ventas: ")

        while validar_datos(numero)== False or int(numero) <= 0:
            print("Dato incorrecto")
            numero = input("Ingrese ventas")

            ventas[i]= int(numero)

            return ventas
