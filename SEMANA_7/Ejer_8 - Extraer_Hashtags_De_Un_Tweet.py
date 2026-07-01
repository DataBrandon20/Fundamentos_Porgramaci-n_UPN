#Enunciado 8 – EXTRAER HASHTAGS DE UN TWEET:
# Dado un texto de tweet, extrae todos los hashtags (#palabras) y devuélvelos en una lista ordenada y en minúsculas.


def extraction_hashtag(tweet):
    extracted_word_hashtag = []
    words = tweet.strip().split()

    for word in words:
        if word.startswith("#"):
            words_clean = word.lower().rstrip(".,!?")
            if words_clean not in extracted_word_hashtag:
                extracted_word_hashtag.append(words_clean)
    
    extracted_word_hashtag.sort()
    return extracted_word_hashtag     

example_tweet = """
¡Por fin me decidí! Hoy arranqué mi camino en el desarrollo de software. Es increíble lo limpio y legible que es el código en #Python. 
Estoy automatizando mis primeros scripts de #IA y analizando datos con #DataScience. Próxima parada: #Django y desarrollo web.
¡El backend me espera! #python #programacion               
"""

words_hashtag = extraction_hashtag(example_tweet)
print("\n" + "="*30 + "Tweet" + "="*30)
print(example_tweet)
print("\n" + "="*20 + " HASHTAGS EXTRAÍDOS " + "="*20)
print(words_hashtag)
print("="*60 + "\n")