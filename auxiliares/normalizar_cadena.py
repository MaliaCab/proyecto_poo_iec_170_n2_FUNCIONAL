'''
from auxiliares.normalizar_cadena import normalizar_cadena

nombre_producto = "Máscara de Pestañas"
nombre_normalizado = normalizar_cadena(nombre_producto)
print(nombre_normalizado)  # salida: "mascara de pestanas"


'''
import unicodedata


def normalizar_cadena(cadena):
    s_decomposed = unicodedata.normalize('NFD', cadena)
    s_filtered = ''.join(
        c for c in s_decomposed if unicodedata.category(c) != 'Mn')
    return s_filtered.lower()