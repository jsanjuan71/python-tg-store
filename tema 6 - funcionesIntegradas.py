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


nombreCentrado = nombre.center(50, " ")
print( nombreCentrado )

nombreEnMayusculas = nombre.upper()
print( nombreEnMayusculas )

print( curso.center(80, " ") )
print( "|%s|%s|%s|%s|%s" % ( 
    arregloFrutas[0].center(15," "), 
    arregloFrutas[1].center(15," "),
    arregloFrutas[2].center(15," "),
    arregloFrutas[3].center(15," "),
    str(1000).center(15," ") ) )

estaturaEnString = str(estatura)
estaturaEnStringCentrada = estaturaEnString.center(80,".")
print( estaturaEnStringCentrada )

print( str(estatura).center(80,"_") )

print( nombre.capitalize() )


print( nombre.split(" ") )

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
print("ACTIVIDAD".center(80,"_"))
parrafo = parrafo.replace("a", "4")
parrafo = parrafo.replace("e", "3")
parrafo = parrafo.replace("o", "0")
parrafo = parrafo.replace("i", "1")
print(parrafo)
listaPalabras = parrafo.split(" ")
primera = listaPalabras[0]
primera = primera.upper()

ultima =  listaPalabras[ len(listaPalabras) - 1]
ultima = ultima.upper()

listaPalabras[0] = primera
listaPalabras[len(listaPalabras) - 1] = ultima

print( str( listaPalabras ) )

print( " ".join( listaPalabras ) )

"erick".capitalize()

#1.capitalize()

#listaPalabras.join(" ")