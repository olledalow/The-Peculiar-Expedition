import random
from OOP_terrains import Sea, Ship, Village, Lake, Pyramid, Mountain, Meadow, Jungle, Thicket, Altar, Sanctuary, Cave
from termcolor import colored
from OOP_map_position import game_map, fog_map
from OOP_player import player
import os

######################################################################################################
#  TERMINAL ASCII MAP:


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


map_coordinates = []  # contains the integer coordinates of the map elements in lists. : [row_index, column index]
map_copy = []  # copy of map_coordinates
village_locations = []  # contains the integer coordinates of the village (F) elements in lists. :
lake_locations = []  # contains the integer coordinates of the Lake (V) elements in lists. : [row_index, column index]
pyramid_position = [0, 0]  # contains the integer coordinates of the Pyramid (P) element in lists. :
mountain_locations = []  # contains the integer coordinates of the Mountain (H) elements in lists. :
altar_locations = []  # contains the integer coordinates of the Shrine (O) elements in lists. :


def get_map_coordinates():
    for row_index, row in enumerate(game_map):  # <- with the enumerate, I get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I get the indexes
            map_coordinates.append([row_index, column_index])  # filling up the map_coordinates list with coordinates.
            map_copy.append([row_index, column_index])


def sea_ship():
    sea_side = random.randint(1, 4)
    boat = random.randint(0, 15)
    global map_coordinates

    if sea_side == 1:
        for number in range(16):
            game_map[number][0] = Sea(coordinate=(number, 0))
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [number, 0]:
                    map_coordinates.remove([number, 0])

            if game_map[number][1] == game_map[boat][1]:
                game_map[boat][1] = Ship(coordinate=(boat, 1))
                player.position = [boat, 1]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [boat, 1]:
                        map_coordinates.remove([boat, 1])

            t1 = random.randint(1, 100)
            if t1 < 85 and game_map[number][1] != Ship():
                game_map[number][1] = Sea(coordinate=(number, 1))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [number, 1]:
                        map_coordinates.remove([number, 1])

            t2 = random.randint(1, 100)
            if t2 < 75 and game_map[number][1] == Sea():
                game_map[number][2] = Sea(coordinate=(number, 2))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [number, 2]:
                        map_coordinates.remove([number, 2])

            t3 = random.randint(1, 100)
            if t3 < 50 and game_map[number][2] == Sea():
                game_map[number][3] = Sea(coordinate=(number, 3))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [number, 3]:
                        map_coordinates.remove([number, 3])

    elif sea_side == 2:
        for number in range(16):
            game_map[0][number] = Sea(coordinate=(0, number))
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [0, number]:
                    map_coordinates.remove([0, number])

            if game_map[1][number] == game_map[1][boat]:
                game_map[1][boat] = Ship(coordinate=(1, boat))
                player.position = [1, boat]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, boat]:
                        map_coordinates.remove([1, boat])

            t1 = random.randint(1, 101)
            if t1 < 85 and game_map[1][number] != Ship():
                game_map[1][number] = Sea(coordinate=(1, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [1, number]:
                        map_coordinates.remove([1, number])

            t2 = random.randint(1, 101)
            if t2 < 75 and game_map[1][number] == Sea():
                game_map[2][number] = Sea(coordinate=(2, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [2, number]:
                        map_coordinates.remove([2, number])

            t3 = random.randint(1, 101)
            if t3 < 50 and game_map[2][number] == Sea():
                game_map[3][number] = Sea(coordinate=(3, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [3, number]:
                        map_coordinates.remove([3, number])

    elif sea_side == 3:
        for number in range(16):
            game_map[15][number] = Sea(coordinate=(15, number))
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [15, number]:
                    map_coordinates.remove([15, number])

            if game_map[14][number] == game_map[14][boat]:
                game_map[14][boat] = Ship(coordinate=(14, boat))
                player.position = [14, boat]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, boat]:
                        map_coordinates.remove([14, boat])

            t1 = random.randint(1, 101)
            if t1 < 85 and game_map[14][number] != Ship():
                game_map[14][number] = Sea(coordinate=(14, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [14, number]:
                        map_coordinates.remove([14, number])

            t2 = random.randint(1, 101)
            if t2 < 75 and game_map[14][number] == Sea():
                game_map[13][number] = Sea(coordinate=(13, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [13, number]:
                        map_coordinates.remove([13, number])

            t3 = random.randint(1, 101)
            if t3 < 50 and game_map[13][number] == Sea():
                game_map[12][number] = Sea(coordinate=(12, number))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [12, number]:
                        map_coordinates.remove([12, number])

    elif sea_side == 4:
        for number in range(16):
            game_map[number][15] = Sea(coordinate=(number, 15))
            for e in map_coordinates:  # COORDINATE DELETION
                if e == [number, 15]:
                    map_coordinates.remove([number, 15])

            if game_map[number][14] == game_map[boat][14]:
                game_map[boat][14] = Ship(coordinate=(boat, 14))
                player.position = [boat, 14]
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [boat, 14]:
                        map_coordinates.remove([boat, 14])

            t1 = random.randint(1, 101)
            if t1 < 85 and game_map[number][14] != Ship():
                game_map[number][14] = Sea(coordinate=(number, 14))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [number, 14]:
                        map_coordinates.remove([number, 14])

            t2 = random.randint(1, 101)
            if t2 < 75 and game_map[number][14] == Sea():
                game_map[number][13] = Sea(coordinate=(number, 13))
                for e in map_coordinates:  # COORDINATE DELETIONcoordinate=(boat, 1)
                    if e == [number, 13]:
                        map_coordinates.remove([number, 13])

            t3 = random.randint(1, 101)
            if t3 < 50 and game_map[number][13] == Sea():
                game_map[number][12] = Sea(coordinate=(number, 12))
                for e in map_coordinates:  # COORDINATE DELETION
                    if e == [number, 12]:
                        map_coordinates.remove([number, 12])


def village():
    global map_coordinates
    global village_locations

    village_number = random.randint(2, 3)

    while village_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((player.position[0] + player.position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue
        else:
            if len(village_locations) == 0:
                game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Village(coordinate=(map_coordinates[x][0],
                                                                                             map_coordinates[x][1]))
                village_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                village_number -= 1

            elif len(village_locations) == 1:
                if abs((village_locations[0][0] + village_locations[0][1]) -
                       (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Village(coordinate=(map_coordinates[x][0],
                                                                                                 map_coordinates[x][1]))
                    village_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    village_number -= 1

            elif len(village_locations) == 2:
                if abs((village_locations[0][0] + village_locations[0][1]) -
                       (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((village_locations[1][0] + village_locations[1][1]) -
                               (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue
                else:
                    game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Village(coordinate=(map_coordinates[x][0],
                                                                                                 map_coordinates[x][1]))
                    village_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    village_number -= 1


def lake():
    global map_coordinates
    global lake_locations
    lake_number = random.randint(2, 3)

    while lake_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((player.position[0] + player.position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6 or \
                abs((pyramid_position[0] + pyramid_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            if 15 >= map_coordinates[x][0] >= 0 and 15 >= map_coordinates[x][1] >= 0:
                game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Lake(coordinate=(map_coordinates[x][0],
                                                                                          map_coordinates[x][1]))
                lake_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                lake_number -= 1

                for e in range(4):
                    if random.randint(1, 10) <= 6:
                        try:
                            placement = random.randint(1, 4)
                            if placement == 1:
                                if 15 >= map_coordinates[x][0]+1 >= 0:
                                    game_map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = \
                                        Lake(coordinate=(map_coordinates[x][0]+1, map_coordinates[x][1]))
                                    lake_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])
                            elif placement == 2:
                                if 15 >= map_coordinates[x][0] - 1 >= 0:
                                    game_map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = \
                                        Lake(coordinate=(map_coordinates[x][0]-1, map_coordinates[x][1]))
                                    lake_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])
                            elif placement == 3:
                                if 15 >= map_coordinates[x][1] + 1 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = \
                                        Lake(coordinate=(map_coordinates[x][0], map_coordinates[x][1]+1))
                                    lake_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])
                            elif placement == 4:
                                if 15 >= map_coordinates[x][1] - 1 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = \
                                        Lake(coordinate=(map_coordinates[x][0], map_coordinates[x][1]-1))
                                    lake_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])

                        except IndexError:
                            # if the coordinate is out of coordinates
                            pass

    for e in lake_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            # If the element is not in the list anymore
            pass


def pyramid():
    global map_coordinates
    global pyramid_position
    p_number = 1

    while p_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((player.position[0] + player.position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 14:
            continue
        else:
            game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Pyramid(coordinate=(map_coordinates[x][0],
                                                                                         map_coordinates[x][1]))
            pyramid_position = [map_coordinates[x][0], map_coordinates[x][1]]
            map_coordinates.pop(x)
            p_number -= 1


def mountain():
    global map_coordinates
    global mountain_locations
    mountain_number = random.randint(5, 6)

    while mountain_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((player.position[0] + player.position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 7 or \
                abs((pyramid_position[0] + pyramid_position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
            continue
        else:
            if (15 >= map_coordinates[x][0] >= 0) and (15 >= map_coordinates[x][1] >= 0):
                game_map[map_coordinates[x][0]][map_coordinates[x][1]] = Mountain(coordinate=(map_coordinates[x][0],
                                                                                  map_coordinates[x][1]))
                mountain_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                mountain_number -= 1

                for e in range(5):
                    if random.randint(1, 10) <= 4:
                        try:
                            placement = random.randint(1, 4)
                            if placement == 1:
                                if 15 >= map_coordinates[x][0]+1 >= 0:
                                    game_map[map_coordinates[x][0] + 1][map_coordinates[x][1]] = \
                                        Mountain(coordinate=(map_coordinates[x][0]+1, map_coordinates[x][1]))

                                    mountain_locations.append([map_coordinates[x][0] + 1, map_coordinates[x][1]])

                                if 15 >= map_coordinates[x][0]+2 >= 0:
                                    game_map[map_coordinates[x][0] + 2][map_coordinates[x][1]] = \
                                        Mountain(coordinate=(map_coordinates[x][0]+2, map_coordinates[x][1]))

                                    mountain_locations.append([map_coordinates[x][0] + 2, map_coordinates[x][1]])

                            elif placement == 2:
                                if 15 >= map_coordinates[x][0]-1 >= 0:
                                    game_map[map_coordinates[x][0] - 1][map_coordinates[x][1]] = \
                                        Mountain(coordinate=(map_coordinates[x][0]-1, map_coordinates[x][1]))

                                    mountain_locations.append([map_coordinates[x][0] - 1, map_coordinates[x][1]])

                                if 15 >= map_coordinates[x][0]-2 >= 0:
                                    game_map[map_coordinates[x][0] - 2][map_coordinates[x][1]] = \
                                        Mountain(coordinate=(map_coordinates[x][0]-2, map_coordinates[x][1]))

                                    mountain_locations.append([map_coordinates[x][0] - 2, map_coordinates[x][1]])

                            elif placement == 3:
                                if 15 >= map_coordinates[x][1]+1 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] + 1] = \
                                        Mountain(coordinate=(map_coordinates[x][0], map_coordinates[x][1]+1))

                                    mountain_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 1])

                                if 15 >= map_coordinates[x][1]+2 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] + 2] = \
                                        Mountain(coordinate=(map_coordinates[x][0], map_coordinates[x][1]+2))

                                    mountain_locations.append([map_coordinates[x][0], map_coordinates[x][1] + 2])

                            elif placement == 4:
                                if 15 >= map_coordinates[x][1]-1 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] - 1] = \
                                        Mountain(coordinate=(map_coordinates[x][0], map_coordinates[x][1]-1))

                                    mountain_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 1])

                                if 15 >= map_coordinates[x][1]-2 >= 0:
                                    game_map[map_coordinates[x][0]][map_coordinates[x][1] - 2] = \
                                        Mountain(coordinate=(map_coordinates[x][0], map_coordinates[x][1]-2))

                                    mountain_locations.append([map_coordinates[x][0], map_coordinates[x][1] - 2])

                        except IndexError:
                            pass

    for e in mountain_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass


def meadow_jungle_thicket():
    global map_coordinates

    for e in map_coordinates:
        choice = random.randint(1, 3)
        if choice == 1:
            game_map[e[0]][e[1]] = Meadow(coordinate=(e[0], e[1]))

        elif choice == 2:
            game_map[e[0]][e[1]] = Jungle(coordinate=(e[0], e[1]))

        elif choice == 3:
            game_map[e[0]][e[1]] = Thicket(coordinate=(e[0], e[1]))


def wet_terrain():
    for e in lake_locations:
        try:
            if game_map[e[0] + 1][e[1]].icon in "RJ.":
                game_map[e[0] + 1][e[1]].wet = True
                game_map[e[0] + 1][e[1]].if_wet()
        except IndexError:
            continue

        try:
            if game_map[e[0] + 1][e[1] + 1].icon in "RJ.":
                game_map[e[0] + 1][e[1] + 1].wet = True
                game_map[e[0] + 1][e[1] + 1].if_wet()
        except IndexError:
            continue

        try:
            if e[0] > 0 and game_map[e[0] - 1][e[1]].icon in "RJ.":
                game_map[e[0] - 1][e[1]].wet = True
                game_map[e[0] - 1][e[1]].if_wet()
        except IndexError:
            continue

        try:
            if e[0] > 0 and e[1] > 0 and game_map[e[0] - 1][e[1] - 1].icon in "RJ.":
                game_map[e[0] - 1][e[1] - 1].wet = True
                game_map[e[0] - 1][e[1] - 1].if_wet()
        except IndexError:
            continue

        try:
            if game_map[e[0]][e[1] + 1].icon in "RJ.":
                game_map[e[0]][e[1] + 1].wet = True
                game_map[e[0]][e[1] + 1].if_wet()
        except IndexError:
            continue

        try:
            if e[0] > 0 and game_map[e[0] - 1][e[1] + 1].icon in "RJ.":
                game_map[e[0] - 1][e[1] + 1].wet = True
                game_map[e[0] - 1][e[1] + 1].if_wet()
        except IndexError:
            continue

        try:
            if e[1] > 0 and game_map[e[0]][e[1] - 1].icon in "RJ.":
                game_map[e[0]][e[1] - 1].wet = True
                game_map[e[0]][e[1] - 1].if_wet()
        except IndexError:
            continue

        try:
            if e[1] > 0 and game_map[e[0] + 1][e[1] - 1].icon in "RJ.":
                game_map[e[0] + 1][e[1] - 1].wet = True
                game_map[e[0] + 1][e[1] - 1].if_wet()
        except IndexError:
            continue


def altar():
    global map_coordinates
    global altar_locations

    altar_number = random.randint(2, 3)

    while altar_number > 0:
        x = random.randint(0, len(map_coordinates) - 1)
        if abs((player.position[0] + player.position[1]) - (map_coordinates[x][0] + map_coordinates[x][1])) < 4:
            continue

        else:
            if len(altar_locations) == 0:
                game_map[map_coordinates[x][0]][map_coordinates[x][1]] = \
                    Altar(coordinate=(map_coordinates[x][0], map_coordinates[x][1]))
                altar_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                map_coordinates.pop(x)
                altar_number -= 1

            elif len(altar_locations) == 1:
                if abs((altar_locations[0][0] + altar_locations[0][1]) -
                       (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue

                else:
                    game_map[map_coordinates[x][0]][map_coordinates[x][1]] = \
                        Altar(coordinate=(map_coordinates[x][0], map_coordinates[x][1]))
                    altar_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    altar_number -= 1

            elif len(altar_locations) == 2:
                if abs((altar_locations[0][0] + altar_locations[0][1]) -
                       (map_coordinates[x][0] + map_coordinates[x][1])) < 6 \
                        or abs((altar_locations[1][0] + altar_locations[1][1]) -
                               (map_coordinates[x][0] + map_coordinates[x][1])) < 6:
                    continue

                else:
                    game_map[map_coordinates[x][0]][map_coordinates[x][1]] = \
                        Altar(coordinate=(map_coordinates[x][0], map_coordinates[x][1]))
                    altar_locations.append([map_coordinates[x][0], map_coordinates[x][1]])
                    map_coordinates.pop(x)
                    altar_number -= 1


def sanctuary():
    global mountain_locations

    sanctuary_number = random.randint(3, 4)

    while sanctuary_number > 0:
        x = len(mountain_locations)
        y = random.randint(0, x-1)
        z = mountain_locations[y]
        if game_map[z[0]][z[1]] == Sanctuary():
            continue
        else:
            game_map[z[0]][z[1]] = Sanctuary(coordinate=(z[0], z[1]))
            sanctuary_number -= 1
            mountain_locations.remove(z)

    for e in mountain_locations:
        try:
            map_coordinates.remove(e)
            pass
        except ValueError:
            pass

def cave():
    global mountain_locations

    cave_number = random.randint(3, 4)

    while cave_number > 0:
        x = len(mountain_locations)
        y = random.randint(0, x-1)
        z = mountain_locations[y]
        if game_map[z[0]][z[1]] == Cave():
            continue
        else:
            game_map[z[0]][z[1]] = Cave(coordinate=(z[0], z[1]))
            cave_number -= 1
            mountain_locations.remove(z)

    for e in mountain_locations:
        try:
            map_coordinates.remove(e)
        except ValueError:
            pass


def fog():
    fog_map[player.position[0]][player.position[1]] = "!"

    for num1 in player.sight:
        for num2 in player.sight:

            try:
                fog_map[player.position[0] + num1][player.position[1] + num2] = "!"
            except IndexError:
                pass

            try:
                fog_map[player.position[0] + num1][abs(player.position[1] - num2)] = "!"
            except IndexError:
                pass

            try:
                fog_map[abs(player.position[0] - num1)][player.position[1] + num2] = "!"
            except IndexError:
                pass

            try:
                fog_map[abs(player.position[0] - num1)][abs(player.position[1] - num2)] = "!"
            except IndexError:
                pass


def display_map():
    # Displays the map with the current location after every move
    # fog(fog_map)
    # print("\n" * 30)
    # clear_screen()
    # fog()
    for ROW_INDEX, ROW in enumerate(game_map):  # <- with the enumerate, I can print the indexes
        for COLUMN_INDEX, COLUMN in enumerate(ROW):  # <- with the enumerate, I can print the indexes
            if ROW_INDEX == player.position[0] and COLUMN_INDEX == player.position[1]:
                print('\x1b[5;31;43m' + COLUMN.icon + " " + '\x1b[0m', end="")

            else:
                if fog_map[ROW_INDEX][COLUMN_INDEX] == "!":
                    if COLUMN.icon in "TVG":
                        print(colored(COLUMN.icon + " ", "blue"), end="")
                    if COLUMN.icon in "L@C":
                        print(colored(COLUMN.icon + " ", "red"), end="")
                    if COLUMN.icon == "P":
                        print(colored(COLUMN.icon + " ", "yellow"), end="")
                    if COLUMN.icon in "HSBFO":
                        print(colored(COLUMN.icon + " ", "white"), end="")
                    if COLUMN.icon in ".JR":
                        if COLUMN.wet:
                            print(colored(COLUMN.icon + " ", "cyan"), end="")
                        else:
                            print(colored(COLUMN.icon + " ", "green"), end="")
                else:
                    if COLUMN.icon in "TVG":
                        print("?" + " ", end="")
                    if COLUMN.icon in "SHB":
                        print("?" + " ", end="")
                    if COLUMN.icon in "JR.":
                        print("?" + " ", end="")
                    if COLUMN.icon in "P":
                        print("?" + " ", end="")
                    if COLUMN.icon in "Nrf":
                        print("?" + " ", end="")
                    if COLUMN.icon in "L@":
                        print("?" + " ", end="")
                    if COLUMN.icon in "FOC":
                        print("?" + " ", end="")
        print()


def generate_map():
    get_map_coordinates()
    sea_ship()
    pyramid()
    lake()
    mountain()
    village()
    altar()
    sanctuary()
    cave()
    meadow_jungle_thicket()
    wet_terrain()


def reset_map():
    global map_coordinates, village_locations, lake_locations, pyramid_position, mountain_locations, altar_locations
    map_coordinates = []  # contains the integer coordinates of the map elements in lists. : [row_index, column index]
    village_locations = []  # contains the integer coordinates of the village (F) elements in lists. :
    lake_locations = []  # integer coordinates of the Lake (V) elements in lists. : [row_index, column index]
    pyramid_position = [0, 0]  # contains the integer coordinates of the Pyramid (P) element in lists. :
    mountain_locations = []  # contains the integer coordinates of the Mountain (H) elements in lists. :
    altar_locations = []  # contains the integer coordinates of the Shrine (O) elements in lists. :


def reset_fog():
    coordinates = range(16)
    for num1 in coordinates:
        for num2 in coordinates:
            fog_map[num1][num2] = "?"

generate_map()
