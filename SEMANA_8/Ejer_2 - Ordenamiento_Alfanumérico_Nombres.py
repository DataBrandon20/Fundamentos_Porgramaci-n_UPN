# Enunciado 2 – Ordenamiento Alfanumérico de Nombres
# Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
# 1) Imprímela sin modificar.
# 2) Ordénala alfabéticamente ignorando mayúsculas con sort().
# 3) Crea una nueva lista ordenada en orden descendente usando sorted().
# 4) Muestra los resultados de cada paso.


names = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print('='*22, ' LISTA ORIGINAL ', '='*22)
print(' '*7, f'{names}\n')

print('='*14, ' LISTA ORDENADA ALFABÉTICAMENTE ', '='*14)
names.sort(key=str.lower)
print(' '*7, f'{names}\n')

print('='*5, ' LISTA ORDENADA ALFABÉTICAMENTE FORMA DESCENDENTE ', '='*5)
original_list_names = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print(' '*7, sorted(original_list_names, reverse=True, key=str.lower), '\n')
print('='*62)