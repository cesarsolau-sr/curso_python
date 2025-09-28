palabras =  ["python", "programación", "lista", "comprehension", "for", "if", "else", "diccionario"]
new_palabras = [palabra.upper() for palabra in palabras if len(palabra) > 4 ]
print(new_palabras)