import os

EXIT = "SALIR"


def quest():
    return input("Introduce un producto [{} para salir de la lista]: ".format(EXIT))


def create_list(list_name, buy_list):
    with open(list_name + ".txt", "w") as my_list:
        my_list.write("\n".join(buy_list))
    #a = open("{}.txt".format(list_name), "w")  # Abre(crea) compras.txt en modo escritura: w (write),
    # r para leer, a para agregar sin borrar
    #a.write("\n".join(buy_list))
    #a.close()


def main():
    list_name = input("Cual sera el nombre de la lista? ")
    buy_list = []
    input_user = quest()

    while input_user != EXIT:
        if input_user.lower() in [a.lower() for a in buy_list]:  # For rapidito, list compresion.
            print("Ya esta en la lista")
        else:
            buy_list.append(input_user)
        os.system("cls")
        print("\n".join(buy_list))
        input_user = quest()

    create_list(list_name, buy_list)


if __name__ == "__main__":
    main()
