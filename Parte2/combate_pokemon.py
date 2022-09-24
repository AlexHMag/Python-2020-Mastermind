from random import randint
import os

VIDA_INICIAL_P = 80
VIDA_INICIAL_S = 90

TAMANIO_VIDA = 20

vida_p = VIDA_INICIAL_P
vida_s = VIDA_INICIAL_S

barra_p = int((vida_p * TAMANIO_VIDA) / VIDA_INICIAL_P)
barra_s = int((vida_s * TAMANIO_VIDA) / VIDA_INICIAL_S)

print("Empieza el combate entre Pikachu y Squirtel\n")
print("Pikachu  [{}{}]   {}PV".format("*"*barra_p, " "*(TAMANIO_VIDA-barra_p), vida_p))
print("Squirtel [{}{}]   {}PV".format("*"*barra_s, " "*(TAMANIO_VIDA-barra_s), vida_s))
input("Enter para continuar... \n\n")

while vida_p > 0 and vida_s > 0:
    os.system("cls")
    #Pikachu
    print("Turno de pikachu")
    ataque_p = randint(1, 2)
    if ataque_p == 1:
        #Bola voltio
        print("Pikachu uso bola voltio")
        vida_s -= 10
    else:
        #Onda trueno
        print("Pikachu uso onda trueno")
        vida_s -= 11

    barra_s = int((vida_s * TAMANIO_VIDA) / VIDA_INICIAL_S)
    print("Pikachu  [{}{}]   {}PV".format("*" * barra_p, " " * (TAMANIO_VIDA - barra_p), vida_p))
    print("Squirtel [{}{}]   {}PV".format("*" * barra_s, " " * (TAMANIO_VIDA - barra_s), vida_s))
    input("Enter para continuar... \n\n")

    os.system("cls")
    #Squirtel
    print("Turno de Squirtel")
    ataque_s = None

    while ataque_s != "p" and ataque_s != "a" and ataque_s != "b":
        ataque_s = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua o [B]urbuja: ")
        if ataque_s == "p":
            vida_p -= 10
        elif ataque_s == "a":
            vida_p -= 12
        elif ataque_s == "b":
            vida_p -= 9

    barra_p = int((vida_p * TAMANIO_VIDA) / VIDA_INICIAL_P)
    print("Pikachu  [{}{}]   {}PV".format("*" * barra_p, " " * (TAMANIO_VIDA - barra_p), vida_p))
    print("Squirtel [{}{}]   {}PV".format("*" * barra_s, " " * (TAMANIO_VIDA - barra_s), vida_s))
    input("Enter para continuar... \n\n")

if vida_p > vida_s:
    print("Pikachu gana\n")
else:
    print("Squirtel gana\n")

input("Pulsa Enter para salir.")

