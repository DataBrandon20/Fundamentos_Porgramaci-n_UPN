#EJERCICIO 4
#Enunciado: Escribir y leer un archivo binario que almacene
# 5 números enteros usando el módulo 'struct'.
# Verificar que los datos escritos y leídos sean idénticos.


import os
import struct

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_BINARIO = os.path.join(BASE_DIR, 'ARCHIVO_SEM_9', 'numeros.bin')

numbers_original = [23, 47, 152, 28, 1006]

with open(ARCHIVO_BINARIO, 'wb') as f:
    binary_data = struct.pack('5i', *numbers_original)
    f.write(binary_data)
    print('Datos empaquetados y guardados con éxito.')

with open(ARCHIVO_BINARIO, 'rb') as f:
    datos_read = f.read()
    unpacked_numbers = struct.unpack('5i', datos_read)

numeros_leidos_lista = list(unpacked_numbers)

print(f"Originales : {numbers_original}")
print(f"Leídos     : {numeros_leidos_lista}")