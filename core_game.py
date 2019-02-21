# THIS FILE CONTAINS:
# Variables that are essential for almost all the functions in and outside of this file
# Functions responsible for displaying the map, the inventory and for moving on the map (looping the game)
# Function calls for starting the program


from termcolor import colored
import random

from random_map_generator import game_map, position, fog_map, fog, sight

from passive_terrains import dot, r, r_wet, dot_wet, j
from interactive_terrains import o, s, b, volcano_back, injured_list, injured, injury
from OOP_player import player
from OOP_terrains import Village
# from OOP_village import current_vendor
# from GAME_displays import display_merchant


EC = 3  # ENERGY COST: game difficulty. minimal energy cost for a move.
moves = 0  # number of moves the player made in the game
four_steps = []  # saves the current moves number for later use (after 4 steps its used)
company_cost = 1  # initial multiplier for movement cost. it increases with more companions
slots_cost = 1  # initial multiplier for movement cost. it increases if the player has more items than allowed slots.
allowed_slots = 8  # amount of items the player can carry without increasing the energy cost of steps

# ITEMS: [NAME/AMOUNT/COST/ATTRIBUTE]
inventory = {  # starting items in player's inventory
    "glassball": [1, 100, 0],
    "whiskey": [1, 50, 20],
    "fruit": [5, 45, 15],
    "meat": [5, 60, 25],
    "chocolate": [5, 50, 20],
    "medicine": [5, 50, 20],
    "torch": [2, 40, 0]
}


companions = {  # will contain the companions the player hires
}


# def display_inventory(current_energy):
#     # display inventory, shows free slots or excess item number, prints energy bar,
#     # allow the player to consume food or drink to restore energy
#     display_bag()
#     if len(inventory) > allowed_slots:
#         print(str(len(inventory)) + " out of " + str(allowed_slots) + ". You are carrying" +
#               str(len(inventory) - allowed_slots) + "extra items in your hand.")
#     else:
#         print(str(len(inventory)) + " out of " + str(allowed_slots) + ". You have " +
#               str(allowed_slots - len(inventory)) + " free slots left.")
#     for e in inventory:
#         if inventory[e][0] != 0:
#             print(e, inventory[e][0])  # print inventory elements if have any of it.
#
#     while True:
#         print("     min _________________________ max")
#         print("energy: |" + colored(str(int(current_energy / 4) * u"\u25A0"), "green"))
#
#         if "soldier" in companions:
#             print("Because you have a Soldier companion, you get extra 20% energy when drinking whiskey")
#         if "shaman" in companions:
#             print("Because you have a Shaman companion, you get extra 20% energy when using medicine")
#
#         x = input("choose food or drink to consume for energy or press 'ENTER' to exit: \n")
#         if x == "fruit" or x == "whiskey" or x == "medicine" or x == "chocolate" or x == "meat":
#             for e in list(inventory):
#                 if x == e:
#                     try:
#                         y = int(input("How many would you like to eat or drink? "))
#                         if inventory[e][0] - y > -1:
#                             if current_energy + (inventory[e][2] * y) > 100:
#                                 current_energy = 100
#                                 inventory[e][0] -= y
#                                 if inventory[e][0] == 0:
#                                     inventory.pop(e, None)
#
#                             else:
#                                 current_energy += (inventory[e][2] * y)
#                                 inventory[e][0] -= y
#                                 if inventory[e][0] == 0:
#                                     inventory.pop(e, None)
#
#                         else:
#                             print("You don't have that much...")
#                     except ValueError:
#                         input("That is not a valid number!")
#                         pass
#         else:
#             slot_cost = slots()
#             current_energy -= 0
#             return current_energy, slot_cost
#

def slots():
    # If there is more items in inventory than allowed, moves cost more energy.
    if len(inventory) > allowed_slots:
        slot_cost = ((len(inventory) - allowed_slots) * 0.2) + 1
        return slot_cost
    else:
        slot_cost = 1
        return slot_cost


def display_map(current_map, current_position):
    # Displays the map with the current location after every move
    # fog(fog_map)
    print("\n" * 30)
    fog()
    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can print the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can print the indexes

            if row_index == current_position[0] and column_index == current_position[1]:
                # If the array element = to our position
                print('\x1b[5;31;43m' + column + " " + '\x1b[0m', end="")  # Print the position with red and yellow

            else:  # print the terrain types in different color
                if fog_map[row_index][column_index] == "!":
                    if column in "TVG":
                        print(colored(column + " ", "blue"), end="")
                    if column in "SHB":
                        print(colored(column + " ", "grey"), end="")
                    if column in "JR.":
                        print(colored(column + " ", "green"), end="")
                    if column in "P":
                        print(colored(column + " ", "yellow"), end="")
                    if column in "Nrf":
                        print(colored(column + " ", "cyan"), end="")
                    if column in "L@":
                        print(colored(column + " ", "red"), end="")
                    if column in "FOC":
                        print(column + " ", end="")
                else:
                    if column in "TVG":
                        print("?" + " ", end="")
                    if column in "SHB":
                        print("?" + " ", end="")
                    if column in "JR.":
                        print("?" + " ", end="")
                    if column in "P":
                        print("?" + " ", end="")
                    if column in "Nrf":
                        print("?" + " ", end="")
                    if column in "L@":
                        print("?" + " ", end="")
                    if column in "FOC":
                        print("?" + " ", end="")
        print()


def display_oldmap(current_map, current_position):
    # Displays the map with the current location after every move
    print("\n" * 30)
    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can print the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can print the indexes

            if row_index == current_position[0] and column_index == current_position[1]:
                # If the array element = to our position
                print('\x1b[5;31;43m' + column + " " + '\x1b[0m', end="")  # Print the position with red and yellow

            else:  # print the terrain types in different color
                if column in "TVG":
                    print(colored(column + " ", "blue"), end="")
                elif column in "SHB":
                    print(colored(column + " ", "grey"), end="")
                elif column in "JR.":
                    print(colored(column + " ", "green"), end="")
                elif column in "P":
                    print(colored(column + " ", "yellow"), end="")
                elif column in "Nrf":
                    print(colored(column + " ", "cyan"), end="")
                elif column in "L@":
                    print(colored(column + " ", "red"), end="")
                else:
                    print(column + " ", end="")
        print()


def move(current_map, current_energy, current_gold, current_position, current_companions, current_inventory,
         companions_cost, move_cost, def_slot, currently_injured, injureds_list, scout_sight):

    global moves, slots_cost, company_cost, four_steps, allowed_slots
    while current_energy > 0:

        moving = input("move with 'w a s d', check your bag with 'b', see your companions with 'c'. ")
        if len(inventory) > 8:
            slots_cost = def_slot()

        if moving == "w" and current_position[0] > 0:
            if current_map[current_position[0] - 1][current_position[1]] not in "TVH":
                moves += 1
                if current_map[current_position[0] - 1][current_position[1]] == "R":
                    current_energy = r(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] -= 1

                elif current_map[current_position[0] - 1][current_position[1]] == "N":
                    current_energy = dot_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] -= 1

                elif current_map[current_position[0] - 1][current_position[1]] == "J":
                    current_position[0] -= 1
                    current_energy, slots_cost = j(current_energy, current_map, current_position, current_inventory,
                                                   move_cost, slots_cost, companions_cost, def_slot)

                elif current_map[current_position[0] - 1][current_position[1]] == "r":
                    current_energy = r_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] -= 1

                elif current_map[current_position[0] - 1][current_position[1]] in "Ff":
                    Village().in_village()
                    # current_gold, current_energy, \
                    #     slots_cost, company_cost = f(current_gold, current_energy, current_vendor,
                    #                                  current_companions, current_inventory, def_slot, scout_sight)
                    # current_position[0] -= 1

                elif current_map[current_position[0] - 1][current_position[1]] == "O":
                    current_position[0] -= 1
                    current_energy, slots_cost = o(current_energy, current_map, current_position, current_inventory,
                                                   def_slot, four_steps, moves)

                elif current_map[current_position[0] - 1][current_position[1]] in "S":
                    current_position[0] -= 1
                    current_energy, current_slot,\
                        currently_injured, injureds_list = s(current_energy, current_map, current_position,
                                                             current_inventory, def_slot, moves, four_steps,
                                                             current_companions, currently_injured, injureds_list)

                elif current_map[current_position[0] - 1][current_position[1]] in ".":
                    current_position[0] -= 1
                    current_energy = dot(current_energy, current_companions, current_inventory, slots_cost,
                                         companions_cost)

                elif current_map[current_position[0] - 1][current_position[1]] in "B":
                    current_position[0] -= 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = b(current_energy, current_position,
                                                             current_inventory, def_slot, injureds_list,
                                                             current_companions, currently_injured)

                elif current_map[current_position[0] - 1][current_position[1]] in "LP":
                    current_position[0] -= 1

        elif moving == "s" and current_position[0] < 15:
            if current_map[current_position[0] + 1][current_position[1]] not in "TVH":
                moves += 1

                if current_map[current_position[0] + 1][current_position[1]] == "R":
                    current_energy = r(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] += 1

                elif current_map[current_position[0] + 1][current_position[1]] == "N":
                    current_energy = dot_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] += 1

                elif current_map[current_position[0] + 1][current_position[1]] == "J":
                    current_position[0] += 1
                    current_energy, slots_cost = j(current_energy, current_map, current_position, current_inventory,
                                                   move_cost, slots_cost, companions_cost, def_slot)

                elif current_map[current_position[0] + 1][current_position[1]] == "r":
                    current_energy = r_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[0] += 1

                elif current_map[current_position[0] + 1][current_position[1]] in "Ff":
                    Village().in_village()
                    # current_gold, current_energy, \
                    #     slots_cost, company_cost = f(current_gold, current_energy, current_vendor,
                    #                                  current_companions, current_inventory, def_slot, scout_sight)
                    # current_position[0] += 1

                elif current_map[current_position[0] + 1][current_position[1]] in "O":
                    current_position[0] += 1
                    current_energy, slots_cost = o(current_energy, current_map, current_position, current_inventory,
                                                   def_slot, four_steps, moves)

                elif current_map[current_position[0] + 1][current_position[1]] in "S":
                    current_position[0] += 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = s(current_energy, current_map, current_position,
                                                             current_inventory, def_slot, moves, four_steps,
                                                             current_companions, currently_injured, injureds_list)

                elif current_map[current_position[0] + 1][current_position[1]] in ".":
                    current_position[0] += 1
                    current_energy = dot(current_energy, current_companions, current_inventory, slots_cost,
                                         companions_cost)

                elif current_map[current_position[0] + 1][current_position[1]] in "B":
                    current_position[0] += 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = b(current_energy, current_position,
                                                             current_inventory, def_slot, injureds_list,
                                                             current_companions, currently_injured)

                elif current_map[current_position[0] + 1][current_position[1]] in "LP":
                    current_position[0] += 1

        elif moving == "a" and current_position[1] > 0:
            if current_map[current_position[0]][current_position[1] - 1] not in "TVH":
                moves += 1

                if current_map[current_position[0]][current_position[1] - 1] == "R":
                    current_energy = r(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] -= 1

                elif current_map[current_position[0]][current_position[1] - 1] == "N":
                    current_energy = dot_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] -= 1

                elif current_map[current_position[0]][current_position[1] - 1] == "J":
                    current_position[1] -= 1
                    current_energy, slots_cost = j(current_energy, current_map, current_position, current_inventory,
                                                   move_cost, slots_cost, companions_cost, def_slot)

                elif current_map[current_position[0]][current_position[1] - 1] == "r":
                    current_energy = r_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] -= 1

                elif current_map[current_position[0]][current_position[1] - 1] in "Ff":
                    Village().in_village()
                    # current_gold, current_energy, \
                    #     slots_cost, company_cost = f(current_gold, current_energy, current_vendor,
                    #                                  current_companions, current_inventory, def_slot, scout_sight)
                    # current_position[1] -= 1

                elif current_map[current_position[0]][current_position[1] - 1] in "O":
                    current_position[1] -= 1
                    current_energy, slots_cost = o(current_energy, current_map, current_position, current_inventory,
                                                   def_slot, four_steps, moves)

                elif current_map[current_position[0]][current_position[1] - 1] in "S":
                    current_position[1] -= 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = s(current_energy, current_map, current_position,
                                                             current_inventory, def_slot, moves, four_steps,
                                                             current_companions, currently_injured, injureds_list)

                elif current_map[current_position[0]][current_position[1] - 1] in ".":
                    current_position[1] -= 1
                    current_energy = dot(current_energy, current_companions, current_inventory, slots_cost,
                                         companions_cost)

                elif current_map[current_position[0]][current_position[1] - 1] in "B":
                    current_position[1] -= 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = b(current_energy, current_position,
                                                             current_inventory, def_slot, injureds_list,
                                                             current_companions, currently_injured)

                elif current_map[current_position[0]][current_position[1] - 1] in "LP":
                    current_position[1] -= 1

        elif moving == "d" and current_position[1] < 15:
            if current_map[current_position[0]][current_position[1] + 1] not in "TVH":
                moves += 1

                if current_map[current_position[0]][current_position[1] + 1] == "R":
                    current_energy = r(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] += 1

                elif current_map[current_position[0]][current_position[1] + 1] == "N":
                    current_energy = dot_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] += 1

                elif current_map[current_position[0]][current_position[1] + 1] == "J":
                    current_position[1] += 1
                    current_energy, slots_cost = j(current_energy, current_map, current_position, current_inventory,
                                                   move_cost, slots_cost, companions_cost, def_slot)

                elif current_map[current_position[0]][current_position[1] + 1] == "r":
                    current_energy = r_wet(current_energy, move_cost, slots_cost, companions_cost)
                    current_position[1] += 1

                elif current_map[current_position[0]][current_position[1] + 1] in "Ff":
                    Village().in_village()
                    # current_gold, current_energy, \
                    #     slots_cost, company_cost = f(current_gold, current_energy, current_vendor,
                    #                                  current_companions, current_inventory, def_slot, scout_sight)
                    # current_position[1] += 1

                elif current_map[current_position[0]][current_position[1] + 1] in "O":
                    current_position[1] += 1
                    current_energy, slots_cost = o(current_energy, current_map, current_position, current_inventory,
                                                   def_slot, four_steps, moves)

                elif current_map[current_position[0]][current_position[1] + 1] in "S":
                    current_position[1] += 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = s(current_energy, current_map, current_position,
                                                             current_inventory, def_slot, moves, four_steps,
                                                             current_companions, currently_injured, injureds_list)

                elif current_map[current_position[0]][current_position[1] + 1] in ".":
                    current_position[1] += 1
                    current_energy = dot(current_energy, current_companions, current_inventory, slots_cost,
                                         companions_cost)

                elif current_map[current_position[0]][current_position[1] + 1] in "B":
                    current_position[1] += 1
                    current_energy, current_slot, \
                        currently_injured, injureds_list = b(current_energy, current_position,
                                                             current_inventory, def_slot, injureds_list,
                                                             current_companions, currently_injured)

                elif current_map[current_position[0]][current_position[1] + 1] in "LP":
                    current_position[1] += 1

        elif moving == "b":
            player.display_inventory()
        elif moving == "c":
            if len(companions) > 0:
                for e in companions:
                    print(e, companions[e])
                input("")
            else:
                input("You have no companions!")

        for e in four_steps:
            if e + 4 == moves:
                # function to change back the L to terrain
                volcano_back(current_map)

        if currently_injured:
            #  5% chance on calling the injury funciton.
            if random.randint(1, 100) < 5:
                company_cost, currently_injured, allowed_slots = injury(current_companions, current_inventory,
                                                                        allowed_slots, scout_sight)

        display_map(current_map, position)
        print("     min _________________________ max")
        print("HP:     |" + colored(str(int(player.health_point // 4) * u"\u25A0"), "green") +
              str(int(player.health_point)))
        print("energy: |" + colored(str(int(player.energy // 4) * u"\u25A0"), "yellow") + str(int(player.energy)))
        print("Mana:   |" + colored(str(int(player.mana_point) * ("|" + u"\u25A0" + "|")), "blue") +
              str(int(player.mana_point)))
        print("gold: " + colored(str(current_gold), "yellow"))
        print("slot cost: " + str(slots_cost))
        print("company cost: " + str(company_cost))
        print("injured: " + str(currently_injured))
        print("injured list: " + str(injureds_list))
        print("allowed slots: " + str(allowed_slots))
        # display_oldmap(game_map, position)


# gold, allowed_slots = crew_recruitment(gold, companions, inventory, allowed_slots)
display_map(game_map, position)
# print()
# display_oldmap(game_map, position)
print(" ~~ WELCOME TO THE PECULIAR EXPEDITION ~~ ")
print("Above you can see the map. Your current location is always highlighted with yellow.")
move(game_map, player.energy, player.gold, position, player.companions, inventory, company_cost, EC, slots, injured,
     injured_list, sight)
