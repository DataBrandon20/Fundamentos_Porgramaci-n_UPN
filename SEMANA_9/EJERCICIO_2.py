#EJERCICIO 2
#Enunciado: Crear un archivo de texto llamado 'notas_nuevas.txt'
# y escribir en él los nombres de los estudiantes con notas >= 8.5.
# Usar referencias explícitas para manipular los datos.


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESTUDIANTES_UPN = os.path.join(BASE_DIR, 'ARCHIVO_SEM_9/estudiantes.txt')
NOTAS_NUEVA = os.path.join(BASE_DIR, 'ARCHIVO_SEM_9', 'notas_nueva.txt')

with open(ESTUDIANTES_UPN, 'r', encoding='utf-8') as f_1, \
    open(NOTAS_NUEVA, 'w', encoding='utf-8') as f_2:

    for line in f_1:
        line = line.strip()

        if not line:
            continue

        elements = line.split(',')


        if len(elements) >= 4:
            name = elements[0]
            note = float(elements[3])

            if note >= 8.5:
                f_2.write(f'{name:<16} :  {note}\n')
                print('='*40)