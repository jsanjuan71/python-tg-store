from locale import format_string as localeFormatString, setlocale, LC_ALL

import openpyxl

#from opencv import v, l, r as opencv_reader

setlocale( LC_ALL, 'en_US')

print("$"+ localeFormatString('%.2f', 1005060.21656656565, grouping=True, monetary=True))

"""
ACTIVIDAD: Crear la funcion que devuelva un número en formato de moneda.
"""