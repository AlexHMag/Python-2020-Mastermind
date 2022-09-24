"""

Programa Lista de la compra

Que desea comprar? ([Q] para salir) > Leche
Seguro que quiere añadir "Leche"? [S/N] > S
Leche añadido!

Que desea comprar? ([Q] para salir) > Pan
Seguro que quiere añadir "Pan"? [S/N] > N

Que desea comprar? ([Q] para salir) > Pan
Seguro que quiere añadir "Pan"? [S/N] > S
Pan añadido!

Que desea comprar? ([Q] para salir) > Pan
Pan ya está en la lista!

Que desea comprar? ([Q] para salir) > Q
La Lista de la compra es:
["Leche", "Pan"]

"""

lista = []

elemento = None

while elemento != "Q":
    elemento = input("¿Que desea comprar? ([Q] para salir)\n")
    if elemento in lista:
        print("{} ya esta en la lista".format(elemento))
    else:
        if elemento == "Q":
            elemento = "Q"
        else:
            if input("¿Seguro que quiere añadir {}? [S/N]\n".format(elemento)) == "S":
                lista.append(elemento)
            else:
                elemento = None

print("La Lista de la compra es:")
print(lista)

