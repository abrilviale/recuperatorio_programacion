def validar_datos(texto: str)-> bool:
    '''
    Valido que el texto no este vacio y que contenga solamente numeros
    '''
    if len (texto) == 0:
        return False
    for i in range (len(texto)):
        if texto[i] < "0" or texto [i] > "9":
            return False
    return True
