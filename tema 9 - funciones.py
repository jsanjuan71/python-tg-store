
def isNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def convertToNumber(number):
    if isNumber(number):
        return int(number) or float(number)
    else:
        return None


def calculateSubtotal(cantidad, precio):

    precio = convertToNumber(precio)
    cantidad = convertToNumber(cantidad)
    #None | 0 | 0.0 | False = False
    if precio != None and cantidad != None:
        return precio * cantidad
    else:
        return None


calculateSubtotal(1, 2)
 
calculateSubtotal( cantidad = 1, precio = 2 )

subtotal = calculateSubtotal(1,2)
if subtotal:
    print(  subtotal * 2 )


#definir
#invocar
