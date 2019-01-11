from termcolor import colored
import random

map = [
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
    ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?"],
]
map_coordinates = []

F_locations = []

O_locations = []

H_locations = []

V_locations = []


for row_index, row in enumerate(map):  # <- with the enumerate, I can print the indexes
    for column_index, column in enumerate(row):  # <- with the enumerate, I can print the indexes
        map_coordinates.append([row_index, column_index])

position = [8, 8]
P_position = []

def T_C_terrain(map):
    T_chance = random.randint(1, 4)
    C_chance = random.randint(0, 15)
    global position
    global map_coordinates

    if T_chance == 1:
        for r in range(16):
            map[r][0] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [r, 0]:
                    map_coordinates.remove([r, 0])

            if map[r][1] == map[C_chance][1]:
                map[C_chance][1] = "C"
                position = [C_chance, 1]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [C_chance, 1]:
                        map_coordinates.remove([C_chance, 1])

            T1 = random.randint(1, 100)
            if T1 < 85 and map[r][1] != "C":
                map[r][1] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 1]:
                        map_coordinates.remove([r, 1])

            T2 = random.randint(1, 100)
            if T2 < 75 and map[r][1] == "T":
                map[r][2] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 2]:
                        map_coordinates.remove([r, 2])

            T3 = random.randint(1, 101)
            if T3 < 50 and map[r][2] == "T":
                map[r][3] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 3]:
                        map_coordinates.remove([r, 3])

            # T4 = random.randint(1, 101)
            # if T4 < 40 and map[r][3] == "T":
            #     map[r][4] = "T"
            #     for e in map_coordinates:  # COORDINATE DELETION
            #         if e == [r, 3]:
            #             map_coordinates.remove([r, 3])

    elif T_chance == 2:
        for r in range(16):
            map[0][r] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [0, r]:
                    map_coordinates.remove([0, r])

            if map[1][r] == map[1][C_chance]:
                map[1][C_chance] = "C"
                position = [1, C_chance]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, C_chance]:
                        map_coordinates.remove([1, C_chance])

            T1 = random.randint(1, 101)
            if T1 < 85 and map[1][r] != "C":
                map[1][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, r]:
                        map_coordinates.remove([1, r])

            T2 = random.randint(1, 101)
            if T2 < 75 and map[1][r] == "T":
                map[2][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [2, r]:
                        map_coordinates.remove([2, r])

            T3 = random.randint(1, 101)
            if T3 < 50 and map[2][r] == "T":
                map[3][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [3, r]:
                        map_coordinates.remove([3, r])

            # T4 = random.randint(1, 101)
            # if T4 < 40 and map[3][r] == "T":
            #     map[4][r] = "T"
            #     for e in map_coordinates:  # COORDINATE DELETION
            #         if e == [4, r]:
            #             map_coordinates.remove([4, r])

    elif T_chance == 3:
        for r in range(16):
            map[15][r] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [15, r]:
                    map_coordinates.remove([15, r])

            if map[14][r] == map[14][C_chance]:
                map[14][C_chance] = "C"
                position = [14, C_chance]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, C_chance]:
                        map_coordinates.remove([14, C_chance])

            T1 = random.randint(1, 101)
            if T1 < 85 and map[14][r] != "C":
                map[14][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, r]:
                        map_coordinates.remove([14, r])

            T2 = random.randint(1, 101)
            if T2 < 75 and map[14][r] == "T":
                map[13][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [13, r]:
                        map_coordinates.remove([13, r])

            T3 = random.randint(1, 101)
            if T3 < 50 and map[13][r] == "T":
                map[12][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [12, r]:
                        map_coordinates.remove([12, r])

            # T4 = random.randint(1, 101)
            # if T4 < 40 and map[12][r] == "T":
            #     map[11][r] = "T"
            #     for e in map_coordinates:  # COORDINATE DELETION
            #         if e == [11, r]:
            #             map_coordinates.remove([1, r])

    elif T_chance == 4:
        for r in range(16):
            map[r][15] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [r, 15]:
                    map_coordinates.remove([r, 15])

            if map[r][14] == map[C_chance][14]:
                map[C_chance][14] = "C"
                position = [C_chance, 14]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [C_chance, 14]:
                        map_coordinates.remove([C_chance, 14])

            T1 = random.randint(1, 101)
            if T1 < 85 and map[r][14] != "C":
                map[r][14] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 14]:
                        map_coordinates.remove([r, 14])

            T2 = random.randint(1, 101)
            if T2 < 75 and map[r][14] == "T":
                map[r][13] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 13]:
                        map_coordinates.remove([r, 13])

            T3 = random.randint(1, 101)
            if T3 < 50 and map[r][13] == "T":
                map[r][12] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 12]:
                        map_coordinates.remove([r, 12])

            # T4 = random.randint(1, 101)
            # if T4 < 40 and map[r][12] == "T":
            #     map[r][11] = "T"
            #     for e in map_coordinates:  # COORDINATE DELETION
            #         if e == [r, 11]:
            #             map_coordinates.remove([r, 11])

def F_terrain(map):
    global map_coordinates
    global F_locations

    F_number = random.randint(2, 3)

    while F_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue
        else:
            if len(F_locations) == 0:
                map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                F_number -= 1

            elif len(F_locations) == 1:
                if abs((F_locations[0][0] + F_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                    F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    F_number -= 1

            elif len(F_locations) == 2:
                if abs((F_locations[0][0] + F_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((F_locations[1][0] + F_locations[1][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                    F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    F_number -= 1



def V_terrain(map):
    global map_coordinates
    global V_locations
    V_number = random.randint(2, 3)
    V_amount = [1, 2, 3, 4]

    while V_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 or \
                abs((P_position[0] + P_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            map[map_coordinates[x][0]][map_coordinates[x][1]] = "V"
            V_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
            V_number -= 1

            for e in V_amount:
                y = random.randint(1, 10)
                if y <= 6:
                    try:
                        y = random.randint(1, 4)
                        if y == 1:
                            map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = "V"
                            V_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])
                        elif y == 2:
                            map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = "V"
                            V_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])
                        elif y == 3:
                            map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = "V"
                            V_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])
                        elif y == 4:
                            map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = "V"
                            V_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])

                    except IndexError:
                        # if the coordinate is out of coordinates
                        pass

    print("V:")
    for e in V_locations:
        print(e, end="")
        try:
            map_coordinates.remove(e)
        except ValueError:
            # If the element is not in the list anymore
            pass
    print()


def H_terrain(map):
    global map_coordinates
    global H_locations
    H_number = random.randint(6, 7)
    H_amount = [1, 2, 3, 4, 5]

    while H_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 or \
                abs((P_position[0] + P_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            map[map_coordinates[x][0]][map_coordinates[x][1]] = "H"
            H_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
            H_number -= 1

            for e in H_amount:
                y = random.randint(1, 10)
                if y <= 4:
                    try:
                        y = random.randint(1, 4)
                        if y == 1:
                            map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])
                            map[map_coordinates[x][0] + 2][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] + 2, map_coordinates[x][1]])
                        elif y == 2:
                            map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])
                            map[map_coordinates[x][0] - 2][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] - 2, map_coordinates[x][1]])
                        elif y == 3:
                            map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])
                            map[map_coordinates[x][0]][map_coordinates[x][1] + 2] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 2])
                        elif y == 4:
                            map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])
                            map[map_coordinates[x][0]][map_coordinates[x][1] - 2] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 2])

                    except IndexError:

                        pass

    print("H:")
    for e in H_locations:
        print(e, end="")
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass
    print()


def O_terrain(map):
    global map_coordinates
    global O_locations

    O_number = random.randint(2, 3)

    while O_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue
        else:
            if len(O_locations) == 0:
                map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                O_number -= 1

            elif len(O_locations) == 1:
                if abs((O_locations[0][0] + O_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                    O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    O_number -= 1

            elif len(O_locations) == 2:
                if abs((O_locations[0][0] + O_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((O_locations[1][0] + O_locations[1][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                    O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    O_number -= 1


def P_terrain(map):
    global map_coordinates
    global P_position
    P_number = 1

    while P_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 14:
            continue
        else:
            map[map_coordinates[x][0]][map_coordinates[x][1]] = "P"
            P_position = [map_coordinates[x][0], map_coordinates[x][1]]
            map_coordinates.pop(x)
            P_number -= 1


def B_terrain(map):
    global H_locations

    B_number = random.randint(3, 4)

    while B_number > 0:
        x = len(H_locations)
        y = random.randint(0, x-1)
        z = H_locations[y]
        if map[z[0]][z[1]] == "B":
            continue
        else:
            map[z[0]][z[1]] = "B"
            B_number -= 1
            H_locations.remove(z)

    print("H after B:")
    for e in H_locations:
        print(e, end="")
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass
    print()


def S_terrain(map):
    global H_locations

    S_number = random.randint(3, 4)

    while S_number > 0:
        x = len(H_locations)
        y = random.randint(0, x-1)
        z = H_locations[y]
        if map[z[0]][z[1]] == "S":
            continue
        else:
            map[z[0]][z[1]] = "S"
            S_number -= 1
            H_locations.remove(z)

    print("H after S:")
    for e in H_locations:
        print(e, end="")
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass
    print()

def dot_J_R_terrain(map):
    global map_coordinates

    for e in map_coordinates:
        x = random.randint(1, 3)
        if x == 1:
            map[e[0]][e[1]] = "."

        elif x == 2:
            map[e[0]][e[1]] = "J"

        elif x == 3:
            map[e[0]][e[1]] = "R"

def wet_terrain(map):
    for e in V_locations:
        try:
            if map[e[0] + 1][e[1]] == "R":
                map[e[0] + 1][e[1]] = "r"
        except IndexError:
            continue

        try:
            if map[e[0] + 1][e[1] + 1] == "R":
                map[e[0] + 1][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1]] == "R":
                map[e[0] - 1][e[1]] = "r"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1] - 1] == "R":
                map[e[0] - 1][e[1] - 1] = "r"
        except IndexError:
            continue

        try:
            if map[e[0]][e[1] + 1] == "R":
                map[e[0]][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1] + 1] == "R":
                map[e[0] - 1][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if map[e[0]][e[1] - 1] == "R":
                map[e[0]][e[1] - 1] = "r"
        except IndexError:
            continue

        try:
            if map[e[0] + 1][e[1] - 1] == "R":
                map[e[0] + 1][e[1] - 1] = "r"
        except IndexError:
            continue


        try:
            if map[e[0] + 1][e[1]] == ".":
                map[e[0] + 1][e[1]] = "N"
        except IndexError:
            continue

        try:
            if map[e[0] + 1][e[1] + 1] == ".":
                map[e[0] + 1][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1]] == ".":
                map[e[0] - 1][e[1]] = "N"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1] - 1] == ".":
                map[e[0] - 1][e[1] - 1] = "N"
        except IndexError:
            continue

        try:
            if map[e[0]][e[1] + 1] == ".":
                map[e[0]][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if map[e[0] - 1][e[1] + 1] == ".":
                map[e[0] - 1][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if map[e[0] + 1][e[1] - 1] == ".":
                map[e[0] + 1][e[1] - 1] = "N"
        except IndexError:
            continue


# def display_map(map, position):
#     for row_index, row in enumerate(map):  # <- with the enumerate, I can print the indexes
#         for column_index, column in enumerate(row):  # <- with the enumerate, I can print the indexes
#
#             if row_index == position[0] and column_index == position[1]:  # If the array element = to our position
#                 print('\x1b[5;31;43m' + column + " " + '\x1b[0m', end="")  # Print the position with red and yellow
#
#             else:  # print the terrain types in different color
#                 if column in "TVG":
#                     print(colored(column + " ", "blue"), end="")
#                 elif column in "SHB":
#                     print(colored(column + " ", "grey"), end="")
#                 elif column in "JR.":
#                     print(colored(column + " ", "green"), end="")
#                 elif column in "P":
#                     print(colored(column + " ", "yellow"), end="")
#                 elif column in "Nrf":
#                     print(colored(column + " ", "cyan"), end="")
#                 elif column in "L@OF" \
#                                "":
#                     print(colored(column + " ", "red"), end="")
#                 else:
#                     print(column + " ", end="")
#         print()

# print(len(map_coordinates))
T_C_terrain(map)
P_terrain(map)
V_terrain(map)
H_terrain(map)
B_terrain(map)
F_terrain(map)
O_terrain(map)
S_terrain(map)
dot_J_R_terrain(map)
wet_terrain(map)



# display_map(map, position)
# print(map_coordinates)
# print(len(map_coordinates))