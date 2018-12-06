current_energy = 100  # displayed as u"\u25A0" bar
EC = 3  # game difficulty. minimal energy cost for a move.
gold = 250
position = [3, 5]  # actual position on the map
moves = 0  # number of moves the player made in the game

# ITEMS: NAME/AMOUNT/COST/ATTRIBUTE
inventory = {
    "rope": [2, 40, 0],
    "machete": [2, 40, 0],
    "torch": [1, 40, 0],
    "glassball": [2, 100, 0],
    "whiskey": [1, 50, 20],
}
# ITEMS: NAME/AMOUNT/COST/ATTRIBUTE
vendor = {
    "fruit": [5, 45, 15],
    "meat": [5, 60, 25],
    "chocolate": [5, 50, 20],
    "medicine": [5, 50, 20],
    "whiskey": [5, 50, 20],
    "rope": [2, 40, 0],
    "torch": [2, 40, 0]
}

companions = {

}

crew = {
    "trader": "- 10% price bonus for trading",
    "soldier": "- Whiskey gives + 20% Energy",
    "donkey": "- +2 inventory slots"
}

villagers = {
    "scout": "  +1 vision",
    "shaman": "- Medicine gives +20% energy",
    "wise": "- +3 reputation on new maps"
}

import time
from termcolor import colored
import random

map = [
    ["T", "T", "T", "T", "T", "T", "F", "R", "R", "H", "O", ".", ".", "N", "V", "V"],
    ["T", "T", "T", "T", "T", "T", "T", "J", "J", "H", ".", "R", "R", "r", "r", "N"],
    ["T", "T", "T", "T", "T", "T", ".", "J", ".", "H", "H", "N", "r", "R", "R", "H"],
    ["T", "T", "T", "T", "T", "C", ".", ".", "B", "H", "H", "V", "N", "N", "H", "H"],
    ["T", "T", "T", "T", "T", "T", "T", ".", "N", "N", "V", "V", "V", "J", ".", "S"],
    ["T", "T", "T", "T", "T", "R", ".", "R", "J", "J", "V", "r", "r", "r", ".", "L"],
    ["T", "T", "T", "J", "J", ".", "R", "J", "J", "O", "N", "N", "R", ".", ".", "J"],
    ["T", "T", "T", "T", "R", "R", "R", ".", ".", ".", ".", "V", "H", "P", "J", "."],
    ["T", "T", "T", "T", "T", "H", "J", "F", ".", "R", "H", "B", ".", "H", "J", "H"],
    ["T", "T", "T", "T", "T", "T", "H", ".", "L", "R", ".", ".", "R", "R", "B", "S"],
    ["T", "T", "T", "T", "T", "T", "S", ".", "J", "R", "J", "H", ".", "R", "R", "."],
    ["T", "T", "T", "T", "T", ".", ".", "R", ".", "J", ".", "H", "H", ".", ".", "."],
    [".", "T", "R", ".", "R", "R", "R", "R", ".", "N", "N", "N", "H", "H", "H", "H"],
    ["H", "T", "R", "H", ".", ".", "H", "J", ".", "r", "V", "f", ".", "B", "H", "."],
    ["T", "T", "T", ".", "J", "J", "B", "H", ".", "r", "N", "N", "R", "J", "J", "J"],
    ["T", "T", "T", "T", ".", "J", "L", "L", ".", ".", "R", "O", ".", ".", "J", "J"]
]

from GAME_displays import display_curse_geyser
from GAME_displays import display_curse_volcano
from GAME_displays import display_shrine_treasure
from GAME_displays import display_shrine
from GAME_displays import display_shrine_chest
from GAME_displays import display_shrine_doll
from GAME_displays import display_shrine_room
from GAME_displays import display_shrine_runes
from GAME_displays import display_shrine_door
from GAME_displays import display_rest
from GAME_displays import display_merchant
from GAME_displays import display_village
from GAME_displays import display_crew
from GAME_displays import display_bag


# ITEMS: NAME/AMOUNT/COST/ATTRIBUTE

def display_inventory(energy):
    display_bag()
    if len(inventory) > allowed_slots:
        print(str(len(inventory)) + " out of " + str(allowed_slots) + ". You are carrying" +
              str(len(inventory) - allowed_slots) + "extra items in your hand.")
    else:
        print(str(len(inventory)) + " out of " + str(allowed_slots) + ". You have " +
              str(allowed_slots - len(inventory)) + " free slots left.")
    for e in inventory:
        if inventory[e][0] != 0:
            print(e, inventory[e][0])  # print inventory elements if have any of it.

    while True:
        print("     min _________________________ max")
        print("energy: |" + colored(str(int(energy / 4) * u"\u25A0"), "green"))

        if "soldier" in companions:
            print("Because you have a Soldier companion, you get extra 20% energy when drinking whiskey")
        if "shaman" in companions:
            print("Because you have a Shaman companion, you get extra 20% energy when using medicine")

        X = input("choose food or drink to consume for energy or press 'ENTER' to exit: \n")
        if X == "fruit" or X == "whiskey" or X == "medicine" or X == "chocolate" or X == "meat":
            for e in list(inventory):
                if X == e:
                    Y = int(input("How many would you like to eat or drink? "))
                    if inventory[e][0] - Y > -1:
                        if energy + (inventory[e][2] * Y) > 100:
                            energy = 100
                            inventory[e][0] -= Y
                            if inventory[e][0] == 0:
                                inventory.pop(e, None)

                        else:
                            energy += (inventory[e][2] * Y)
                            inventory[e][0] -= Y
                            if inventory[e][0] == 0:
                                inventory.pop(e, None)


                    else:
                        print("You don't have that much...")

        else:
            slots()
            energy -= 0
            return energy


#############################################################################################
# TERRAIN TYPES

##### .

def dot(energy):
    if (len(inventory)) > 8:
        energy -= slots_cost * company_cost
        return energy
    else:
        energy -= 0
        return energy


##### R

def R(energy):
    energy -= (EC * 1.4) * slots_cost * company_cost
    return energy


##### r

def r(energy):
    energy -= (EC * 2.1) * slots_cost * company_cost
    return energy


##### N

def N(energy):
    energy -= (EC * 1.8) * slots_cost * company_cost
    return energy


##### J

def J(energy):
    if "machete" in inventory:
        if inventory["machete"][0] >= 1:
            inventory["machete"][0] -= 1
            map[position[0]][position[1]] = "."
            energy -= EC * slots_cost * company_cost
            if inventory["machete"][0] == 0:
                inventory.pop("machete", None)
        company()
        slots()
        return energy
    else:
        energy -= (EC * 2) * slots_cost * company_cost
        company()
        slots()
        return energy


##### F

def F(gold, energy):
    villager_chance = random.randint(1, 101)
    if villager_chance <= 99:
        gold = villager_recruitment(gold)

    while True:

        display_village()
        Z = input("For trading enter 'trade', for resting 'rest' or hit 'ENTER' to leave the village ").lower()
        if Z == "trade":
            display_merchant()

            print("ITEM, AMOUNT, COST")
            for e in vendor:
                if "trader" in companions:
                    if vendor[e][0] != 0:
                        print(e, vendor[e][0],
                              str(int(vendor[e][1] * 0.9)))
                else:
                    if vendor[e][0] != 0:
                        print(e, vendor[e][0],
                              vendor[e][1])  # print the key (item name), 1. value (amount), 2. value (price)

            print()
            print("My inventory:")
            for e in inventory:
                if "trader" in companions:
                    if inventory[e][0] != 0:
                        print(e, inventory[e][0], str(int(inventory[e][1] * 1.1)))
                else:
                    if inventory[e][0] != 0:
                        print(e, inventory[e][0], inventory[e][1])
            print("My gold: " + colored(str(gold), "yellow"))
            if "trader" in companions:
                print("Because You have a Trader companion, You can sell your stuff for more gold, and buy cheaper!")

            while True:
                b_s = input("Enter 'b' to buy, 's' to sell, 'i' to check inventory, 'ENTER' to exit: ")
                if b_s == "b":
                    X = input("choose an item (type the name), or hit ENTER to exit: ").lower()
                    if X not in vendor:
                        gold -= 0
                        break

                    Y = int(input("how many would you like to buy? (enter a number) "))
                    if X in vendor and Y <= vendor[X][0] and Y * vendor[X][1] <= gold:
                        vendor[X][0] -= Y
                        print()
                        if "trader" in companions:
                            gold -= int(Y * (vendor[X][1] * 0.9))
                            print("You saved " + colored(str((Y * vendor[X][1]) - int((Y * (vendor[X][1] * 0.9)))),
                                                         "yellow") + " gold. Thanks to your Trader!")
                        else:
                            gold -= Y * vendor[X][1]
                        if X in inventory:
                            inventory[X][0] += Y
                            inventory[X][1] = vendor[X][1]
                            inventory[X][2] = vendor[X][2]
                            print("My gold: " + colored(str(gold), "yellow"))

                        else:
                            inventory[X] = [int(x) for x in str(Y)]
                            inventory[X].append(vendor[X][1])
                            inventory[X].append(vendor[X][2])
                            print()
                            print("My gold: " + colored(str(gold), "yellow"))

                elif b_s == "s":
                    X = input("choose an item (type the name), or hit ENTER to exit: ").lower()
                    if X not in inventory:
                        gold -= 0
                        break

                    Y = int(input("how many would you like to sell? (enter a number) "))
                    if X in inventory and Y <= inventory[X][0]:
                        inventory[X][0] -= Y
                        print()
                        if "trader" in companions:
                            gold += int(Y * (inventory[X][1] * 1.1))
                            print("You earned " + colored(
                                str(int((int(Y * (inventory[X][1] * 1.1)))) - (Y * inventory[X][1])),
                                "yellow") + " extra gold. Thanks to your Trader!")
                            if inventory[X][0] == 0:
                                inventory.pop(X, None)
                            print("My gold: " + colored(str(gold), "yellow"))
                        else:
                            gold += Y * inventory[X][1]
                            if inventory[X][0] == 0:
                                inventory.pop(X, None)
                            print("My gold: " + colored(str(gold), "yellow"))

                elif b_s == "i":
                    display_merchant()
                    print("ITEM, AMOUNT, COST")
                    for e in vendor:
                        if "trader" in companions:
                            if vendor[e][0] != 0:
                                print(e, vendor[e][0],
                                      str(int(vendor[e][1] * 0.9)))
                        else:
                            if vendor[e][0] != 0:
                                print(e, vendor[e][0],
                                      vendor[e][1])  # print the key (item name), 1. value (amount), 2. value (price)

                    print()
                    print("My inventory:")
                    for e in inventory:
                        if "trader" in companions:
                            if inventory[e][0] != 0:
                                print(e, inventory[e][0], str(int(inventory[e][1] * 1.1)))
                        else:
                            if inventory[e][0] != 0:
                                print(e, inventory[e][0], inventory[e][1])
                    print("My gold: " + colored(str(gold), "yellow"))
                else:
                    break

        elif Z == "rest":  # restoring energy
            if energy < 100:
                print(("\n") * 10)
                display_rest()
                print()
                print("You are resting in this fancy bed!")
                print("     min _________________________ max")
                print("energy: |" + colored(str(int(energy / 4) * u"\u25A0"), "green"), end='')
                while int(energy) <= 96:
                    time.sleep(1.5)  # every 1.5 seconds we add +4 to the current energy
                    energy += 4
                    print(colored(str(u"\u25A0"), "green"), end='')  # with the "end=''" parameter the bar is adding up
                    if int(energy) > 96:
                        energy = 100
                print()
                print("Rise and Shine beautiful! You are rested!")
                input(" ")
            else:
                print("You are rested already... Go and kick some asses You lazy pig!")
                input(" ")



        else:
            slots()
            gold -= 0
            return gold, energy


##### O

four_steps = []  # saves the current moves number for later use (after 4 steps its used)


def O(energy):  # Function on Shrines.
    display_shrine()
    global four_steps

    for e in O_coordinate:
        if position == e:
            input("You have already cleared this Shrine...")
            energy -= 0
            return energy

    if position not in O_coordinate:
        O_coordinate.append(position.copy())

    input("You see an old shrine in the distance. Not sure why, but you feel the need to get closer.")
    input("You feel almost like... its calling you... ")
    display_shrine_door()
    input("Step by step You get closer to the entrance of the Shrine...")
    input("You see a great closed stone door with ancient runes carved into it.")
    input("You have never seen runes like these before, but somehow You can still read it...")
    display_shrine_runes()
    input("You whisper the ancient words while reading the runes...")
    print("fa ur", end='')
    time.sleep(1)
    print("os rit", end='')
    time.sleep(1.5)
    print("kaun hg'agalas ", end='')
    time.sleep(2)
    print("laf man ", end='')
    time.sleep(2)
    print("yr'eh odal")
    time.sleep(1.5)
    input("When You finished reading the runes the door immediately creeked open, and You entered without hesitaion...")
    display_shrine_room()
    input("The first thing you saw was a 'doll' on the ground... You grabbed it and and gave it a closer look")
    display_shrine_doll()
    input("It looks like a...")
    input("Voodoo doll...")
    input("You heared a creeking sound from behind")
    input("You glanced back over your shoulder and realised the door you came in was closed")
    input("You don't remember closing it...")
    input("A chill went down on your spine. Your heart started beating faster")
    input("This was the first time You questioned if it was a good idea to come to this place...")
    input("Your eyes started to get used to the dark, and you could see something at the end of the corridor...")
    input("Candles blazing next to a something big... a box? a chest maybe?")
    input("You start to walk slowly towards the end of the corridor")
    display_shrine_chest()
    input("It looks like an old chest. It might contain treasure!")
    input("Or something much worse...")
    input("You hear distant whispers in your head... like some kind of voodoo chanting")
    input("You know there is something wrong with this place... You have to act quickly!")
    input("What do you do? loot the chest and face the consequences, or run away and never look back?")
    loot = input("type 'loot' or hit enter you run away... ")
    if loot == "loot":
        display_shrine_treasure()
        input("You opened the chest slowly and this is what You found...")
        input("A cracked skull with a golden dagger in it.")
        input("This dagger probably worht a lot... you pulled it out of the skull and...")
        if "treasure" in inventory:  # adds a treasure to inventory.
            inventory["treasure"][0] += 1
        else:
            inventory["treasure"] = [1, 100, 0]

        curse_chance = random.randint(1, 101)  # 80% chance on a curse. If curse happens:
        if curse_chance <= 80:
            energy -= 15
            input("The whispers in your head are getting louder and louder.")
            input("It's not whispers anymore. IT'S SCREAMING!")
            input("YOU CAN FEEL THE GROUND SHAKING BENEATH YOUR FEET")
            input("You are trying to get back to the door, but it is so hard to move")
            input("Somehow you make it to the door and try to open it, but its stuck! ")
            input("THE VOODOO CHANTING AND SCREAMS ARE SO LOUD THEY ARE ALMOST UNBEARABLE...")
            input("You also start to scream: STOP! STOOOP! PLEASE STOOOOOOP!")
            input("You starin to the door, punching it, kicking it but it doesnt move...")
            input("Val'har ak yer'un chtu zul. VAL'HAR AK YURIN TCHE TUN!")
            input("The chanting is starting to make you crazy!")
            input("You grasp your last bits of energy, step back from the door and run into as hard as you can")
            input("The door finally opened, you rolled down the stairs.")
            input("The chanthing stopped... but the earthquake got stronger... You looked up and...")
            X = random.randint(1, 101)  # 35% chance on volcano curse, 65% chance on geyser curse
            if X <= 35:
                display_curse_volcano()
                input("You can see thick black smoke flying up from the closest mountain...")
                input("It turned into a Volcano!")
                input("bright red and yellow Lava is flowing out of it, burning everything down in its way...")
                input("'What have I done?' You are thinking... but It's too late for regrets now...")
                four_steps.append(moves)
                curse_Volcano(map)
                slots()
                return energy
            else:
                display_curse_geyser()
                input("You can see a huge water pillar emerging from the closest lake...")
                input("It turend into a geyser, spitting water everywhere in the area, making everything wet...")
                input("'What have I done?' You are thinking... but It's too late for regrets now...")
                curse_geyser()
                slots()
                return energy
        else:
            input("You run to the door, kick it in and run of the Shrine!")
            input("The fresh air filled your lungs, You looked down to your brand new treasure and thought:")
            input("Next time I might not be this lucky...")
            slots()
            energy -= 0
            return energy

    else:
        slots()
        energy -= 0
        return energy


##### S

S_coordinate = []


def S(energy):
    global four_steps

    for e in S_coordinate:
        if position == e:
            input("You have already cleared this Sanctuary...")
            energy -= 0
            return energy

    if position not in S_coordinate:
        S_coordinate.append(position.copy())

    if "treasure" in inventory:  # adds a treasure to inventory.
        inventory["treasure"][0] += 1
    else:
        inventory["treasure"] = [1, 100, 0]

    if inventory["rope"][0] >= 1:
        inventory["rope"][0] -= 1
        if inventory["rope"][0] == 0:
            inventory.pop("rope", None)
        energy -= 0
        slots()
        return energy
    else:
        bad_luck = random.randint(1, 101)
        if bad_luck <= 50:
            energy = catastrophe(energy)
            slots()
            return energy

        elif bad_luck >= 51 and bad_luck <= 70:
            curse_chance = random.randint(1, 101)
            if curse_chance <= 65:
                display_curse_geyser()
                curse_geyser()
                energy -= 0
                slots()
                return energy
            else:
                four_steps.append(moves)
                display_curse_volcano()
                curse_Volcano(map)
                energy -= 0
                slots()
                return energy
        else:
            slots()
            energy -= 0
            return energy


##### B

B_coordinate = []


def B(energy):
    for e in B_coordinate:
        if position == e:
            input("You have already been in this Cave...")
            energy -= 0
            return energy

    if position not in B_coordinate:
        B_coordinate.append(position.copy())

    if "treasure" in inventory:  # adds a treasure to inventory.
        inventory["treasure"][0] += 1
    else:
        inventory["treasure"] = [1, 100, 0]

    if inventory["torch"][0] >= 1:
        inventory["torch"][0] -= 1
        if inventory["torch"][0] == 0:
            inventory.pop("torch", None)
        energy -= 0
        slots()
        return energy
    else:
        catastrophe_chance = random.randint(1, 101)
        if catastrophe_chance <= 65:
            energy = catastrophe(energy)
            slots()
            return energy
        else:
            energy -= 0
            slots()
            return energy


##########################################################################################


# INTERACTIVES

##### catastrophe

def catastrophe(energy):
    X = random.randint(1, 101)
    if X <= 70:
        energy -= 45
        return energy
    else:
        energy -= 0
        return energy


##### volcano

O_coordinate = []  # coordinates of the Shrine we are currently in.
L_coordinate = []  # types and coordinates of terrains that are being changed to L
Volcano_coordinate = []  # coordinates of H-s being changed to @ (volcanos)


def curse_Volcano(map):
    H_coordinates = []  # Actual coordinates of H-s, like : [3, 5]
    steps = []  # Number of steps between position and H, like: 5

    for row_index, row in enumerate(map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == "H":
                H_coordinates.append([row_index, column_index])
                steps.append(sum([abs(position[0] - row_index), (abs(position[1] - column_index))]))

    H = H_coordinates[steps.index(min(steps))]  # coordinate of the closest H to our position

    map[H[0]][H[1]] = "@"  # Change the closest H to our position to @ (volcano)
    Volcano_coordinate.append([map.index(map[H[0]]), map.index(map[H[1]])])

    if H[0] - 1 > 0 and map[H[0] - 1][H[1]] not in "TVSHOF":
        L_coordinate.append([map[H[0] - 1][H[1]], map.index(map[H[0] - 1]), map.index(map[H[1]])])
        map[H[0] - 1][H[1]] = "L"

    if H[0] + 1 < 15 and map[H[0] + 1][H[1]] not in "TVSHOF":
        L_coordinate.append([map[H[0] + 1][H[1]], map.index(map[H[0] + 1]), map.index(map[H[1]])])
        map[H[0] + 1][H[1]] = "L"

    if H[1] - 1 > 0 and map[H[0]][H[1] - 1] not in "TVSHOF":
        L_coordinate.append([map[H[0]][H[1] - 1], map.index(map[H[0]]), map.index(map[H[1] - 1])])
        map[H[0]][H[1] - 1] = "L"

    if H[1] + 1 < 15 and map[H[0]][H[1] + 1] not in "TVSHOF":
        L_coordinate.append([map[H[0]][H[1] + 1], map.index(map[H[0]]), map.index(map[H[1] + 1])])
        map[H[0]][H[1] + 1] = "L"

    if H[0] - 1 > 0 and H[1] - 1 > 0 and map[H[0] - 1][H[1] - 1] not in "TVSHOF":
        L_coordinate.append([map[H[0] - 1][H[1] - 1], map.index(map[H[0] - 1]), map.index(map[H[1] - 1])])
        map[H[0] - 1][H[1] - 1] = "L"

    if H[0] + 1 < 15 and H[1] + 1 < 15 and map[H[0] + 1][H[1] + 1] not in "TVSHOF":
        L_coordinate.append([map[H[0] + 1][H[1] + 1], map.index(map[H[0] + 1]), map.index(map[H[1] + 1])])
        map[H[0] + 1][H[1] + 1] = "L"

    if H[0] - 1 > 0 and H[1] + 1 < 15 and map[H[0] - 1][H[1] + 1] not in "TVSHOF":
        L_coordinate.append([map[H[0] - 1][H[1] + 1], map.index(map[H[0] - 1]), map.index(map[H[1] + 1])])
        map[H[0] - 1][H[1] + 1] = "L"

    if H[0] + 1 < 15 and H[1] - 1 > 0 and map[H[0] + 1][H[1] - 1] not in "TVSHOF":
        L_coordinate.append([map[H[0] + 1][H[1] - 1], map.index(map[H[0] + 1]), map.index(map[H[1] - 1])])
        map[H[0] + 1][H[1] - 1] = "L"


def volcano_back():
    for e in L_coordinate:
        map[e[1]][e[2]] = "."


##### geyser

def curse_geyser():
    Water_coordinates = []  # Actual coordinates of V-s, like : [3, 5]
    steps = []  # Number of steps between position and V, like: 5

    for row_index, row in enumerate(map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == "V":
                Water_coordinates.append([row_index, column_index])
                steps.append(sum([abs(position[0] - row_index), (abs(position[1] - column_index))]))

    W = Water_coordinates[steps.index(min(steps))]  # coordinate of the closest V to our position

    if position not in O_coordinate:
        O_coordinate.append(position.copy())

    map[W[0]][W[1]] = "G"  # change the closest V to our position to G

    if W[0] - 2 >= 0 and map[W[0] - 2][W[1]] not in "TVSHO":
        if map[W[0] - 2][W[1]] == ".":
            map[W[0] - 2][W[1]] = "N"
        elif map[W[0] - 2][W[1]] == "R":
            map[W[0] - 2][W[1]] = "r"
        elif map[W[0] - 2][W[1]] == "F":
            map[W[0] - 2][W[1]] = "f"

    if W[0] + 2 <= 15 and map[W[0] + 2][W[1]] not in "TVSHOJ":
        if map[W[0] + 2][W[1]] == ".":
            map[W[0] + 2][W[1]] = "N"
        elif map[W[0] + 2][W[1]] == "R":
            map[W[0] + 2][W[1]] = "r"
        if map[W[0] + 2][W[1]] == "F":
            map[W[0] + 2][W[1]] = "f"

    if W[1] - 2 >= 0 and map[W[0]][W[1] - 2] not in "TVSHOJ":
        if map[W[0]][W[1] - 2] == ".":
            map[W[0]][W[1] - 2] = "N"
        elif map[W[0]][W[1] - 2] == "R":
            map[W[0]][W[1] - 2] = "r"
        elif map[W[0]][W[1] - 2] == "F":
            map[W[0]][W[1] - 2] = "f"

    if W[1] + 2 <= 15 and map[W[0]][W[1] + 2] not in "TVSHOJ":
        if map[W[0]][W[1] + 2] == ".":
            map[W[0]][W[1] + 2] = "N"
        elif map[W[0]][W[1] + 2] == "R":
            map[W[0]][W[1] + 2] = "r"
        elif map[W[0]][W[1] + 2] == "F":
            map[W[0]][W[1] + 2] = "f"

    if W[0] - 2 >= 0 and W[1] - 2 > 0 and map[W[0] - 2][W[1] - 2] not in "TVSHOJ":
        if map[W[0] - 2][W[1] - 2] == ".":
            map[W[0] - 2][W[1] - 2] = "N"
        elif map[W[0] - 2][W[1] - 2] == "R":
            map[W[0] - 2][W[1] - 2] = "r"
        elif map[W[0] - 2][W[1] - 2] == "F":
            map[W[0] - 2][W[1] - 2] = "f"

    if W[0] - 2 >= 0 and W[1] - 1 > 0 and map[W[0] - 2][W[1] - 1] not in "TVSHOJ":
        if map[W[0] - 2][W[1] - 1] == ".":
            map[W[0] - 2][W[1] - 1] = "N"
        elif map[W[0] - 2][W[1] - 1] == "R":
            map[W[0] - 2][W[1] - 1] = "r"
        elif map[W[0] - 2][W[1] - 1] == "F":
            map[W[0] - 2][W[1] - 1] = "f"

    if W[0] - 1 >= 0 and W[1] - 2 > 0 and map[W[0] - 1][W[1] - 2] not in "TVSHOJ":
        if map[W[0] - 1][W[1] - 2] == ".":
            map[W[0] - 1][W[1] - 2] = "N"
        elif map[W[0] - 1][W[1] - 2] == "R":
            map[W[0] - 1][W[1] - 2] = "r"
        elif map[W[0] - 1][W[1] - 2] == "F":
            map[W[0] - 1][W[1] - 2] = "f"

    if W[0] + 2 <= 15 and W[1] + 2 < 15 and map[W[0] + 2][W[1] + 2] not in "TVSHOJ":
        if map[W[0] + 2][W[1] + 2] == ".":
            map[W[0] + 2][W[1] + 2] = "N"
        elif map[W[0] + 2][W[1] + 2] == "R":
            map[W[0] + 2][W[1] + 2] = "r"
        elif map[W[0] + 2][W[1] + 2] == "F":
            map[W[0] + 2][W[1] + 2] = "f"

    if W[0] + 2 <= 15 and W[1] + 1 < 15 and map[W[0] + 2][W[1] + 1] not in "TVSHOJ":
        if map[W[0] + 2][W[1] + 1] == ".":
            map[W[0] + 2][W[1] + 1] = "N"
        elif map[W[0] + 2][W[1] + 1] == "R":
            map[W[0] + 2][W[1] + 1] = "r"
        elif map[W[0] + 2][W[1] + 1] == "F":
            map[W[0] + 2][W[1] + 1] = "f"

    if W[0] + 1 <= 15 and W[1] + 2 < 15 and map[W[0] + 1][W[1] + 2] not in "TVSHOJ":
        if map[W[0] + 1][W[1] + 2] == ".":
            map[W[0] + 1][W[1] + 2] = "N"
        elif map[W[0] + 1][W[1] + 2] == "R":
            map[W[0] + 1][W[1] + 2] = "r"
        elif map[W[0] + 1][W[1] + 2] == "F":
            map[W[0] + 1][W[1] + 2] = "f"

    if W[0] - 2 >= 0 and W[1] + 2 < 15 and map[W[0] - 2][W[1] + 2] not in "TVSHOJ":
        if map[W[0] - 2][W[1] + 2] == ".":
            map[W[0] - 2][W[1] + 2] = "N"
        elif map[W[0] - 2][W[1] + 2] == "R":
            map[W[0] - 2][W[1] + 2] = "r"
        elif map[W[0] - 2][W[1] + 2] == "F":
            map[W[0] - 2][W[1] + 2] = "f"

    if W[0] - 2 >= 0 and W[1] + 1 < 15 and map[W[0] - 2][W[1] + 1] not in "TVSHOJ":
        if map[W[0] - 2][W[1] + 1] == ".":
            map[W[0] - 2][W[1] + 1] = "N"
        elif map[W[0] - 2][W[1] + 1] == "R":
            map[W[0] - 2][W[1] + 1] = "r"
        elif map[W[0] - 2][W[1] + 1] == "F":
            map[W[0] - 2][W[1] + 1] = "f"

    if W[0] - 1 >= 0 and W[1] + 2 < 15 and map[W[0] - 1][W[1] + 2] not in "TVSHOJ":
        if map[W[0] - 1][W[1] + 2] == ".":
            map[W[0] - 1][W[1] + 2] = "N"
        elif map[W[0] - 1][W[1] + 2] == "R":
            map[W[0] - 1][W[1] + 2] = "r"
        elif map[W[0] - 1][W[1] + 2] == "F":
            map[W[0] - 1][W[1] + 2] = "f"

    if W[0] + 2 <= 15 and W[1] - 2 > 0 and map[W[0] + 2][W[1] - 2] not in "TVSHOJ":
        if map[W[0] + 2][W[1] - 2] == ".":
            map[W[0] + 2][W[1] - 2] = "N"
        elif map[W[0] + 2][W[1] - 2] == "R":
            map[W[0] + 2][W[1] - 2] = "r"
        elif map[W[0] + 2][W[1] - 2] == "F":
            map[W[0] + 2][W[1] - 2] = "f"

    if W[0] + 2 <= 15 and W[1] - 1 > 0 and map[W[0] + 2][W[1] - 1] not in "TVSHOJ":
        if map[W[0] + 2][W[1] - 1] == ".":
            map[W[0] + 2][W[1] - 1] = "N"
        elif map[W[0] + 2][W[1] - 1] == "R":
            map[W[0] + 2][W[1] - 1] = "r"
        elif map[W[0] + 2][W[1] - 1] == "F":
            map[W[0] + 2][W[1] - 1] = "f"

    if W[0] + 1 <= 15 and W[1] - 2 > 0 and map[W[0] + 1][W[1] - 2] not in "TVSHOJ":
        if map[W[0] + 1][W[1] - 2] == ".":
            map[W[0] + 1][W[1] - 2] = "N"
        elif map[W[0] + 1][W[1] - 2] == "R":
            map[W[0] + 1][W[1] - 2] = "r"
        elif map[W[0] + 1][W[1] - 2] == "F":
            map[W[0] + 1][W[1] - 2] = "f"

##### company
company_cost = 1

def company():
    global company_cost
    if len(companions) > 0:
        company_cost = (len(companions) * 0.15) + 1
        return slots_cost
    else:
        company_cost = 1
        return slots_cost



##### slots

slots_cost = 1
allowed_slots = 8


def slots():
    global slots_cost
    if len(inventory) > allowed_slots:
        slots_cost = ((len(inventory) - allowed_slots) * 0.2) + 1
        return slots_cost
    else:
        slots_cost = 1
        return slots_cost


##### partners

def crew_recruitment(gold):
    display_crew()
    print("\n"
          "You can choose a companion for your adventures! Each costs 150 gold! You can have maximum 3 companions.")

    print("Every companion increases the cost of moves by 15%. Press 'ENTER' to continue \n")
    input("Press 'ENTER' to see the crew!")
    for i in crew:
        print(i, crew[i])
    print()

    while True:
        x = input(
            "Type the name of the companion you want to choose, or type 'Q' if You want to continue alone.").lower()
        for e in crew:
            if x == e:
                if gold >= 150 and len(companions) < 3:
                    companions[e] = crew[e]
                    crew.pop(e, None)
                    gold -= 150
                    if x == "soldier":
                        soldier()

                    elif x == "trader":
                        # It has no separate def function. It's implemented in def F() at trading costs.
                        pass

                    else:  # Donkey
                        donkey()
                    company()
                    return gold

                else:
                    gold -= 0
                    print("Not enough gold!")
                    input()
                    return gold

        if x == "q":
            gold -= 0
            return gold


def villager_recruitment(gold):
    display_crew()
    print("\n"
          "WOW! YOUR REPUTATION PRECEDES YOU! \n"
          "Local villagers offer their help to you for a little gold! \n"
          "Each costs 150 gold! You can have maximum 3 companions.")

    print("Every companion increases the cost of moves by 15%. Press 'ENTER' to continue \n"
          "Now You can choose from:")
    input("Press 'ENTER' to see the villagers: ")

    for i in villagers:
        print(i, villagers[i])

    print()

    while True:
        x = input(
            "Type the name of the companion you want to choose, or type 'Q' if You want to continue alone.").lower()
        for e in villagers:
            if x == e:
                if gold >= 150 and len(companions) < 3:
                    companions[e] = villagers[e]
                    villagers.pop(e, None)
                    gold -= 150
                    if x == "wise":
                        pass

                    elif x == "shaman":
                        shaman()

                    else:
                        pass
                    company()
                    return gold

                else:
                    gold -= 0
                    print("Not enough gold!")
                    input()
                    return gold

        if x == "q":
            gold -= 0
            return gold


def soldier():
    if "whiskey" in inventory:
        inventory["whiskey"][2] = 24

    if "whiskey" in vendor:
        vendor["whiskey"][2] = 24


def soldier_out():
    if "whiskey" in inventory:
        inventory["whiskey"][2] = 20

    if "whiskey" in vendor:
        vendor["whiskey"][2] = 20


def shaman():
    if "medicine" in inventory:
        inventory["medicine"][2] = 24

    if "medicine" in vendor:
        vendor["medicine"][2] = 24


def shaman_out():
    if "medicine" in inventory:
        inventory["medicine"][2] = 20

    if "medicine" in vendor:
        vendor["medicine"][2] = 20


def donkey():
    global allowed_slots
    allowed_slots += 2


def donkey_out():
    global allowed_slots
    allowed_slots -= 2


#############################################################################################


def display_map(map, position):
    print(("\n") * 15)
    for row_index, row in enumerate(map):  # <- with the enumerate, I can print the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can print the indexes

            if row_index == position[0] and column_index == position[1]:  # If the array element = to our position
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


def move(position, map, current_energy, gold):
    global moves
    while current_energy > 0:

        moving = input("move with 'w a s d', check your bag with 'b', see your companions with 'c'. ")
        if len(inventory) > 8:
            slots()

        if moving == "w" and position[0] > 0:
            if map[position[0] - 1][position[1]] not in "TVH":
                moves += 1
                if map[position[0] - 1][position[1]] == "R":
                    current_energy = R(current_energy)
                    position[0] -= 1

                elif map[position[0] - 1][position[1]] == "N":
                    current_energy = N(current_energy)
                    position[0] -= 1

                elif map[position[0] - 1][position[1]] == "J":
                    position[0] -= 1
                    current_energy = J(current_energy)

                elif map[position[0] - 1][position[1]] == "r":
                    current_energy = r(current_energy)
                    position[0] -= 1

                elif map[position[0] - 1][position[1]] in "Ff":
                    gold, current_energy = F(gold, current_energy)
                    position[0] -= 1

                elif map[position[0] - 1][position[1]] == "O":
                    position[0] -= 1
                    current_energy = O(current_energy)

                elif map[position[0] - 1][position[1]] in "S":
                    position[0] -= 1
                    current_energy = S(current_energy)

                elif map[position[0] - 1][position[1]] in ".":
                    position[0] -= 1
                    current_energy = dot(current_energy)

                elif map[position[0] - 1][position[1]] in "B":
                    position[0] -= 1
                    current_energy = B(current_energy)

                elif map[position[0] - 1][position[1]] in "LP":
                    position[0] -= 1

        elif moving == "s" and position[0] < 15:
            if map[position[0] + 1][position[1]] not in "TVH":
                moves += 1

                if map[position[0] + 1][position[1]] == "R":
                    current_energy = R(current_energy)
                    position[0] += 1

                elif map[position[0] + 1][position[1]] == "N":
                    current_energy = N(current_energy)
                    position[0] += 1

                elif map[position[0] + 1][position[1]] == "J":
                    position[0] += 1
                    current_energy = J(current_energy)

                elif map[position[0] + 1][position[1]] == "r":
                    current_energy = r(current_energy)
                    position[0] += 1

                elif map[position[0] + 1][position[1]] in "Ff":
                    gold, current_energy = F(gold, current_energy)
                    position[0] += 1

                elif map[position[0] + 1][position[1]] in "O":
                    position[0] += 1

                    current_energy = O(current_energy)
                elif map[position[0] + 1][position[1]] in "S":
                    position[0] += 1
                    current_energy = S(current_energy)

                elif map[position[0] + 1][position[1]] in ".":
                    position[0] += 1
                    current_energy = dot(current_energy)

                elif map[position[0] + 1][position[1]] in "B":
                    position[0] += 1
                    current_energy = B(current_energy)

                elif map[position[0] + 1][position[1]] in "LP":
                    position[0] += 1

        elif moving == "a" and position[1] > 0:
            if map[position[0]][position[1] - 1] not in "TVH":
                moves += 1

                if map[position[0]][position[1] - 1] == "R":
                    current_energy = R(current_energy)
                    position[1] -= 1

                elif map[position[0]][position[1] - 1] == "N":
                    current_energy = N(current_energy)
                    position[1] -= 1

                elif map[position[0]][position[1] - 1] == "J":
                    position[1] -= 1
                    current_energy = J(current_energy)

                elif map[position[0]][position[1] - 1] == "r":
                    current_energy = r(current_energy)
                    position[1] -= 1

                elif map[position[0]][position[1] - 1] in "Ff":
                    gold, current_energy = F(gold, current_energy)
                    position[1] -= 1

                elif map[position[0]][position[1] - 1] in "O":
                    position[1] -= 1
                    current_energy = O(current_energy)

                elif map[position[0]][position[1] - 1] in "S":
                    position[1] -= 1
                    current_energy = S(current_energy)

                elif map[position[0]][position[1] - 1] in ".":
                    position[1] -= 1
                    current_energy = dot(current_energy)

                elif map[position[0]][position[1] - 1] in "B":
                    position[1] -= 1
                    current_energy = B(current_energy)

                elif map[position[0]][position[1] - 1] in "LP":
                    position[1] -= 1

        elif moving == "d" and position[1] < 15:
            if map[position[0]][position[1] + 1] not in "TVH":
                moves += 1

                if map[position[0]][position[1] + 1] == "R":
                    current_energy = R(current_energy)
                    position[1] += 1

                elif map[position[0]][position[1] + 1] == "N":
                    current_energy = N(current_energy)
                    position[1] += 1

                elif map[position[0]][position[1] + 1] == "J":
                    position[1] += 1
                    current_energy = J(current_energy)

                elif map[position[0]][position[1] + 1] == "r":
                    current_energy = r(current_energy)
                    position[1] += 1

                elif map[position[0]][position[1] + 1] in "Ff":
                    gold, current_energy = F(gold, current_energy)
                    position[1] += 1

                elif map[position[0]][position[1] + 1] in "O":
                    position[1] += 1
                    current_energy = O(current_energy)

                elif map[position[0]][position[1] + 1] in "S":
                    position[1] += 1
                    current_energy = S(current_energy)

                elif map[position[0]][position[1] + 1] in ".":
                    position[1] += 1
                    current_energy = dot(current_energy)

                elif map[position[0]][position[1] + 1] in "B":
                    position[1] += 1
                    current_energy = B(current_energy)

                elif map[position[0]][position[1] + 1] in "LP":
                    position[1] += 1

        elif moving == "b":
            current_energy = display_inventory(current_energy)
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
                volcano_back()

        display_map(map, position)
        print("     min _________________________ max")
        print("energy: |" + colored(str(int(current_energy / 4) * u"\u25A0"), "green") + str(int(current_energy)))
        print("gold: " + colored(str(gold), "yellow"))



gold = crew_recruitment(gold)
display_map(map, position)
print(" ~~ WELCOME TO THE PECULIAR EXPEDITION ~~ ")
print("Above you can see the map. Your current location is always highlighted with yellow.")
move(position, map, current_energy, gold)
