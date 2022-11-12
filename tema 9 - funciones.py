
def isNumber(number):
    try:
        int(number) or float(number)
        return True
    except ValueError:
        return False


def convertToNumber(number):
    if isNumber(number):
        return int(number) or float(number)
    else:
        return None


def calculateSubtotal(precio, cantidad):
    precio = convertToNumber(precio)
    cantidad = convertToNumber(cantidad)
    if precio and cantidad:
        return precio * cantidad
    else:
        return None
