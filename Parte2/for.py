
vocales = ["a", "e", "i", "o", "u"]
vocales_encontradas = 0

frase = "Buenos dias, hoy ha llovido"

for letra in frase:
    if letra in vocales:
        print("He encontrado unas: {}".format(letra))
        vocales_encontradas += 1

print("He encontrado todas estas vocales: {}".format(vocales_encontradas))