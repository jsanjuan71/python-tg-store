import locale

locale.setlocale(locale.LC_ALL, 'en_US')

print(locale.format_string('%.2f', 1005060.216, grouping=True, monetary=True))

"""
ACTIVIDAD: Crear la funcion que devuelva un número en formato de moneda.
"""