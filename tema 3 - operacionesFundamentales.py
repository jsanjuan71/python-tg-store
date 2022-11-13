PI = 3.141592
IVA = 16
numeroCinco = 5
#suma
print("_____ suma _____")
suma = 5 + 10
print( suma )

sumaConFloat = 5 + 10.3
print( sumaConFloat )

sumaConVariable = 10.3 + numeroCinco
print( sumaConVariable )

# resta
print("_____ resta _____")
resta = 343 - 23
print( resta )

restaConfloat = 34 - 10.5
print( restaConfloat )

restaConVariable = 100 - numeroCinco
print( restaConVariable )

# multiplicación
print("_____ multiplicación _____")
multi = 17 * 10
print( multi )

multiConNegativo = 10 * -1
print( multiConNegativo )

multiConVariable = numeroCinco * numeroCinco
print( multiConVariable )

# división
print("_____ división _____")
divi = 100 / 3
print( divi )

diviConFloat = 15 / 3.3
print( diviConFloat )

diviConVariable = 10 / numeroCinco
print( diviConVariable )


#Residuo
mod = 10 % numeroCinco




# Operaciones
print("_____ Operaciones fundamentales _____")
radio = 3
circunferencia = PI * (radio * radio)
print( circunferencia )

base = 5.2
altura = 3
areaTriangulo = ( base * altura ) / 2



print( areaTriangulo )

"""
ACTIVIDAD: Sabiendo el precio de un producto:
    Aplicarle un descuento del 7% 
    Mostrar el precio final con IVA incluido
"""

precio = 100
#descuento = precio - ( precio * 0.07 )
#precio = precio * 0.07
#precio *= 0.07
#precioConIva = (descuento / IVA) + descuento
descuento = 7
total = precio - ( precio * (descuento / 100) )
total += total * (IVA / 100)

total+=10

print( total )


# A + B infijas
# +A  prefija  -5
# A+  posfija  
 
