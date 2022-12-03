# Lambda expression | lambda function | Funciones anónimas
import math
print("Tradicional".center(80, "_"))
def potencia2(num):
    return math.pow(num, 2)

for num in range(100):
    elevadoAlCuadrado = int(potencia2(num))
    print( f"{num} = {elevadoAlCuadrado}" )


# Aplicando lambda
print("Con lambda como variable".center(80, "_"))
potencia2Lambda = lambda num : math.pow(num, 2)

for num in range(100):
    elevadoAlCuadrado = int(potencia2Lambda(num))
    print( f"{num} = {elevadoAlCuadrado}" )


print("Con lambda como expresión".center(80, "_"))
for num in range(100):
    parONon = (lambda num: (num%2==0 and "par") or "non")(num)
    print( f"{num} = {parONon}" )

print("Con lambda como expresión pero mas de un parametro".center(80, "_"))
for num in range(100):
    parONon = (lambda num, divisor: (num%divisor==0 and "par") or "non")(num, 2)
    print( f"{num} = {parONon}" )

"""
Actividad: 
    Usando funciones lambda y comprensión de listas:
    * Crear una lista de los numeros entre 0 y 999
    * Los números nones deber ser mostrados tal cual
    * Los números pares deben ser reemplazados por una mascara
    * La mascara debe ser guiones, la cantidad de dígitos del número enmascarado
"""