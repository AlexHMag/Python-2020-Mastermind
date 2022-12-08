import os
import random
import readchar

MY_POSITION = [2, 2]
BOSS_POSITION = [[45, 5], [2, 10], [45, 15], [2, 17]]
boss = [[45, 5], [2, 10], [45, 15], [2, 17]]
X = 0
Y = 1
boss_win_1 = None
boss_win_2 = None
boss_win_3 = None
boss_win_4 = None
# map
obstacle_definition = """\
████████████████████████████████████████████████
                                               █
                                               █
                                               █
████████████████████████████████████████████   █
████████████████████████████████████████████   █
█                                              █
█                                              █
█                                              █
█   ████████████████████████████████████████████
█   ████████████████████████████████████████████
█                                              █
█                                              █
█                                              █
████████████████████████████████████████████   █
████████████████████████████████████████████   █
                                               █
                                               █
                                               █
████████████████████████████████████████████████\
"""
# Create obstacles map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGTH = len(obstacle_definition)

# Main while
while True:
    print("+" + "-" * (MAP_WIDTH * 2) + "-+")

    for coordinate_y in range(MAP_HEIGTH):
        print("|", end=" ")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "

            for position_boss in boss:

                if position_boss[X] == coordinate_x and position_boss[Y] == coordinate_y:
                    char_to_draw = "✪"

                if (MY_POSITION[X] == position_boss[X] or MY_POSITION[X] == (position_boss[X] + 1) or MY_POSITION[
                    X] == (position_boss[X] - 1)) \
                        and (MY_POSITION[Y] == position_boss[Y] or (MY_POSITION[Y] == position_boss[Y] + 1) or (
                        MY_POSITION[Y] == position_boss[Y] - 1)):

                    if position_boss == BOSS_POSITION[0]:

                        # PRIMER BOSS LEVEL 1 ||||||||||||||||||||||||||||||||| 01 |||||||||||||||||||||||||||||||||||||
                        # PRIMER BOSS LEVEL 1 ||||||||||||||||||||||||||||||||| 01 |||||||||||||||||||||||||||||||||||||
                        while not boss_win_1:
                            os.system("cls")
                            respuesta1 = input("Lt. SURGE DE CIUDAD CARMÍN (Level 1) TE RETA A UN DUELO POKEMÓN\n"
                                               " ¿ACEPTAS? (S/N)")
                            if (respuesta1 == "S") or (respuesta1 == "s"):
                                V_PIKACHU = 80
                                V_SQUIRTLE = 90
                                v_pikachu = V_PIKACHU
                                v_squirtle = V_SQUIRTLE
                                T_BARRA = 20
                                input("ES HORA DE-DE-DE-DE-DE-DEL DUELO¡¡¡\n")
                                os.system("cls")
                                # INICIO DE BUCLE COMBATE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                while (v_pikachu >= 0) or (v_squirtle >= 0):
                                    # TURNO DE PIKACHU||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_pikachu > 0:
                                        print("Turno de Pikachu")
                                        a_pk = random.randint(1, 2)
                                        if a_pk == 1:
                                            print("Pikachu ataca con Bola Voltio")
                                            v_squirtle -= 12
                                        else:
                                            print("Pikachu ataca con Onda Trueno")
                                            v_squirtle -= 14
                                        if v_squirtle > 0:
                                            pk_barra = int(v_pikachu * T_BARRA / V_PIKACHU)
                                            print(str("Pikachu :[{}{}] [{}/{}]").format
                                                  ("█" * pk_barra, " " * (T_BARRA - pk_barra), v_pikachu, V_PIKACHU))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle:[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        else:
                                            v_squirtle = 0
                                            pk_barra = int(v_pikachu * T_BARRA / V_PIKACHU)
                                            print(str("Pikachu :[{}{}] [{}/{}]").format
                                                  ("█" * pk_barra, " " * (T_BARRA - pk_barra), v_pikachu, V_PIKACHU))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle:[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                    else:
                                        print("SQUIRTLE GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        boss.remove(position_boss)
                                        boss_win_1 = True
                                        break
                                    input("Presione Enter para continuar \n")
                                    os.system("cls")
                                    # TURNO DE SQUIRTLE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_squirtle > 0:
                                        a_sq = None
                                        while a_sq not in ["P", "L", "B", "S", "p", "l", "b", "s"]:
                                            print("Turno de Squirtle")
                                            a_sq = input("¿Que ataque deseas realizar?\n"
                                                         "[P]lacaje\n"
                                                         "[L]átigo\n"
                                                         "[B]urbuja\n"
                                                         "[S]altar Turno\n")
                                            os.system("cls")
                                            if (a_sq == "P") or (a_sq == "p"):
                                                print("Turno de Squirtle \nSquirtle ataca con Placaje")
                                                v_pikachu -= 10
                                            elif (a_sq == "L") or (a_sq == "l"):
                                                print("Turno de Squirtle \nSquirtle ataca con Látigo")
                                                v_pikachu -= 12
                                            elif (a_sq == "B") or (a_sq == "b"):
                                                print("Turno de Squirtle \nSquirtle ataca con Burbuja")
                                                v_pikachu -= 14
                                            elif (a_sq == "S") or (a_sq == "s"):
                                                print("Turno de Squirtle \nSquirtle No ataca para descansar")
                                                v_pikachu -= 0
                                        if v_pikachu > 0:
                                            pk_barra = int(v_pikachu * T_BARRA / V_PIKACHU)
                                            print(str("Pikachu :[{}{}] [{}/{}]").format
                                                  ("█" * pk_barra, " " * (T_BARRA - pk_barra), v_pikachu, V_PIKACHU))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle:[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        else:
                                            v_pikachu = 0
                                            pk_barra = int(v_pikachu * T_BARRA / V_PIKACHU)
                                            print(str("Pikachu :[{}{}] [{}/{}]").format
                                                  ("█" * pk_barra, " " * (T_BARRA - pk_barra), v_pikachu, V_PIKACHU))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle:[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        input("Presione Enter para continuar \n")
                                        os.system("cls")
                                    else:
                                        print("PIKACHU GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        break
                            else:
                                os.system("cls")
                                print("+" + "-" * (MAP_WIDTH * 2) + "-+")
                                MY_POSITION = [position_boss[X], (position_boss[Y] - 2)]
                                break
                    elif position_boss == BOSS_POSITION[1]:

                        # SEGUNDO BOSS LEVEL 2 ||||||||||||||||||||||||||||||||| 02 ||||||||||||||||||||||||||||||||||||
                        # SEGUNDO BOSS LEVEL 2 ||||||||||||||||||||||||||||||||| 02 ||||||||||||||||||||||||||||||||||||
                        while not boss_win_2:
                            os.system("cls")
                            respuesta1 = input("ERIKA DE CIUDAD AZULONA (Level 2) TE RETA A UN DUELO POKEMÓN\n"
                                               " ¿ACEPTAS? (S/N)")
                            if (respuesta1 == "S") or (respuesta1 == "s"):
                                V_CHIKORITA = 100
                                V_SQUIRTLE = 100
                                v_chikorita = V_CHIKORITA
                                v_squirtle = V_SQUIRTLE
                                T_BARRA = 20
                                input("ES HORA DE-DE-DE-DE-DE-DEL DUELO¡¡¡\n")
                                os.system("cls")
                                # INICIO DE BUCLE COMBATE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                while (v_chikorita >= 0) or (v_squirtle >= 0):
                                    # TURNO DE CHIKORITA||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_chikorita > 0:
                                        print("Turno de Chikorita")
                                        a_ck = random.randint(1, 3)
                                        if a_ck == 1:
                                            print("Chikorita ataca con Placaje")
                                            v_squirtle -= 14
                                        elif a_ck == 2:
                                            print("Chikorita ataca con Hojas Afiladas")
                                            v_squirtle -= 16
                                        elif a_ck == 3:
                                            print("Chikorita ataca con Hoja Mágica")
                                            v_squirtle -= 18
                                        if v_squirtle > 0:
                                            ck_barra = int(v_chikorita * T_BARRA / V_CHIKORITA)
                                            print(str("Chikorita:[{}{}] [{}/{}]").format
                                                  ("█" * ck_barra, " " * (T_BARRA - ck_barra), v_chikorita,
                                                   V_CHIKORITA))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle :[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        else:
                                            v_squirtle = 0
                                            ck_barra = int(v_chikorita * T_BARRA / V_CHIKORITA)
                                            print(str("Chikorita:[{}{}] [{}/{}]").format
                                                  ("█" * ck_barra, " " * (T_BARRA - ck_barra), v_chikorita,
                                                   V_CHIKORITA))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle :[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                    else:
                                        print("SQUIRTLE GANA Y EVOLUCIONA A WARTORTLE¡¡¡\n"
                                              "+10 Salud\n"
                                              "Wartortle aprendre HIDROBOMBA\n\n")
                                        input("Presione Enter para continuar \n")
                                        boss.remove(position_boss)
                                        boss_win_2 = True
                                        break
                                    input("Presione Enter para continuar \n")
                                    os.system("cls")
                                    # TURNO DE SQUIRTLE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_squirtle > 0:
                                        a_sq = None
                                        while a_sq not in ["P", "L", "B", "U", "p", "l", "b", "u"]:
                                            print("Turno de Squirtle")
                                            a_sq = input("¿Que ataque deseas realizar?\n"
                                                         "[P]lacaje\n"
                                                         "[L]átigo\n"
                                                         "[B]urbuja\n"
                                                         "[U]sar Posición de Curación\n")
                                            os.system("cls")
                                            if (a_sq == "P") or (a_sq == "p"):
                                                print("Turno de Squirtle \nSquirtle ataca con Placaje")
                                                v_chikorita -= 12
                                            elif (a_sq == "L") or (a_sq == "l"):
                                                print("Turno de Squirtle \nSquirtle ataca con Látigo")
                                                v_chikorita -= 14
                                            elif (a_sq == "B") or (a_sq == "b"):
                                                print("Turno de Squirtle \nSquirtle ataca con Burbuja")
                                                v_chikorita -= 16
                                            elif (a_sq == "U") or (a_sq == "u"):
                                                print("Turno de Squirtle \nSquirtle recupera +20p de Salud")
                                                v_squirtle += 20
                                        if v_chikorita > 0:
                                            ck_barra = int(v_chikorita * T_BARRA / V_CHIKORITA)
                                            print(str("Chikorita:[{}{}] [{}/{}]").format
                                                  ("█" * ck_barra, " " * (T_BARRA - ck_barra), v_chikorita,
                                                   V_CHIKORITA))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle :[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        else:
                                            v_chikorita = 0
                                            ck_barra = int(v_chikorita * T_BARRA / V_CHIKORITA)
                                            print(str("Chikorita:[{}{}] [{}/{}]").format
                                                  ("█" * ck_barra, " " * (T_BARRA - ck_barra), v_chikorita,
                                                   V_CHIKORITA))
                                            sq_barra = int(v_squirtle * T_BARRA / V_SQUIRTLE)
                                            print(str("Squirtle :[{}{}] [{}/{}]").format
                                                  ("█" * sq_barra, " " * (T_BARRA - sq_barra), v_squirtle, V_SQUIRTLE))
                                        input("Presione Enter para continuar \n")
                                        os.system("cls")
                                    else:
                                        print("CHIKORITA GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        break
                            else:
                                MY_POSITION = [position_boss[X], (position_boss[Y] - 2)]
                                print("+" + "-" * (MAP_WIDTH * 2) + "-+")
                                break
                    elif position_boss == BOSS_POSITION[2]:

                        # TERCER BOSS LEVEL 3 ||||||||||||||||||||||||||||||||| 03 |||||||||||||||||||||||||||||||||||||
                        # TERCER BOSS LEVEL 3 ||||||||||||||||||||||||||||||||| 03 |||||||||||||||||||||||||||||||||||||
                        while not boss_win_3:
                            os.system("cls")
                            respuesta1 = input("BLAINE DE ISLA CANELA (Level 3) TE RETA A UN DUELO POKEMÓN\n"
                                               " ¿ACEPTAS? (S/N)")
                            if (respuesta1 == "S") or (respuesta1 == "s"):
                                V_NINETALES = 100
                                V_WARTORTLE = 110
                                v_ninetales = V_NINETALES
                                v_wartortle = V_WARTORTLE
                                T_BARRA = 20
                                input("ES HORA DE-DE-DE-DE-DE-DEL DUELO¡¡¡\n")
                                os.system("cls")
                                # INICIO DE BUCLE COMBATE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                while (v_ninetales >= 0) or (v_wartortle >= 0):
                                    # TURNO DE NINETALES||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_ninetales > 0:
                                        print("Turno de Ninetales")
                                        a_nt = random.randint(1, 4)
                                        if a_nt == 1:
                                            print("Ninetales ataca con Rugido")
                                            v_wartortle -= 14
                                        elif a_nt == 2:
                                            print("Ninetales ataca con Ataque Rápido")
                                            v_wartortle -= 16
                                        elif a_nt == 3:
                                            print("Ninetales ataca con Ascuas")
                                            v_wartortle -= 18
                                        elif a_nt == 4:
                                            print("Ninetales ataca con Giro Fuego")
                                            v_wartortle -= 25
                                        if v_wartortle > 0:
                                            nt_barra = int(v_ninetales * T_BARRA / V_NINETALES)
                                            print(str("Ninetales:[{}{}] [{}/{}]").format
                                                  ("█" * nt_barra, " " * (T_BARRA - nt_barra), v_ninetales,
                                                   V_NINETALES))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle:[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        else:
                                            v_wartortle = 0
                                            nt_barra = int(v_ninetales * T_BARRA / V_NINETALES)
                                            print(str("Ninetales:[{}{}] [{}/{}]").format
                                                  ("█" * nt_barra, " " * (T_BARRA - nt_barra), v_ninetales,
                                                   V_NINETALES))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle:[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                    else:
                                        print("WARTORTLE GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        boss.remove(position_boss)
                                        boss_win_3 = True
                                        break
                                    input("Presione Enter para continuar \n")
                                    os.system("cls")
                                    # TURNO DE WARTORTLE |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_wartortle > 0:
                                        a_sq = None
                                        while a_sq not in ["L", "B", "H", "U", "l", "b", "h", "u"]:
                                            print("Turno de Wartortle")
                                            a_sq = input("¿Que ataque deseas realizar?\n"
                                                         "[L]átigo\n"
                                                         "[B]urbuja\n"
                                                         "[H]idroBomba\n"
                                                         "[U]sar Posición de Curación\n")
                                            os.system("cls")
                                            if (a_sq == "L") or (a_sq == "l"):
                                                print("Turno de Wartortle \nWartortle ataca con Látigo")
                                                v_ninetales -= 16
                                            elif (a_sq == "B") or (a_sq == "b"):
                                                print("Turno de Wartortle \nWartortle ataca con Burbuja")
                                                v_ninetales -= 18
                                            elif (a_sq == "H") or (a_sq == "h"):
                                                print("Turno de Wartortle \nWartortle ataca con HidroBomba")
                                                v_ninetales -= 20
                                            elif (a_sq == "U") or (a_sq == "u"):
                                                print("Turno de Wartortle \nWartortle recupera +20p de Salud")
                                                v_wartortle += 20

                                        if v_ninetales > 0:
                                            nt_barra = int(v_ninetales * T_BARRA / V_NINETALES)
                                            print(str("Ninetales:[{}{}] [{}/{}]").format
                                                  ("█" * nt_barra, " " * (T_BARRA - nt_barra), v_ninetales,
                                                   V_NINETALES))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle:[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        else:
                                            v_ninetales = 0
                                            nt_barra = int(v_ninetales * T_BARRA / V_NINETALES)
                                            print(str("Ninetales:[{}{}] [{}/{}]").format
                                                  ("█" * nt_barra, " " * (T_BARRA - nt_barra), v_ninetales,
                                                   V_NINETALES))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle:[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        input("Presione Enter para continuar \n")
                                        os.system("cls")
                                    else:
                                        print("NINETALES GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        break
                            else:
                                MY_POSITION = [position_boss[X], (position_boss[Y] - 2)]
                                print("+" + "-" * (MAP_WIDTH * 2) + "-+")
                                break
                    elif position_boss == BOSS_POSITION[3]:

                        # CUARTO BOSS LEVEL 4 ||||||||||||||||||||||||||||||||| 04 |||||||||||||||||||||||||||||||||||||
                        # CUARTO BOSS LEVEL 4 ||||||||||||||||||||||||||||||||| 04 |||||||||||||||||||||||||||||||||||||
                        while not boss_win_4:
                            os.system("cls")
                            respuesta1 = input("WALLACE DE GIMNASIO ARRECÍPOLIS (Level 4) TE RETA A UN DUELO POKEMÓN\n"
                                               "¿ACEPTAS? (S/N)")
                            if (respuesta1 == "S") or (respuesta1 == "s"):
                                V_TENTACRUEL = 110
                                V_WARTORTLE = 130
                                v_tentacruel = V_TENTACRUEL
                                v_wartortle = V_WARTORTLE
                                T_BARRA = 20
                                input("ES HORA DE-DE-DE-DE-DE-DEL DUELO¡¡¡\n")
                                os.system("cls")
                                # INICIO DE BUCLE COMBATE|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                while (v_tentacruel >= 0) or (v_wartortle >= 0):
                                    # TURNO DE TENTACRUEL|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_tentacruel > 0:
                                        print("Turno de Tentacruel")
                                        a_tc = random.randint(1, 4)
                                        if a_tc == 1:
                                            print("Tentacruel ataca con Picotazo")
                                            v_wartortle -= 15
                                        elif a_tc == 2:
                                            print("Tentacruel ataca con Ácido")
                                            v_wartortle -= 20
                                        elif a_tc == 3:
                                            print("Tentacruel ataca con Rayo Burbuja")
                                            v_wartortle -= 25
                                        elif a_tc == 4:
                                            print("Tentacruel ataca con Hiperrayo")
                                            v_wartortle -= 30
                                        if v_wartortle > 0:
                                            tc_barra = int(v_tentacruel * T_BARRA / V_TENTACRUEL)
                                            print(str("Tentacruel:[{}{}] [{}/{}]").format
                                                  ("█" * tc_barra, " " * (T_BARRA - tc_barra), v_tentacruel,
                                                   V_TENTACRUEL))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle :[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        else:
                                            v_wartortle = 0
                                            tc_barra = int(v_tentacruel * T_BARRA / V_TENTACRUEL)
                                            print(str("Tentacruel:[{}{}] [{}/{}]").format
                                                  ("█" * tc_barra, " " * (T_BARRA - tc_barra), v_tentacruel,
                                                   V_TENTACRUEL))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle :[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                    else:
                                        print("WARTORTLE GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        boss.remove(position_boss)
                                        boss_win_4 = True
                                        break
                                    input("Presione Enter para continuar \n")
                                    os.system("cls")
                                    # TURNO DE WARTORTLE |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                    if v_wartortle > 0:
                                        a_wt = None
                                        while a_wt not in ["U", "L", "B", "H", "u", "l", "b", "h"]:
                                            print("Turno de Wartortle")
                                            a_wt = input("¿Que ataque deseas realizar?\n"
                                                         "[L]átigo\n"
                                                         "[B]urbuja\n"
                                                         "[H]idroBomba\n"
                                                         "[U]sar Posición de Sanación\n")

                                            os.system("cls")
                                            if (a_wt == "L") or (a_wt == "l"):
                                                print("Turno de Wartortle \nWartortle ataca con Látigo")
                                                v_tentacruel -= 18
                                            elif (a_wt == "B") or (a_wt == "b"):
                                                print("Turno de Wartortle \nWartortle ataca con Burbuja")
                                                v_tentacruel -= 20
                                            elif (a_wt == "H") or (a_wt == "h"):
                                                print("Turno de Wartortle \nWartortle ataca con HidroBomba")
                                                v_tentacruel -= 22
                                            elif (a_wt == "U") or (a_wt == "u"):
                                                print("Turno de Wartortle \nWartortle recupera +20p de salud")
                                                v_wartortle += 20

                                        if v_tentacruel > 0:
                                            tc_barra = int(v_tentacruel * T_BARRA / V_TENTACRUEL)
                                            print(str("Tentacruel:[{}{}] [{}/{}]").format
                                                  ("█" * tc_barra, " " * (T_BARRA - tc_barra), v_tentacruel,
                                                   V_TENTACRUEL))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle :[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        else:
                                            v_tentacruel = 0
                                            tc_barra = int(v_tentacruel * T_BARRA / V_TENTACRUEL)
                                            print(str("Tentacruel:[{}{}] [{}/{}]").format
                                                  ("█" * tc_barra, " " * (T_BARRA - tc_barra), v_tentacruel,
                                                   V_TENTACRUEL))
                                            wt_barra = int(v_wartortle * T_BARRA / V_WARTORTLE)
                                            print(str("Wartortle :[{}{}] [{}/{}]").format
                                                  ("█" * wt_barra, " " * (T_BARRA - wt_barra), v_wartortle,
                                                   V_WARTORTLE))
                                        input("Presione Enter para continuar \n")
                                        os.system("cls")
                                    else:
                                        print("TENTACRUEL GANA¡¡¡")
                                        input("Presione Enter para continuar \n")
                                        break
                            else:
                                MY_POSITION = [position_boss[X], (position_boss[Y] - 2)]
                                print("+" + "-" * (MAP_WIDTH * 2) + "-+")
                                break

            if MY_POSITION[X] == coordinate_x and MY_POSITION[Y] == coordinate_y:
                char_to_draw = "☻"
            if obstacle_definition[coordinate_y][coordinate_x] == "█":
                char_to_draw = "█"
            print("{}".format(char_to_draw), end=" ")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "-+")

    if boss_win_1 and boss_win_2 and boss_win_3 and boss_win_4:
        os.system("cls")
        print("OBTIENES LA MEDALLA AGUA")
        print("¡¡¡FELICIDADES!!!")
        break
    direction = readchar.readchar()
    my_move_position = None
    recovery_move = MY_POSITION.copy()
    if direction == "w":
        my_move_position = [MY_POSITION[X], (MY_POSITION[Y] - 1) % MAP_HEIGTH]
    elif direction == "s":
        my_move_position = [MY_POSITION[X], (MY_POSITION[Y] + 1) % MAP_HEIGTH]
    elif direction == "a":
        my_move_position = [(MY_POSITION[X] - 1) % MAP_WIDTH, MY_POSITION[Y]]
    elif direction == "d":
        my_move_position = [(MY_POSITION[X] + 1) % MAP_WIDTH, MY_POSITION[Y]]
    elif direction == "q":
        break
    if my_move_position:
        if obstacle_definition[my_move_position[Y]][my_move_position[X]] != "█":
            MY_POSITION = my_move_position
    os.system("cls")