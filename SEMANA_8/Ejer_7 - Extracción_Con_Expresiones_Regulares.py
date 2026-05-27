# Enunciado 7 – Extracción con Expresiones Regulares
# Dada una lista de strings con información mezclada como:
# ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
# Usa expresiones regulares para extraer el nombre, la edad y el teléfono de cada registro
# y almacénalos en una lista de diccionarios.


import re

user_list = ['Ana García - edad:25 - tel:987654321', 'Luis Pérez - edad:30 - tel:912345678']
new_list = []
patterns = r'(.*?) - edad:(\d+) - tel:(\d+)'

for element in user_list:
    match = re.search(patterns, element)

    if match:
        dictionary = {
            'name': match.group(1),
            'age': int(match.group(2)),
            'num': int(match.group(3))
        }
        new_list.append(dictionary)

print('='*20, ' REGISTROS PROCESADOS ', '='*20)
for key in new_list:
    print(' '*8 + f"Nombre: {key['name']:<10} | Edad: {key['age']:>2} años | Tel: {key['num']}")
print('='*64)