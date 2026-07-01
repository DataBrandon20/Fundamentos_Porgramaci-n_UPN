# Enunciado 9 – Buscador Inteligente con Regex y Ordenamiento
# Implementa una función buscador(catalogo, query) que reciba una lista de diccionarios
# con campos 'titulo', 'autor' y 'año'. La función debe:
# 1) Buscar el query en título y autor (regex, case-insensitive).
# 2) Ponderar resultados: coincidencia en título vale 2 puntos, en autor 1 punto.
# 3) Retornar resultados ordenados por puntaje (mayor a menor) y luego por año.

import re

def search(catalog, query):
    results = []
    
    for book in catalog:
        score = 0
        
        if re.search(query, book['title'], re.I):
            score += 2
            
        if re.search(query, book['author'], re.I):
            score += 1
            
        if score > 0:
            copy_book = book.copy()
            copy_book['score'] = score
            results.append(copy_book)
            
    results.sort(key=lambda x: (-x['score'], x['year']))
    
    return results

my_catalog = [
    {'title': 'Cien años de soledad', 'author': 'Gabriel García Márquez', 'year': 1967},
    {'title': 'El amor en los tiempos del cólera', 'author': 'Gabriel García Márquez', 'year': 1985},
    {'title': 'Crónica de una muerte anunciada', 'author': 'Gabriel García Márquez', 'year': 1981},
    {'title': 'Gabriel: Biografía de un mito', 'author': 'Gerald Martin', 'year': 2008}
]

print('='*28, f" BUSCADOR SMART: 'gabriel' ", '='*29)
for book in search(my_catalog, "gabriel"):
    print(' '*2, f"Score: {book['score']} pts | {book['title']:<33} ({book['year']}) | {book['author']}")

print('='*86)