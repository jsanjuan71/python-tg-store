# Slicing | Deslizamiento | Segmentación | Sublistas

import random
nums = [n* random.randint(1,10) for n in range(1000)]

print(nums)

# obtener los primeros 100
count = 0
lista = []
for i in nums:
    if count < 100:
        lista.append(i)
        count += 1
    else:   break

print(lista)
print(f"Último = {lista[ len(lista) - 1]}")

# Naaaa, así no, con slicing
listSliced = nums[:100]
print( f"Último = {listSliced[-1]}" )

# Ahora, los segundos 10
secondTen = nums[10:20] # rebana de 10(excluyente) a 20(incluyente) 
print("lastTen", secondTen)

# Los últimos 5
lastFive = nums[-5:] # rebana de -5 hasta el final
print("lastFive", lastFive)

last = nums[-1] # rebana de 0 a -1(equivale a len-1)
print("last", last)
"""
Actividad: Utilizando la lista de numeros al azar definida arriba
        * Dividir en bloques de 50
        * Por cada bloque, cada numero debe ser divido entre 2 y al final sumar todos
        * Crear una lista con la sumatoria de cada bloque
        * Mostrar los primeros 5
        * Mostrar el penúltimo
"""


