x = 20
y = 10
nombre = "Julio Sanjuan"
edad = 12
estatura = 1.71
esInstructor = True



if edad >= 18:
    print("Usted ya es mayor de edad")
    if estatura >= 1.70:
        print("Usted ya es mayor de edad y mide mas de 1.7")
        print("print")
# ----------------------------------------------------------------
if edad > 17:
    print("Usted ya es mayor de edad")
else:
    print("Usted NO es mayor de edad")

# ----------------------------------------------------------------

if edad >= 65:
    print("Usted ya es de la tercera edad")
elif edad >= 18:
    print("Usted ya es mayor de edad")
elif edad >=2:
    print("Usted es un infante")
else:
    print("Usted es un bebé")



"""
ACTIVIDAD: Crear la promoción "TODOS GANAN" para un producto con las siguientes condiciones: 
    si el precio es mayor a $5000 aplicar el 10% de descuento
    si el precio es mayor a $999 aplicar el 5% de desceunto
    si el precio es menor 1000 aplicar el 1%

    Una vez calculada la promoción mostrar al usuario el precio final con IVA incluido
"""
precio= 5000
conDescuento = 0
IVA = 16
if precio > 5000:
    conDescuento = precio - (precio * 0.1)
elif precio > 999:
    conDescuento = precio - (precio * 0.05)
else:
    conDescuento = precio - (precio * 0.01)

print( conDescuento * (1+(IVA/100)) )