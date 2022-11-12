numero = "10x"
#print( int(numero) )

try:
    print( int(numero) )
except ValueError:
    print(f"{numero} No es un número válido")

division = None
divisor = 0
try:
    division = 35 / divisor
except ZeroDivisionError:
    pass

try:
    division = dividendo / divisor
except Exception as error:
    print(f"ERROR: {error}")


#ES MEJOR PREVENIR

if( divisor != 0 ):
    division = 35 / divisor
else:
    division = 0



 