# Enunciado 10 – Análisis de Texto y Estadísticas de Palabras
# Dado un párrafo de texto, implementa un analizador completo que:
# 1) Extraiga todas las palabras usando regex (solo letras y apóstrofes).
# 2) Construya un diccionario con la frecuencia de cada palabra (sin importar mayúsculas).
# 3) Ordene por frecuencia (desc) y luego alfabéticamente para desempates.
# 4) Muestre el top 5 de palabras más frecuentes y las palabras únicas ordenadas.


import re

def analizador_texto(parrafo):
    total_words = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+", parrafo)
    frequency = {}

    for word in total_words:
        word_min = word.lower()
        frequency[word_min] = frequency.get(word_min, 0) + 1
            
    words_list = list(frequency.items())
    
    words_list.sort(key=lambda x: (-x[1], x[0]))
    
    top_5 = words_list[:5]
    unique = [word for word, frec_1 in words_list if frec_1 == 1]
            
    return top_5, unique

texto = """
Aprender Python es genial, realmente genial. El código en Python es arte 
cuando es limpio y rápido. Un código hermoso refleja una mente limpia, 
por eso escribir código en Python es una filosofía de vida.
"""
top, unique = analizador_texto(texto)

print('='*18, ' ANALIZADOR DE TEXTO ', '='*18)
print(' '*10, '--- TOP 5 PALABRAS MÁS FRECUENTES ---')
for position, (word, frec_2) in enumerate(top, start=1):
    print(' '*14, f"{position}. '{word}': se repite {frec_2} {'vez' if frec_2 == 1 else 'veces'}")

print('\n' + ' '*10, '--- PALABRAS ÚNICAS (ORDENADAS A-Z) ---')
for position, word in enumerate(unique, start=1):
    print(' '*14, f"{position}. {word}")
    
print('='*59)