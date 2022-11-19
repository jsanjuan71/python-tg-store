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

for key in objetoProducto:
    print(f"{key}: {objetoProducto[key]}")
print("================================")

for key, value in objetoProducto.items():
    print(f"{key}: {value}")

opcion = None
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