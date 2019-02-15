# THIS FILE CONTAINS:
# Dictionary variables holding the keys and values for 'companions' and vendor merchandise
# Functions responsible for running the Village (trading,resting,hiring companions) , calculating the move cost in the
#   aspect of having more companions, giving and taking away benefits of companions on hiring or loosing them


import random
import time

from termcolor import colored

from GAME_displays import display_rest
from GAME_displays import display_merchant
from GAME_displays import display_village
from GAME_displays import display_crew

villagers = {
    "scout": "  +1 vision",
    "shaman": "- Medicine gives +20% energy",
    "wise": "- +3 reputation on new maps"
}

vendor = {
    "fruit": [5, 45, 15],
    "meat": [5, 60, 25],
    "chocolate": [5, 50, 20],
    "medicine": [5, 50, 20],
    "whiskey": [5, 50, 20],
    "rope": [2, 40, 0],
    "torch": [2, 40, 0],
    "machete": [1, 40, 0]
}

crew = {
    "trader": "- 10% price bonus for trading",
    "soldier": "- Whiskey gives + 20% Energy",
    "donkey": "- +2 inventory slots"
}


def f(current_gold, current_energy, current_vendor, current_companions, current_inventory, def_slot):
    # Village: chance to recruit villagers as companions, sell and buy items at vendor, rest for restoring energy
    villager_chance = random.randint(1, 101)
    if villager_chance <= 100:
        current_gold, companion_cost = villager_recruitment(current_gold, current_companions, current_inventory)
    else:
        companion_cost = 0

    while True:

        display_village()
        z = input("For trading enter 'trade', for resting 'rest' or hit 'ENTER' to leave the village ").lower()
        if z == "trade":
            display_merchant()

            print("ITEM, AMOUNT, COST")
            for e in current_vendor:
                if "trader" in current_companions:  # if player has trader companion, prices are 10% lower.
                    if current_vendor[e][0] != 0:
                        print(e, current_vendor[e][0],
                              str(int(current_vendor[e][1] * 0.9)))
                else:
                    if current_vendor[e][0] != 0:
                        print(e, current_vendor[e][0],
                              current_vendor[e][1])

            print()
            print("My inventory:")
            for e in current_inventory:
                if "trader" in current_companions:  # if player has trader, items can be sold for 10% extra gold
                    if current_inventory[e][0] != 0:
                        print(e, current_inventory[e][0], str(int(current_inventory[e][1] * 1.1)))
                else:
                    if current_inventory[e][0] != 0:
                        print(e, current_inventory[e][0], current_inventory[e][1])
            print("My gold: " + colored(str(current_gold), "yellow"))
            if "trader" in current_companions:
                print("Because You have a Trader companion, You make better deals!")

            while True:
                b_s = input("Enter 'b' to buy, 's' to sell, 'i' to check inventory, 'ENTER' to exit: ")
                if b_s == "b":
                    x = input("choose an item (type the name), or hit ENTER to exit: ").lower()
                    if x not in current_vendor:
                        current_gold -= 0
                        break

                    y = int(input("how many would you like to buy? (enter a number) "))
                    if x in current_vendor and y <= current_vendor[x][0] and y * current_vendor[x][1] <= current_gold:
                        current_vendor[x][0] -= y
                        print()
                        if "trader" in current_companions:
                            current_gold -= int(y * (current_vendor[x][1] * 0.9))
                            print("You saved " + colored(str((y * current_vendor[x][1]) -
                                                             int((y * (current_vendor[x][1] * 0.9)))),
                                                         "yellow") + " gold. Thanks to your Trader!")
                        else:
                            current_gold -= y * current_vendor[x][1]
                        if x in current_inventory:
                            current_inventory[x][0] += y
                            current_inventory[x][1] = current_vendor[x][1]
                            current_inventory[x][2] = current_vendor[x][2]
                            print("My gold: " + colored(str(current_gold), "yellow"))

                        else:
                            current_inventory[x] = [int(x) for x in str(y)]
                            current_inventory[x].append(current_vendor[x][1])
                            current_inventory[x].append(current_vendor[x][2])
                            print()
                            print("My gold: " + colored(str(current_gold), "yellow"))

                elif b_s == "s":
                    x = input("choose an item (type the name), or hit ENTER to exit: ").lower()
                    if x not in current_inventory:
                        current_gold -= 0
                        break

                    y = int(input("how many would you like to sell? (enter a number) "))
                    if x in current_inventory and y <= current_inventory[x][0]:
                        current_inventory[x][0] -= y
                        print()
                        if "trader" in current_companions:
                            current_gold += int(y * (current_inventory[x][1] * 1.1))
                            print("You earned " + colored(
                                str(int((int(y * (current_inventory[x][1] * 1.1)))) - (y * current_inventory[x][1])),
                                "yellow") + " extra gold. Thanks to your Trader!")
                            if current_inventory[x][0] == 0:
                                current_inventory.pop(x, None)
                            print("My gold: " + colored(str(current_gold), "yellow"))
                        else:
                            current_gold += y * current_inventory[x][1]
                            if current_inventory[x][0] == 0:
                                current_inventory.pop(x, None)
                            print("My gold: " + colored(str(current_gold), "yellow"))

                elif b_s == "i":
                    display_merchant()
                    print("ITEM, AMOUNT, COST")
                    for e in current_vendor:
                        if "trader" in current_companions:
                            if current_vendor[e][0] != 0:
                                print(e, current_vendor[e][0],
                                      str(int(current_vendor[e][1] * 0.9)))
                        else:
                            if current_vendor[e][0] != 0:
                                print(e, current_vendor[e][0],
                                      current_vendor[e][1])  # print (item name), 1. value (amount), 2. value (price)

                    print()
                    print("My inventory:")
                    for e in current_inventory:
                        if "trader" in current_companions:
                            if current_inventory[e][0] != 0:
                                print(e, current_inventory[e][0], str(int(current_inventory[e][1] * 1.1)))
                        else:
                            if current_inventory[e][0] != 0:
                                print(e, current_inventory[e][0], current_inventory[e][1])
                    print("My gold: " + colored(str(current_gold), "yellow"))
                else:
                    break

        elif z == "rest":  # restoring energy
            if current_energy < 100:
                print("\n" * 10)
                display_rest()
                print()
                print("You are resting in this fancy bed!")
                print("     min _________________________ max")
                print("energy: |" + colored(str(int(current_energy / 4) * u"\u25A0"), "green"), end='')
                while int(current_energy) <= 96:
                    time.sleep(0.5)  # every 0.5 seconds we add +4 to the current energy
                    current_energy += 4
                    print(colored(str(u"\u25A0"), "green"), end='')  # with the "end=''" parameter the bar is adding up
                    if int(current_energy) > 96:
                        current_energy = 100
                print()
                print("Rise and Shine beautiful! You are rested!")
                input(" ")
            else:
                print("You are rested already... Go and kick some asses You lazy pig!")
                input(" ")

        else:
            slot_cost = def_slot()
            current_gold -= 0
            return current_gold, current_energy, slot_cost, companion_cost


def villager_recruitment(current_gold, current_companions, current_inventory):
    # Player can choose a companion for 150 gold
    display_crew()
    print("\n"
          "WOW! YOUR REPUTATION PRECEDES YOU! \n"
          "Local villagers offer their help to you for a little gold! \n"
          "Each costs 150 gold! You can have maximum 3 companions.")

    print("Every companion increases the cost of moves by 15%. \n"
          "Now You can choose from:")
    if len(current_companions) == 3:
        input("You already have 3 companions. You can't have more!")
        current_gold -= 0
        companions_cost = company(current_companions)
        return current_gold, companions_cost
    input("Press 'ENTER' to see the villagers: ")

    for i in villagers:
        print(i, villagers[i])

    print()

    while True:
        x = input(
            "Type the name of the companion you want to choose, or type 'Q' if You want to continue alone.").lower()
        for e in villagers:
            if x == e:
                if current_gold >= 150 and len(current_companions) < 3:
                    current_companions[e] = villagers[e]
                    villagers.pop(e, None)
                    current_gold -= 150
                    if x == "wise":
                        pass

                    elif x == "shaman":
                        shaman(current_inventory)

                    else:
                        pass
                    companions_cost = company(current_companions)
                    return current_gold, companions_cost

                else:
                    current_gold -= 0
                    print("Not enough gold!")
                    input()
                    companions_cost = company(current_companions)
                    return current_gold, companions_cost

        if x == "q":
            current_gold -= 0
            companions_cost = company(current_companions)
            return current_gold, companions_cost


def crew_recruitment(current_gold, current_companions, current_inventory, max_slots):
    # Player can choose a companion for 150 gold
    display_crew()
    print("\n"
          "You can choose a companion for your adventures! Each costs 150 gold! You can have maximum 3 companions.")

    print("Every companion increases the cost of moves by 15%. Press 'ENTER' to continue \n")
    if len(current_companions) == 3:
        input("You already have 3 companions. You can't have more!")
        current_gold = current_gold
        max_slots = max_slots
        input(max_slots)
        return current_gold, max_slots
    input("Press 'ENTER' to see the crew!")
    for i in crew:
        print(i, crew[i])
    print()

    while True:
        x = input(
            "Type the name of the companion you want to choose, or type 'Q' if You want to continue alone.").lower()
        for e in crew:
            if x == e:
                if current_gold >= 150 and len(current_companions) < 3:
                    current_companions[e] = crew[e]
                    crew.pop(e, None)
                    current_gold -= 150
                    if x == "soldier":
                        soldier(current_inventory)

                    elif x == "trader":
                        # It has no separate def function. It's implemented in def F() at trading costs.
                        pass

                    else:  # Donkey
                        max_slots = donkey(max_slots)
                    company(current_companions)
                    input(max_slots)
                    return current_gold, max_slots

                else:
                    current_gold = current_gold
                    max_slots = max_slots
                    print("Not enough gold!")
                    input(max_slots)
                    input()
                    return current_gold, max_slots

        if x == "q":
            current_gold = current_gold
            max_slots = max_slots
            return current_gold, max_slots


def company(current_companions):
    # if player has companions, the energy cost of moves increases by 15%
    if len(current_companions) > 0:
        return (len(current_companions) * 0.15) + 1
    else:
        return 1


def shaman(current_inventory):
    # If soldier chosen as companion, set the energy bonus on medicine higher
    if "medicine" in current_inventory:
        current_inventory["medicine"][2] = 24

    if "medicine" in vendor:
        vendor["medicine"][2] = 24


def shaman_out(current_inventory):
    # If soldier leaves the group, change back medicine energy cost to original
    if "medicine" in current_inventory:
        current_inventory["medicine"][2] = 20

    if "medicine" in vendor:
        vendor["medicine"][2] = 20


def soldier(current_inventory):
    # If soldier chosen as companion, set the energy bonus on whiskey higher
    if "whiskey" in current_inventory:
        current_inventory["whiskey"][2] = 24

    if "whiskey" in vendor:
        vendor["whiskey"][2] = 24


def soldier_out(current_inventory):
    # If soldier leaves the group, change back whiskey energy cost to original
    if "whiskey" in current_inventory:
        current_inventory["whiskey"][2] = 20

    if "whiskey" in vendor:
        vendor["whiskey"][2] = 20


def donkey(max_slots):
    # If donkey chosen as companion, increase inventory slots
    max_slots += 2
    return max_slots


def donkey_out(max_slots):
    # If donkey leaves the group, change back inventory slots to original
    max_slots -= 2
    return max_slots
