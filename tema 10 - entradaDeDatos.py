#nombre = input("Teclee su nombre: ")
#print(f"Hola {nombre.upper()[0]} ")
#Emmet sintax
"""
ACTIVIDAD: Solicitar al usurio nombre y el precio de un producto:
    Mostrar el precio leido
    Mostrar el IVA del producto
    Mostrar el precio con IVA

    __________
    Nombre: Terminal Pin Pad Konfio
    Precio: $199
    I.V.A:  $31.84
    Precio público: $230.84

    * Utiliza funciones

"""
IVA = 0.16

def validaNumero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return None

def calculaIva(precio):
    if validaNumero(precio) != None:
        return float(precio) * IVA

    #return None
nombre = input("Teclea el nombre del producto: ")
precio = input("Ingrese precio: ")

ivaDelPrecio = calculaIva(precio)
if ivaDelPrecio != None:
    precio = float(precio)

    precioFinal = precio + ivaDelPrecio

    print(f"Nombre: {nombre}")
    print(f"Precio: ${precio}")
    print(f"I.V.A.: ${ivaDelPrecio}")
    print(f"Precio público: ${precioFinal}")
else:
    print(f"Precio: {precio} no es un número válido.")
