#EJERCICIO 1
#Enunciado: Leer el archivo 'estudiantes.txt' y mostrar el nombre
# y la nota de cada estudiante usando referencias a objetos (punteros en Python).
# Muestra además la identidad de memoria de cada objeto creado.


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESTUDIANTES_UPN = os.path.join(BASE_DIR, 'ARCHIVO_SEM_9/estudiantes.txt')

with open(ESTUDIANTES_UPN, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        elements = line.split(',')

        if len(elements) >= 4:
            name = elements[0]
            note = elements[3]

            print(f'{name:<17}  |  {note}')
            print(f'{id(name):<17}  |  {[id(note)]}')
            print('='*40)
        else:
            print(f'Línea ignorada por formato incorrecto: ({line})')
            print('='*40)