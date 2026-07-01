#Enunciado 6 – CENSURAR PALABRA EN UN TEXTO:
# Dada una lista de palabras prohibidas, reemplaza cada aparición en un texto por asteriscos del mismo largo.


def censor_text(original_text, banned_list):
    text_to_process = original_text
    words_to_censor = banned_list.split(",")

    for word in words_to_censor:
        replace_asterisc = "*" * len(word)
        text_to_process = text_to_process.replace(word, replace_asterisc)
        text_to_process = text_to_process.replace(word.title(), replace_asterisc)

    return text_to_process

example_text = "El dominio de Python se ha convertido en una habilidad clave en el mercado tecnológico actual. Cuando un programador suma este lenguaje a su perfil, eleva drásticamente sus oportunidades de conseguir un buen trabajo. La mejor manera de demostrar este conocimiento ante los reclutadores es construyendo un proyecto propio y sólido, ya que un portafolio con código real dice más que cualquier currículum."
forbidden_words = "python,trabajo,proyecto"
text_censored = censor_text(example_text, forbidden_words)

print("\n" + "="*20 + " TEXTO ORIGINAL " + "="*20)
print(example_text)
print("\n" + "="*20 + " TEXTO CENSURADO " + "="*20)
print(text_censored)
print("="*56 + "\n")