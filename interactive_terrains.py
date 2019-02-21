# THIS FILE CONTAINS:
# Variables essential for the functions in this file
# TERRAIN Functions for terrain types that have an interactive interface, and FEATURE functions that are called in the
# terrain type functions if they meet the requirements.


import random

from OOP_village import company, donkey_out, scout_out, shaman_out, soldier_out
from OOP_player import player


from GAME_displays import display_curse_geyser
from GAME_displays import display_curse_volcano
from GAME_displays import display_shrine_treasure
from GAME_displays import display_shrine
# from GAME_displays import display_shrine_chest
# from GAME_displays import display_shrine_doll
# from GAME_displays import display_shrine_room
# from GAME_displays import display_shrine_runes
# from GAME_displays import display_shrine_door
# from GAME_displays import display_rest
# from GAME_displays import display_merchant
# from GAME_displays import display_village
# from GAME_displays import display_crew
# from GAME_displays import display_bag


o_coordinate = []  # coordinates of the Shrine we are currently in.
L_coordinate = []  # types and coordinates of terrains that are being changed to lava (L)
Volcano_coordinate = []  # coordinates of H-s being changed to volcanos (@)
S_coordinate = []  # contains the coordinates of already visited Shrines
B_coordinate = []  # contains the coordinates of already visited Caves


#  TERRAINS: ##########################################################################################################


def o(current_energy, current_map, current_position, current_inventory, def_slot, four_steps, moves):
    # Shrine: lootable treasure, 80% chance on catastrophe
    display_shrine()

    for e in o_coordinate:
        if current_position == e:
            input("You have already cleared this Shrine...")
            current_energy -= 0
            current_slot = def_slot()
            return current_energy, current_slot

    if current_position not in o_coordinate:
        o_coordinate.append(current_position.copy())
    input("What do you do? loot the chest and face the consequences, or run away and never look back?")
    loot = input("type 'loot' or hit enter you run away... ")
    if loot == "loot":
        display_shrine_treasure()

        if "treasure" in current_inventory:  # adds a treasure to inventory.
            current_inventory["treasure"][0] += 1
        else:
            current_inventory["treasure"] = [1, 100, 0]

        curse_chance = random.randint(1, 101)  # 80% chance on a curse. If curse happens:
        if curse_chance <= 100:
            current_energy -= 15

            input("The chanthing stopped... but the earthquake got stronger... You looked up and...")
            x = random.randint(1, 101)  # 35% chance on volcano curse, 65% chance on geyser curse
            if x <= 100:
                display_curse_volcano()

                input("'What have I done?' You are thinking... but It's too late for regrets now...")
                four_steps.append(moves)  # save current move number, so after 4 steps it can be used again.
                curse_volcano(current_map, current_position)
                current_slot = def_slot()  # to check the item number (because of 1 plus treasure)
                return current_energy, current_slot
            else:
                display_curse_geyser()

                input("'What have I done?' You are thinking... but It's too late for regrets now...")
                curse_geyser(current_map, current_position)
                current_slot = def_slot()  # to check the item number (because of 1 plus treasure)
                return current_energy, current_slot
        else:

            input("Next time I might not be this lucky...")
            current_slot = def_slot()
            current_energy -= 0
            return current_energy, current_slot

    else:
        current_slot = def_slot()
        current_energy -= 0
        return current_energy, current_slot


def s(current_energy, current_map, current_position, current_inventory, def_slot, moves, four_steps,
      current_companions, currently_injured, injureds_list):
    # Sanctuary: lootable treasure, if rope in inventory its harmless, else 50% chance on catastrophe and 20 on curse

    for e in S_coordinate:
        if current_position == e:
            input("You have already cleared this Sanctuary...")
            current_energy -= 0
            current_slot = def_slot()
            return current_energy, current_slot, currently_injured, injureds_list

    if current_position not in S_coordinate:
        S_coordinate.append(current_position.copy())

    if "treasure" in current_inventory:  # adds a treasure to inventory.
        current_inventory["treasure"][0] += 1
    else:
        current_inventory["treasure"] = [1, 100, 0]

    if "rope" in current_inventory:
        current_inventory["rope"][0] -= 1
        if current_inventory["rope"][0] == 0:
            current_inventory.pop("rope", None)
        current_energy -= 0
        current_slot = def_slot()
        return current_energy, current_slot, currently_injured, injureds_list
    else:
        bad_luck = random.randint(1, 101)
        if bad_luck <= 100:
            input("Catastrophe will happen!")
            current_energy, currently_injured, injureds_list = catastrophe(current_energy, current_companions,
                                                                           currently_injured, injureds_list,
                                                                           current_inventory)
            current_slot = def_slot()
            return current_energy, current_slot, currently_injured, injureds_list

        elif 51 <= bad_luck <= 70:
            input("Curse will happen!")
            curse_chance = random.randint(1, 101)
            if curse_chance <= 65:
                display_curse_geyser()
                curse_geyser(current_map, current_position)
                current_energy -= 0
                current_slot = def_slot()
                return current_energy, current_slot, currently_injured, injureds_list
            else:
                four_steps.append(moves)
                display_curse_volcano()
                curse_volcano(current_map, current_position)
                current_energy -= 0
                current_slot = def_slot()
                return current_energy, current_slot, currently_injured, injureds_list
        else:
            input("Nothing will happen!")
            current_slot = def_slot()
            current_energy -= 0
            return current_energy, current_slot, currently_injured, injureds_list


def b(current_energy, current_position, current_inventory, def_slot, injureds_list, current_companions,
      currently_injured):
    # lootable treasure, if torch in inventory its harmless, else 65% chance on catastrophe
    for e in B_coordinate:
        if current_position == e:
            input("You have already been in this Cave...")
            current_energy -= 0
            current_slot = def_slot()
            return current_energy, current_slot, currently_injured, injureds_list

    if current_position not in B_coordinate:
        B_coordinate.append(current_position.copy())

    if "treasure" in current_inventory:  # adds a treasure to inventory.
        current_inventory["treasure"][0] += 1
    else:
        current_inventory["treasure"] = [1, 100, 0]

    if "torch" in current_inventory:
        current_inventory["torch"][0] -= 1
        if current_inventory["torch"][0] == 0:
            current_inventory.pop("torch", None)
        current_energy -= 0
        current_slot = def_slot()
        return current_energy, current_slot, currently_injured, injureds_list
    else:
        catastrophe_chance = random.randint(1, 101)
        if catastrophe_chance <= 65:
            input('CATASTROOOPHE')  # not here
            current_energy, currently_injured, injureds_list = catastrophe(current_energy, current_companions,
                                                                           currently_injured, injureds_list,
                                                                           current_inventory)
            current_slot = def_slot()
            return current_energy, current_slot, currently_injured, injureds_list
        else:
            input("you got lucky! catastrophe could have happened!")
            current_energy -= 0
            current_slot = def_slot()
            return current_energy, current_slot, currently_injured, injureds_list


#  FEATURES ###########################################################################################################


def curse_volcano(current_map, current_position):
    # turn the closest mountain to volcano, and the neighbour terrains to lava
    h_coordinates = []  # Actual coordinates of H-s, like : [3, 5]
    steps = []  # Number of steps between position and H, like: 5

    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == "H":
                h_coordinates.append([row_index, column_index])
                steps.append(sum([abs(current_position[0] - row_index), (abs(current_position[1] - column_index))]))

    h = h_coordinates[steps.index(min(steps))]  # coordinate of the closest H to our position

    current_map[h[0]][h[1]] = "@"  # Change the closest H to our position to @ (volcano)
    Volcano_coordinate.append([current_map.index(current_map[h[0]]), current_map.index(current_map[h[1]])])

    if h[0] - 1 > 0 and current_map[h[0] - 1][h[1]] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] - 1][h[1]],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1]])])
        current_map[h[0] - 1][h[1]] = "L"

    if h[0] + 1 < 15 and current_map[h[0] + 1][h[1]] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] + 1][h[1]],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1]])])
        current_map[h[0] + 1][h[1]] = "L"

    if h[1] - 1 > 0 and current_map[h[0]][h[1] - 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0]][h[1] - 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0]][h[1] - 1] = "L"

    if h[1] + 1 < 15 and current_map[h[0]][h[1] + 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0]][h[1] + 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0]][h[1] + 1] = "L"

    if h[0] - 1 > 0 and h[1] - 1 > 0 and current_map[h[0] - 1][h[1] - 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] - 1][h[1] - 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0] - 1][h[1] - 1] = "L"

    if h[0] + 1 < 15 and h[1] + 1 < 15 and current_map[h[0] + 1][h[1] + 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] + 1][h[1] + 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0] + 1][h[1] + 1] = "L"

    if h[0] - 1 > 0 and h[1] + 1 < 15 and current_map[h[0] - 1][h[1] + 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] - 1][h[1] + 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0] - 1][h[1] + 1] = "L"

    if h[0] + 1 < 15 and h[1] - 1 > 0 and current_map[h[0] + 1][h[1] - 1] not in "TVSHOFB":
        L_coordinate.append([current_map[h[0] + 1][h[1] - 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0] + 1][h[1] - 1] = "L"


def volcano_back(current_map):
    # turn back the lava terrain to plain ground
    for e in L_coordinate:
        current_map[e[1]][e[2]] = "."


def curse_geyser(current_map, current_position):
    # turns lakes into geysers, and turns neighboring terrain wet.
    water_coordinates = []  # Actual coordinates of V-s, las list coordinates [x,y]
    steps = []  # Number of steps between position and V, as int

    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == "V":
                water_coordinates.append([row_index, column_index])
                steps.append(sum([abs(current_position[0] - row_index), (abs(current_position[1] - column_index))]))

    w = water_coordinates[steps.index(min(steps))]  # coordinate of the closest V to our position

    if current_position not in o_coordinate:
        o_coordinate.append(current_position.copy())

    current_map[w[0]][w[1]] = "G"  # change the closest V to our position to G

    coordinate_number = (0, 1, 2)

    for num1 in coordinate_number:
        for num2 in coordinate_number:
            try:
                if current_map[w[0] + num1][w[1] + num2] not in "TVSHO":
                    if current_map[w[0] + num1][w[1] + num2] == ".":
                        current_map[w[0] + num1][w[1] + num2] = "N"
                    elif current_map[w[0] + num1][w[1] + num2] == "R":
                        current_map[w[0] + num1][w[1] + num2] = "r"
                    elif current_map[w[0] + num1][w[1] + num2] == "F":
                        current_map[w[0] + num1][w[1] + num2] = "f"

                if current_map[w[0] + num1][w[1] - num2] not in "TVSHO":
                    if current_map[w[0] + num1][w[1] - num2] == ".":
                        current_map[w[0] + num1][w[1] - num2] = "N"
                    elif current_map[w[0] + num1][w[1] - num2] == "R":
                        current_map[w[0] + num1][w[1] - num2] = "r"
                    elif current_map[w[0] + num1][w[1] - num2] == "F":
                        current_map[w[0] + num1][w[1] - num2] = "f"

                if current_map[w[0] - num1][w[1] + num2] not in "TVSHO":
                    if current_map[w[0] - num1][w[1] + num2] == ".":
                        current_map[w[0] - num1][w[1] + num2] = "N"
                    elif current_map[w[0] - num1][w[1] + num2] == "R":
                        current_map[w[0] - num1][w[1] + num2] = "r"
                    elif current_map[w[0] - num1][w[1] + num2] == "F":
                        current_map[w[0] - num1][w[1] + num2] = "f"

                if current_map[w[0] - num1][w[1] - num2] not in "TVSHO":
                    if current_map[w[0] - num1][w[1] - num2] == ".":
                        current_map[w[0] - num1][w[1] - num2] = "N"
                    elif current_map[w[0] - num1][w[1] - num2] == "R":
                        current_map[w[0] - num1][w[1] - num2] = "r"
                    elif current_map[w[0] - num1][w[1] - num2] == "F":
                        current_map[w[0] - num1][w[1] - num2] = "f"

            except IndexError:
                continue


def catastrophe(current_energy, current_companions, currently_injured, injureds_list, current_inventory):
    # 70% chance on 35 energy loss, 10% chance on injury, 20% that a companion immediately leaves the group (traitor).

    x = random.randint(1, 101)

    if x <= 1:

        input("You lost 35 energy!")
        current_energy -= 35
        return current_energy, currently_injured, injureds_list

    elif 2 < x <= 90:
        if len(current_companions) != 0:
            currently_injured = True
            y = random.choice(list(current_companions))
            injureds_list[y] = 0
            input("Oh no! Your " + y + " companion got injured... There is a chance he can't keep up in the future...")
            current_energy -= 0
            pass

    else:
        if len(current_companions) != 0:
            traitor(current_companions, current_inventory)
            current_energy -= 0
            return current_energy, currently_injured, injureds_list
    current_energy -= 0
    return current_energy, currently_injured, injureds_list


def traitor(current_companions, current_inventory):
    # a companion leaves the group and steals an item from inventory
    y = random.choice(list(current_companions))
    z = random.choice(list(current_inventory))
    if z == "treasure":
        input("Your " + y + " companion betrayed you! He took the " + z + " and run away with it...")
    else:
        input("Your " + y + " companion betrayed you! He left your group and stole 1 " + z + " from you backpack...")
    current_companions.pop(y, None)
    current_inventory[z][0] -= 1
    if current_inventory[z][0] == 0:
        current_inventory.pop(z, None)
        company(current_companions)


injured_list = {}
injured = False


def injury(current_companions, current_inventory, max_slots, scout_sight):
    #  one companion from the injured list leaves the group. if there is no more companion in the injured list, it sets
    #  the injured variable value to False.
    y = random.choice(list(injured_list))
    input("Your " + y + " companion got enough of your journeys! He leaves the group because of his injuries.")
    del player.companions[y]
    injured_list.pop(y, None)
    companion_cost = company(current_companions)

    if y == "shaman":
        shaman_out(current_inventory)

    if y == "wise":
        pass

    if y == "scout":
        scout_out(scout_sight)

    if y == "donkey":
        max_slots = donkey_out(max_slots)

    if y == "soldier":
        soldier_out(current_inventory)

    if len(injured_list) != 0:
        currently_injured = True
        return companion_cost, currently_injured, max_slots
    else:
        currently_injured = False
        return companion_cost, currently_injured, max_slots
