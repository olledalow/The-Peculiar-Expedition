# THIS FILE CONTAINS:
# Variables and functions for generating a new, random map for the game.


# from termcolor import colored
import random

# This is the list table for the map. 16 rows and 16 columns
game_map = [
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


map_coordinates = []  # contains the integer coordinates of the map elements in lists. : [row_index, column index]

F_locations = []  # contains the integer coordinates of the village (F) elements in lists. : [row_index, column index]

O_locations = []  # contains the integer coordinates of the Shrine (O) elements in lists. : [row_index, column index]

H_locations = []  # contains the integer coordinates of the Mountain (H) elements in lists. : [row_index, column index]

V_locations = []  # contains the integer coordinates of the Lake (V) elements in lists. : [row_index, column index]

P_position = []  # contains the integer coordinates of the Pyramid (P) element in lists. : [row_index, column index]

position = [0, 0]  # contains the integer coordinates of the current position on the map. : [row_index, column index]


for row_index, row in enumerate(game_map):  # <- with the enumerate, I get the indexes
    for column_index, column in enumerate(row):  # <- with the enumerate, I get the indexes
        map_coordinates.append([row_index, column_index])  # filling up the map_coordinates list with coordinates.


def t_c_terrain(current_map):
    t_chance = random.randint(1, 4)
    c_chance = random.randint(0, 15)
    global position
    global map_coordinates

    if t_chance == 1:
        for r in range(16):
            current_map[r][0] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [r, 0]:
                    map_coordinates.remove([r, 0])

            if current_map[r][1] == current_map[c_chance][1]:
                current_map[c_chance][1] = "C"
                position = [c_chance, 1]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [c_chance, 1]:
                        map_coordinates.remove([c_chance, 1])

            t1 = random.randint(1, 100)
            if t1 < 85 and current_map[r][1] != "C":
                current_map[r][1] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 1]:
                        map_coordinates.remove([r, 1])

            t2 = random.randint(1, 100)
            if t2 < 75 and current_map[r][1] == "T":
                current_map[r][2] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 2]:
                        map_coordinates.remove([r, 2])

            t3 = random.randint(1, 100)
            if t3 < 50 and current_map[r][2] == "T":
                current_map[r][3] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 3]:
                        map_coordinates.remove([r, 3])

    elif t_chance == 2:
        for r in range(16):
            current_map[0][r] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [0, r]:
                    map_coordinates.remove([0, r])

            if current_map[1][r] == current_map[1][c_chance]:
                current_map[1][c_chance] = "C"
                position = [1, c_chance]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, c_chance]:
                        map_coordinates.remove([1, c_chance])

            t1 = random.randint(1, 101)
            if t1 < 85 and current_map[1][r] != "C":
                current_map[1][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, r]:
                        map_coordinates.remove([1, r])

            t2 = random.randint(1, 101)
            if t2 < 75 and current_map[1][r] == "T":
                current_map[2][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [2, r]:
                        map_coordinates.remove([2, r])

            t3 = random.randint(1, 101)
            if t3 < 50 and current_map[2][r] == "T":
                current_map[3][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [3, r]:
                        map_coordinates.remove([3, r])

    elif t_chance == 3:
        for r in range(16):
            current_map[15][r] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [15, r]:
                    map_coordinates.remove([15, r])

            if current_map[14][r] == current_map[14][c_chance]:
                current_map[14][c_chance] = "C"
                position = [14, c_chance]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, c_chance]:
                        map_coordinates.remove([14, c_chance])

            t1 = random.randint(1, 101)
            if t1 < 85 and current_map[14][r] != "C":
                current_map[14][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, r]:
                        map_coordinates.remove([14, r])

            t2 = random.randint(1, 101)
            if t2 < 75 and current_map[14][r] == "T":
                current_map[13][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [13, r]:
                        map_coordinates.remove([13, r])

            t3 = random.randint(1, 101)
            if t3 < 50 and current_map[13][r] == "T":
                current_map[12][r] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [12, r]:
                        map_coordinates.remove([12, r])

    elif t_chance == 4:
        for r in range(16):
            current_map[r][15] = "T"
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [r, 15]:
                    map_coordinates.remove([r, 15])

            if current_map[r][14] == current_map[c_chance][14]:
                current_map[c_chance][14] = "C"
                position = [c_chance, 14]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [c_chance, 14]:
                        map_coordinates.remove([c_chance, 14])

            t1 = random.randint(1, 101)
            if t1 < 85 and current_map[r][14] != "C":
                current_map[r][14] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 14]:
                        map_coordinates.remove([r, 14])

            t2 = random.randint(1, 101)
            if t2 < 75 and current_map[r][14] == "T":
                current_map[r][13] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 13]:
                        map_coordinates.remove([r, 13])

            t3 = random.randint(1, 101)
            if t3 < 50 and current_map[r][13] == "T":
                current_map[r][12] = "T"
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [r, 12]:
                        map_coordinates.remove([r, 12])


def f_terrain(current_map):
    global map_coordinates
    global F_locations

    f_number = random.randint(2, 3)

    while f_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue
        else:
            if len(F_locations) == 0:
                current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                f_number -= 1

            elif len(F_locations) == 1:
                if abs((F_locations[0][0] + F_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                    F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    f_number -= 1

            elif len(F_locations) == 2:
                if abs((F_locations[0][0] + F_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((F_locations[1][0] + F_locations[1][1]) -
                               (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "F"
                    F_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    f_number -= 1


def v_terrain(current_map):
    global map_coordinates
    global V_locations
    v_number = random.randint(2, 3)

    while v_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 or \
                abs((P_position[0] + P_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "V"
            V_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
            v_number -= 1

            for e in range(4):
                y = random.randint(1, 10)
                if y <= 6:
                    try:
                        y = random.randint(1, 4)
                        if y == 1:
                            current_map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = "V"
                            V_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])
                        elif y == 2:
                            current_map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = "V"
                            V_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])
                        elif y == 3:
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = "V"
                            V_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])
                        elif y == 4:
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = "V"
                            V_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])

                    except IndexError:
                        # if the coordinate is out of coordinates
                        pass

    for e in V_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            # If the element is not in the list anymore
            pass


def h_terrain(current_map):
    global map_coordinates
    global H_locations
    h_number = random.randint(4, 5)

    while h_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 or \
                abs((P_position[0] + P_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "H"
            H_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
            h_number -= 1

            for e in range(5):
                y = random.randint(1, 10)
                if y <= 6:
                    try:
                        y = random.randint(1, 4)
                        if y == 1:
                            current_map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])
                            current_map[map_coordinates[x][0] + 2][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] + 2, map_coordinates[x][1]])
                        elif y == 2:
                            current_map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])
                            current_map[map_coordinates[x][0] - 2][map_coordinates[x][1]] = "H"
                            H_locations.append([map_coordinates[x][0] - 2, map_coordinates[x][1]])
                        elif y == 3:
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] + 2] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 2])
                        elif y == 4:
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])
                            current_map[map_coordinates[x][0]][map_coordinates[x][1] - 2] = "H"
                            H_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 2])

                    except IndexError:
                        pass

    for e in H_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass


def o_terrain(current_map):
    global map_coordinates
    global O_locations

    o_number = random.randint(2, 3)

    while o_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue
        else:
            if len(O_locations) == 0:
                current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                o_number -= 1

            elif len(O_locations) == 1:
                if abs((O_locations[0][0] + O_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                    O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    o_number -= 1

            elif len(O_locations) == 2:
                if abs((O_locations[0][0] + O_locations[0][1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((O_locations[1][0] + O_locations[1][1]) -
                               (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "O"
                    O_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    o_number -= 1


def p_terrain(current_map):
    global map_coordinates
    global P_position
    p_number = 1

    while p_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((position[0] + position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 14:
            continue
        else:
            current_map[map_coordinates[x][0]][map_coordinates[x][1]] = "P"
            P_position = [map_coordinates[x][0], map_coordinates[x][1]]
            map_coordinates.pop(x)
            p_number -= 1


def b_terrain(current_map):
    global H_locations

    b_number = random.randint(3, 4)

    while b_number > 0:
        x = len(H_locations)
        y = random.randint(0, x-1)
        z = H_locations[y]
        if current_map[z[0]][z[1]] == "B":
            continue
        else:
            current_map[z[0]][z[1]] = "B"
            b_number -= 1
            H_locations.remove(z)

    for e in H_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass


def s_terrain(current_map):
    global H_locations

    s_number = random.randint(3, 4)

    while s_number > 0:
        x = len(H_locations)
        y = random.randint(0, x-1)
        z = H_locations[y]
        if current_map[z[0]][z[1]] == "S":
            continue
        else:
            current_map[z[0]][z[1]] = "S"
            s_number -= 1
            H_locations.remove(z)

    for e in H_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass


def dot_j_r_terrain(current_map):
    global map_coordinates

    for e in map_coordinates:
        x = random.randint(1, 3)
        if x == 1:
            current_map[e[0]][e[1]] = "."

        elif x == 2:
            current_map[e[0]][e[1]] = "J"

        elif x == 3:
            current_map[e[0]][e[1]] = "R"


def wet_terrain(current_map):
    for e in V_locations:
        try:
            if current_map[e[0] + 1][e[1]] == "R":
                current_map[e[0] + 1][e[1]] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] + 1][e[1] + 1] == "R":
                current_map[e[0] + 1][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1]] == "R":
                current_map[e[0] - 1][e[1]] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1] - 1] == "R":
                current_map[e[0] - 1][e[1] - 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0]][e[1] + 1] == "R":
                current_map[e[0]][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1] + 1] == "R":
                current_map[e[0] - 1][e[1] + 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0]][e[1] - 1] == "R":
                current_map[e[0]][e[1] - 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] + 1][e[1] - 1] == "R":
                current_map[e[0] + 1][e[1] - 1] = "r"
        except IndexError:
            continue

        try:
            if current_map[e[0] + 1][e[1]] == ".":
                current_map[e[0] + 1][e[1]] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0] + 1][e[1] + 1] == ".":
                current_map[e[0] + 1][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1]] == ".":
                current_map[e[0] - 1][e[1]] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1] - 1] == ".":
                current_map[e[0] - 1][e[1] - 1] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0]][e[1] + 1] == ".":
                current_map[e[0]][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0] - 1][e[1] + 1] == ".":
                current_map[e[0] - 1][e[1] + 1] = "N"
        except IndexError:
            continue

        try:
            if current_map[e[0] + 1][e[1] - 1] == ".":
                current_map[e[0] + 1][e[1] - 1] = "N"
        except IndexError:
            continue


# def display_map(current_map, current_position):
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


# CALLING THE FUNCTIONS IN ORDER.
t_c_terrain(game_map)
p_terrain(game_map)
v_terrain(game_map)
h_terrain(game_map)
b_terrain(game_map)
f_terrain(game_map)
o_terrain(game_map)
s_terrain(game_map)
dot_j_r_terrain(game_map)
wet_terrain(game_map)


# display_map(map, position)
