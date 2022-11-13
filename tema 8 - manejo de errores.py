numero = "10Xt"
#print( int(numero) )

try:
    print( int(numero) )
    print("otra cosa")
except ValueError:
    print(f"{numero} No es un número válido")
    print("send email")

division = None
divisor = 0
try:
    division = 35 / divisor
except (ZeroDivisionError, ValueError):
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



 