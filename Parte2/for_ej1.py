"""

--> introducir nummeros y que saque el max y min

#Lista numeros
numeros = [4, 2, 5, 3, 1, 9]

#Output
max_numero: 9
min_numero: 1
"""

numeros = []

introducido = int(input("Introduzca un numero: "))
numeros.append(introducido)

while input("Desea introducir mas numeros? [S/N]") == "S":
    introducido = int(input("Introduzca un numero: "))
    numeros.append(introducido)

max_numero = numeros[0]
min_numero = max_numero

for numero in numeros:
    if numero >= max_numero:
        max_numero = numero
    elif numero <= min_numero:
        min_numero = numero


print(numeros)
print(max_numero)
print(min_numero)


