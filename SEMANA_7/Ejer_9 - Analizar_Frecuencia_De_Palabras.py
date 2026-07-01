#Enunciado 9 – ANALIZAR FRECUENCIA DE PALABRAS:
# Escribe una función que reciba un párrafo de texto y retorne un diccionario con la frecuencia de cada palabra,
# ignorando signos de puntuación, mayúsculas y palabras vacías (stopwords).


def analyze_frequency(text):
    stopwords = {
        "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", 
        "a", "al", "en", "que", "y", "e", "o", "u", "no", "si", "por", "para", 
        "con", "su", "sus", "es", "son", "se", "un", "una", "lo", "como"
    }

    signs = "¡!¿?.,;:-_()[]{}'\"<>*+=/\\|@#$%^&~`\n\t"
    clean_text = " "

    for character in text.lower():
        if character not in signs:
            clean_text += character
        else:
            clean_text += " "
    
    words = clean_text.split()
    frequency = {}

    for word in words:
        if word not in stopwords:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    
    return frequency

example_text = """
Python es un gran lenguaje de programación. La programación con Python es limpia, 
eficiente y muy robusta. Muchos desarrolladores eligen Python porque la programación 
automatiza tareas complejas, y desarrollar en Python es simplemente genial. ¡Amo Python!
"""

result_dictionary = analyze_frequency(example_text)

if result_dictionary:
    print("\n" + "="*20 + " FRECUENCIA DE PALABRAS " + "="*20)

    for index, (word, count) in enumerate(result_dictionary.items(), start=1):
        print(f"Palabra {index}: '{word}' aparece {count} vez/veces")

    print("="*64 + "\n")