palabras = {
           "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "HYPE": "Tener mucha emoción o expectativas sobre algo",
            "RANDOM": "Algo aleatorio"
           }
print("Hola, este es el diccionario de palabras modernas.")
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in palabras.keys():
    print(palabras[word])
else:
    print("Esa palabra no está en nuestro diccionario.")
