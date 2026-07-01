#EJERCICIO 3
#Enunciado: Leer 'registro_sistema.log' y contar cuántos mensajes
# hay de cada tipo: INFO, WARNING, ERROR. Mostrar el resumen.


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRO_SISTEMA = os.path.join(BASE_DIR, 'ARCHIVO_SEM_9', 'registro_sistema.log')

with open(REGISTRO_SISTEMA, 'r', encoding='utf-8') as f:
    message_count = {}

    for line in f:
        line = line.strip()

        if not line:
            continue
        
        elements = line.split('|')

        if len(elements) >= 3:
            clean_element_1 = elements[1].strip()

            if clean_element_1 in message_count:
                message_count[clean_element_1] += 1
            else:
                message_count[clean_element_1] = 1

for key, value in message_count.items():
    print(f'{key:<8}  |  {value} veces')