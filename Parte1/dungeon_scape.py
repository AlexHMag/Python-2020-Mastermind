import random

texto = "Dungeon Scapist"
print(texto + "\n" + "-" * len(texto) + "\n")
print("Te encuentras en las sombras intentando escapar de los omnis, tienes dos opciones meterte por una puerta o ir"
      "por una trampilla en el suelo. Hacía dónde te diriges?")

opcion = input("Qué salida vas a tomar? A) Puerta / B) Trampilla")

if opcion == "A":
    print("Entras en la puerta y otro guardia te descubre, que haces ?")
    opcion = input("A) Te haces el dormido / B) Sales corriendo hacia la siguiente puerta")

    if opcion == "A":
        print("GAME OVER")
    elif opcion == "B":
        print("Despues de entrar en la puerta encuentra un rana mutante que te regala un puñal, lo aceptas? ")
        opcion = input("[S/N]")

        if opcion == "S":
            print("Coges el pincho y avanzas, hay dos pasillos uno a la izquierda y otro a la redercha. Cual tomas? ")
            opcion = input("A) Izquierda / B) Derecha")

            if opcion == "A":
                print("GAME OVER")
            elif opcion == "B":
                print("FELICIDADES, HAS COMPLETADO EL JUEGO")

        elif opcion == "N":
            print("GAME OVER")

elif opcion == "B":
    print("Caes a unas alcantarillas donde encuentras un palo, lo coges?")
    opcion = input("[S/N]")

    palo_cogido = False

    if opcion == "S":
        print("Coges el palo")
        palo_cogido = True
    elif opcion == "N":
        print("Dejas el palo")
    else:
        print("GAME OVER")
        exit()

    numero_rata = random.randint(1,100)
    print("Te encuentras una rata de dos metros, te pregunta cuanto es 13 *", numero_rata)
    opcion = int(input("Cúal es el resultado? "))


    if opcion == 13 * numero_rata:
        print("GAME OVER")
    else:
        print("La rata te deja pasar por un tunel pero este se Derrumba, no hay salida solo un agujero a escasos metros"
              "Que haces?")
        opcion = input("A) Esperas a que alguien venga a rescatarte / B) Utilizas el palo para escapar")

        if opcion == "A":
            print("GAME OVER")

        elif opcion == "B" and palo_cogido == True:
            print("ENHORABUENA, HAS CONSEGUIDO ESCAPAR DE LA PRISIÓN")

        elif opcion == "B" and palo_cogido == False:
            print("GAME OVER")

else:
    print("HAS MUERTO")
    exit()