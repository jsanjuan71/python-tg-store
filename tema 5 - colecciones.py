# list | lista | array | arreglo | vector 
arregloFrutas = ["manzana", "platano","pera"]
puntosReacta = [ (10,2) , (5,4) ] 
edadDeJulio = 32
# tuple | tupla
tuplaCoordenadas = (-109.33, 98.209, 10)

# dict | diccionario | objeto ¡ JSON
objetoProducto = {"nombre": "Julio Sanjuan", "edad": edadDeJulio, "estatura":1.71, "ubicaciones": [ ({"x":[1,2],"lat":-433443},2) , (5,4) ]}

nombres =  [ "Julio", "David", "Esly" ]

obj = { "nombres": nombres}



#acceso a las colecciones

# list
print( arregloFrutas[1] )

# tuple
x,y,z = tuplaCoordenadas
print( x )

# dict
print( objetoProducto["edad"] )


""""
ACTIVIDAD: Crear 3 colleciones para el proyecto, de la siguiente forma:
    Un diccionario para representar un producto de nuestra tienda
    Una lista para guardar todas las cetegorias de productos que vamos a manejar
    Una tupla para representar el precio de un producto en MXN y en USD
"""






