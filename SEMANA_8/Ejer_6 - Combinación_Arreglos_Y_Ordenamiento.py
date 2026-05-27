# Enunciado 6 – Combinación de Arreglos y Ordenamiento
# Tienes dos arreglos paralelos: productos (strings) y ventas (enteros).
# Combínalos en una lista de diccionarios, luego:
# 1) Ordena por ventas de mayor a menor.
# 2) Imprime el ranking con posición (1°, 2°, etc.).
# 3) Calcula el promedio de ventas e indica cuáles están sobre la media.


products = ['Pantalla', 'Teclado', 'Mouse', 'Tarjeta Gráfica', 'Memoria Ram']
sales = [35, 17, 23, 8, 38]

dictionary = []

for key, value in zip(products, sales):
    new_list = {'products': key, 'sales': value}
    dictionary.append(new_list)

dictionary.sort(reverse=True, key=lambda x: x['sales'])

print('='*19, ' RANKING DE VENTAS ', '='*20)
for index, key in enumerate(dictionary, start=1):
    print(' '*11, f"Position {index:<2}| {key['products']:<16} : {key['sales']:>2} unidades")
    
print('\n' + '='*18, ' ANÁLISIS DE LA MEDIA ', '='*18)
average = sum(sales) / len(sales)
print(' '*9, f"El promedio de ventas general es: {average:.1f}\n")

print(' '*9, "Productos que superan la media:")
for key in dictionary:
    if key['sales'] > average:
        print(' '*9, f"• {key['products']:<16} ({key['sales']} unidades)")
print('='*60)