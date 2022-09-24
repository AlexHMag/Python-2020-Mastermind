import readchar
import os
import random

POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 4
map_x = 20
map_y = 15

my_position = [2, 3]  # jugador = @
tail_length = 0
tail = []
map_objects = []

end_game = False
died = False

# Generate random objects



# Main loop
while not end_game:

    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(0, map_x), random.randint(0, map_y)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Pintar el mapa

    print("#" + "#"*map_x*3 + "#")

    for file in range(map_y):
        print("#", end="")

        for column in range(map_x):
            char_to_draw = " "
            objecct_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == column and map_object[POS_Y] == file:
                    char_to_draw = "$"
                    objecct_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == column and tail_piece[POS_Y] == file:
                    char_to_draw = "*"
                    tail_in_cell = tail_piece

            if my_position[POS_Y] == file and my_position[POS_X] == column:  # Colocar jugador
                char_to_draw = "@"

                if objecct_in_cell:
                    map_objects.remove(objecct_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True


            print(" {} ".format(char_to_draw), end="")
        print("#")

    print("#" + "#"*map_x*3 + "#")

    # Movimiento por el mapa

    # direction = input("¿Donde quieres moverte? [WASD]")
    direction = readchar.readchar().decode()  # Detecta que tecla pulsamos, .decode lo transforma en string

    if direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= map_x  # Reposicionamiento
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= map_x  # Reposicionamiento
    elif direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= map_y  # Reposicionamiento
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= map_y  # Reposicionamiento
    elif direction == "Q":
        end_game = True

    os.system("cls")  # Limpiar terminal

if died:
    print("Game Over!")
    input()