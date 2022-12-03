# list | lista | array | arreglo | vector 
arregloFrutas = ["manzana", "platano", "sandía", "guayaba"]

# tuple | tupla
tuplaCoordenadas = (-109.33, 98.209)

# dict | diccionario | objeto
objetoProducto = {"nombre": "Julio Sanjuan", "edad": 32, "estatura":1.71}


for i in range(1, 10):
    print(i)
print("================================")

for fruta in arregloFrutas:
    print(f"Fruta: {fruta}")
print("================================")

objetoProducto["edad"]

for key in objetoProducto:
    print(f"{key}: {objetoProducto[key]}")
print("================================")

for key, value in objetoProducto.items():
    print(f"{key}: {value}")

opcion = 0
while opcion is not 0:
    try:
        opcion = int(input("Si quiere salir teclee 0, de lo contrario cualquier cosa."))
    except ValueError:
        opcion = None
    print(f"Usted tecleó {opcion}")

print("================================\nFin")


"""
ACTIVIDAD: Actualizar el siguiente inventario de productos:
"""
inventario = [
    {"nombre": "iPhone X", "precio": 19999, "existencia": 10 },
    {"nombre": "MacBook Pro 13 M1", "precio": 32000, "existencia": 5 },
    {"nombre": "Magic Mouse 2", "precio": 2500, "existencia": 50 }
]
""" Por cada producto: 
    Solicitar al usuario el nuevo precio y aumentarle 1% de comisión
        Debes evaluar que el precio sea positivo, que no sea mayor 999,999
        * En caso de que no cumpla volver a solicitarlo
    Solicitar al usuario la cantidad de existencia
        Debes evaluar que la cantidad sea positiva y no mayor a 100
        * En caso de que no cumpla volver a solicitarlo

    Al final mostrar el nuevo inventario de la siguiente forma
    _____________________ Inventario TG Store ________________________________________________
    |       Producto        |       Precio      |       Existencia      |   Total inversión  |
    |   iPhone X            |       $19 999     |           10          |       $199 990
    |   ETC   ................
"""
def validaNumero(numero):
    try:
        return float(numero)
    except ValueError:
        return None

def solicitarNumero(min, max, titulo, criterio):
    num = None
    while num == None or num <= min or num >= max:
        try:
            num = input(f"Teclee el nuevo {titulo} [{min}-{max}] de {criterio}: ")
            num = validaNumero(num)
        except ValueError:
            num = -1
    
    return num

def textoCentrado(texto, ancho, relleno):
    return str(texto).center(ancho, relleno)


ANCHO_CELDA = 20
for producto in inventario:
    precio = solicitarNumero(0.0, 999.0, "precio", producto['nombre'] )
    producto["precio"] = precio * 1.01
    cantidad = solicitarNumero(0.0, 99.0, "cantidad", producto['nombre'])
    producto["existencia"] = cantidad

print( " Inventario TG Store ".center(80,"_") )
print( f"{'Producto'.center(20, ' ')}|{'Precio'.center(20, ' ')}|{'Existensia'.center(20, ' ')}|{'Total'.center(20, ' ')}" )
for producto in inventario:
    print( f"{textoCentrado(producto['nombre'], ANCHO_CELDA, ' ')}|{textoCentrado(producto['precio'], ANCHO_CELDA, ' ')}|{textoCentrado(producto['existencia'], ANCHO_CELDA, ' ')}|{ textoCentrado(float(producto['precio'])*float(producto['existencia']), ANCHO_CELDA, ' ')}" )





