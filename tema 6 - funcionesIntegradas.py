#https://docs.python.org/3/library/functions.html

x = 20
y = 10
edad = 32
curso = "Python desde cero"
nombre = "Julio Sanjuan"
parrafo = """Ciña ¡oh Patria! tus sienes de oliva 
De la paz el arcángel divino, 
Que en el cielo tu eterno destino, 
Por el dedo de Dios se escribió; 
Mas si osare un extraño enemigo, 
Profanar con su planta tu suelo, 
Piensa ¡oh Patria querida! que el cielo 
Un soldado en cada hijo te dio, 
Un soldado en cada hijo te dio."""
estatura = 1.71
esInstructor = True
arregloFrutas = ["manzana", "platano", "uva", "sandía"]
tuplaCoordenadas = (-109.33, 98.209)
objetoProducto = {"nombre": "iPhone X", "precio": 19999, "color":"space gray"}

print( "Hola" )
print( 2022 )

print( nombre )
print( estatura )
print( "Hola %s" % (nombre) )
print( "Mides %5.1f" % (estatura) )

nombreCentrado = nombre.center(80, "*")
print( nombreCentrado )

nombreEnMayusculas = nombre.upper()
print( nombreEnMayusculas )

print( curso.center(80, " ") )
print( "|%s|%s|%s|%s|" % ( 
    arregloFrutas[0].center(20," "), 
    arregloFrutas[1].center(20," "),
    arregloFrutas[2].center(20," "),
    arregloFrutas[3].center(20," ")) )

estaturaEnString = str(estatura)
estaturaEnStringCentrada = estaturaEnString.center(80,".")
print( estaturaEnStringCentrada )

print( str(estatura).center(80,"_") )

print( nombre.capitalize() )


print( nombre.split() )

palabrasDelParrafo = parrafo.split(" ")

print( palabrasDelParrafo )

print( type(palabrasDelParrafo[4]) )

print( "_".join( palabrasDelParrafo) )

print( curso.replace("o", "0") )

print( len(palabrasDelParrafo) )

"""
ACTIVIDAD: Remplazar las vocales del parrafo usando el siguiente esquema:
    a = 4
    e = 3
    o = 0
    i = 1

    La primera y ultima palabra del párrafo deben ser cambiadas a mayúsculas

    Mostrar el párrafo con el resultado final
"""