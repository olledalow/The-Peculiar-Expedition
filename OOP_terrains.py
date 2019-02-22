from termcolor import colored
import time
import random

from OOP_displays import display_village, display_rest, display_crew, display_merchant, display_shrine, \
    display_shrine_treasure, display_curse_volcano, display_curse_geyser, display_boat, display_troll, display_tiger

from OOP_village_items import Treasure, Rope, Torch, Vendor
from OOP_player import player, Whiskey, Chocolate, Meat, Medicine, Fruit, scout, scout_out, donkey, donkey_out, fight
from OOP_map_position import game_map
from OOP_monsters import Troll, Tiger


class Terrain:
    def __init__(self, cost, step, icon):
        self.cost = cost
        self.step = step
        self.icon = icon

    def __eq__(self, other):
        return type(self) == type(other)


class Village(Terrain):
    def __init__(self):
        super().__init__(0, True, "F")
        self.villagers = {  # contains the rentable companions in the village
                          "scout": "  +1 vision",
                          "shaman": " Medicine gives +20% energy",
                          "wise": "   +3 reputation on new maps"
                         }
        self.vendor = Vendor()

    def in_village(self):
        while True:

            display_village()
            choice = input("For trading enter 'trade', for resting 'rest', for hiring 'hire'"
                           " or hit 'Q' to leave the village ").lower()
            if choice == "trade":
                self.display_vendor()

                while True:
                    buy_sell = input("Enter 'b' to buy, 's' to sell, 'i' to check inventory, 'Q' to exit: ")
                    if buy_sell == "b":
                        item = input("choose an item (type the name), or hit ENTER to exit: ").lower()
                        if item == "chocolate".lower():
                            item = Chocolate(int(input("how many would you like to buy? (enter a number) ")))
                        elif item == "meat".lower():
                            item = Meat(int(input("how many would you like to buy? (enter a number) ")))
                        elif item == "whiskey".lower():
                            item = Whiskey(int(input("how many would you like to buy? (enter a number) ")))
                        elif item == "medicine".lower():
                            item = Medicine(int(input("how many would you like to buy? (enter a number) ")))
                        elif item == "fruit".lower():
                            item = Fruit(int(input("how many would you like to buy? (enter a number) ")))
                        else:
                            print("The merchant doesn't sell that item")
                            break
                        print(item.pieces)
                        for element in self.vendor.contents:
                            if item.pieces <= element.pieces and item.pieces * element.price <= player.gold:
                                self.vendor.sell_item(item)
                                player.inventory.add_item(item)
                                player.gold -= item.pieces * int(element.price * 0.9) \
                                    if "trader" in player.companions else item.pieces * element.price
                                if "trader" in player.companions:
                                    print("You saved " +
                                          colored(str((item.pieces * element.price) -
                                                      int(item.pieces * element.price * 0.9)), "yellow") +
                                          " gold. Thanks to your Trader!")
                                print("My gold: " + colored(str(player.gold), "yellow"))
                                break
                            print("Not enough item or gold.")
                            break

                    elif buy_sell == "s":
                        item = input("choose an item (type the name), or hit Q to exit: ").lower()
                        if item == "chocolate".lower():
                            item = Chocolate(int(input("how many would you like to sell? (enter a number) ")))
                        elif item == "meat".lower():
                            item = Meat(int(input("how many would you like to sell? (enter a number) ")))
                        elif item == "whiskey".lower():
                            item = Whiskey(int(input("how many would you like to sell? (enter a number) ")))
                        elif item == "medicine".lower():
                            item = Medicine(int(input("how many would you like to sell? (enter a number) ")))
                        elif item == "fruit".lower():
                            item = Fruit(int(input("how many would you like to suy? (enter a number) ")))
                        else:
                            print("You don't have that in your Inventory")
                            break

                        for element in player.inventory.contents:
                            if item.pieces <= element.pieces:
                                player.inventory.remove_item(item)
                                print()
                                player.gold += item.pieces * int(element.price * 1.1) \
                                    if "trader" in player.companions else item.pieces * element.price

                                if "trader" in player.companions:
                                    print("You earned " +
                                          colored(str(int(item.pieces * element.price * 1.1) -
                                                      (item.pieces * element.price)), "yellow") +
                                          " extra gold. Thanks to your Trader!")
                                print("My gold: " + colored(str(player.gold), "yellow"))
                                break
                            print("You don't have that many")
                            break

                    elif buy_sell == "i":
                        self.display_vendor()

                    elif buy_sell == "q":
                        break

            elif choice == "rest":  # restoring energy
                if player.energy < 100:
                    print("\n" * 10)
                    display_rest()
                    print()
                    print("You are resting in this fancy bed!")
                    print("     min _________________________ max")
                    print("energy: |" + colored(str(int(player.energy / 4) * u"\u25A0"), "green"), end='')
                    while int(player.energy) <= 96:
                        time.sleep(0.5)  # every 0.5 seconds we add +4 to the current energy
                        player.energy += 4
                        print(colored(str(u"\u25A0"), "green"),
                              end='')  # with the "end=''" parameter the bar is adding up
                        if int(player.energy) > 96:
                            player.energy = 100
                    print()
                    print("Rise and Shine beautiful! You are rested!")
                    input(" ")
                else:
                    print("You are rested already... Go and kick some asses You lazy pig!")
                    input(" ")

            elif choice == "hire":
                display_crew()
                print("WOW! Your reputation precedes you! These villagers offer their services for you. (for 150 gold)")
                for villager in self.villagers:
                    print(villager, self.villagers[villager])
                print("current gold: " + colored(str(player.gold), "yellow"))
                chosen_companion = input("Type the name of the chosen companion!")
                if player.gold >= 150:
                    self.add_companion(chosen_companion)
                    player.gold -= 150
                    print(player.companions)
                else:
                    input("You don't have enough gold! Come back when You have 150 gold")

            elif choice == "q".lower():
                break

    def display_vendor(self):
        display_merchant()

        print("ITEM, AMOUNT, COST")
        for e in self.vendor.contents:
            print(str(e) + ",  " + str(int(e.price * 0.9) if "trader" in player.companions else e.price))

        print()
        print("My inventory:")
        for e in player.inventory.contents:
            print(str(e) + ",  " + str(int(e.price * 1.1) if "trader" in player.companions else e.price))

        print("My gold: " + colored(str(player.gold), "yellow"))
        if "trader" in player.companions:
            print("Because You have a Trader companion, You make better deals!")

    def add_companion(self, companion):
        if len(player.companions) >= 3:
            print("You cannot have more than 3 companions at a time")
        else:
            if companion in ["scout", "shaman", "wise"]:
                player.companions[companion] = self.villagers[companion]
                del self.villagers[companion]
                if companion == "scout":
                    scout()


class Sea(Terrain):
    def __init__(self):
        super().__init__(0, False, "T")


class Ship(Terrain):
    def __init__(self):
        super().__init__(0, True, "C")
        self.crew = {  # contains the rentable companions in the ship
                     "trader": "    10% price bonus for trading",
                     "soldier": "   Whiskey gives + 20% Energy",
                     "donkey": "    +2 inventory slots"
                    }

    def in_boat(self):
        while True:

            display_boat()
            choice = input("For resting type 'rest', for hiring 'hire' or hit 'Q' to leave the village ").lower()

            if choice == "rest":  # restoring energy
                if player.energy < 100:
                    print("\n" * 10)
                    display_rest()
                    print()
                    print("You are resting in this fancy bed!")
                    print("     min _________________________ max")
                    print("energy: |" + colored(str(int(player.energy / 4) * u"\u25A0"), "green"), end='')
                    while int(player.energy) <= 96:
                        time.sleep(0.5)  # every 0.5 seconds we add +4 to the current energy
                        player.energy += 4
                        print(colored(str(u"\u25A0"), "green"),
                              end='')  # with the "end=''" parameter the bar is adding up
                        if int(player.energy) > 96:
                            player.energy = 100
                    print()
                    print("Rise and Shine beautiful! You are rested!")
                    input(" ")
                else:
                    print("You are rested already... Go and kick some asses You lazy pig!")
                    input(" ")

            elif choice == "hire":
                display_crew()
                print("Some of your Crew members are ready to help you! for some gold... (150 each)")
                for crew_member in self.crew:
                    print(crew_member, self.crew[crew_member])
                print("current gold: " + colored(str(player.gold), "yellow"))
                chosen_companion = input("Type the name of the chosen companion!")
                if player.gold >= 150:
                    self.add_companion(chosen_companion)
                    player.gold -= 150
                    print(player.companions)
                else:
                    input("You don't have enough gold! Come back when You have 150 gold")

            elif choice == "q".lower():
                break

    def add_companion(self, companion):
        if len(player.companions) >= 3:
            print("You cannot have more than 3 companions at a time")
        else:
            if companion in ["trader", "soldier", "donkey"]:
                player.companions[companion] = self.crew[companion]
                del self.crew[companion]
                if companion == "donkey":
                    donkey()


class Lake(Terrain):
    def __init__(self):
        super().__init__(0, False, "V")


class Pyramid(Terrain):
    def __init__(self):
        super().__init__(0, True, "P")


class Mountain(Terrain):
    def __init__(self):
        super().__init__(0, False, "H")


class Meadow(Terrain):
    def __init__(self, cost=1):
        super().__init__(cost, True, ".")
        self.wet = False

    def if_wet(self):
        if self.wet:
            self.cost = 2


class Jungle(Terrain):
    def __init__(self, cost=3):
        super().__init__(cost, True, "J")
        self.wet = False

    def if_wet(self):
        if self.wet:
            self.cost = 6

    @staticmethod
    def attacked():
        fight_chance = random.randint(1, 100)
        if fight_chance <= 3:
            troll = Troll()
            display_troll()
            input("A jungle Troll attacked you! He is holding a " + str(troll.weapon[0]) + " in his hand!")
            fight(troll)


class Thicket(Terrain):
    def __init__(self, cost=2):
        super().__init__(cost, True, "R")
        self.wet = False

    def if_wet(self):
        if self.wet:
            self.cost = 4

    @staticmethod
    def attacked():
        fight_chance = random.randint(1, 100)
        if fight_chance <= 3:
            tiger = Tiger()
            display_tiger()
            input("A Prowling Tiger attacked you!")
            fight(tiger)


class Lava(Terrain):
    def __init__(self):
        super().__init__(10, True, "L")

    @staticmethod
    def damage():
        player.health_point -= 25


moves = 0
four_steps = []


class Altar(Terrain):
    def __init__(self):
        super().__init__(0, True, "O")
        self.empty = False

    def in_altar(self):
        # Altar: lootable treasure, 80% chance on catastrophe
        display_shrine()
        if self.empty:
            print("You have already cleared this shrine...")
        else:
            input("What do you do? loot the chest and face the consequences, or run away and never look back?")
            loot = input("type 'loot' or hit enter you run away... ")
            if loot == "loot":
                display_shrine_treasure()
                player.inventory.add_item(Treasure(1))
                curse_chance = random.randint(1, 101)  # 80% chance on a curse. If curse happens:
                if curse_chance <= 100:
                    player.energy -= 15
                    input("The chanthing stopped... but the earthquake got stronger... You looked up and...")
                    x = random.randint(1, 100)  # 35% chance on volcano curse, 65% chance on geyser curse
                    if x <= 35:
                        display_curse_volcano()
                        input("'What have I done?' You are thinking... but It's too late for regrets now...")
                        four_steps.append(moves)  # save current move number, so after 4 steps it can be used again.
                        curse_volcano(game_map, player.position)
                    else:
                        display_curse_geyser()
                        input("'What have I done?' You are thinking... but It's too late for regrets now...")
                        curse_geyser(game_map, player.position)

                else:
                    input("Next time You might not be this lucky...")

            else:
                input("hehe, Coward! xd")


class Sanctuary(Terrain):
    def __init__(self):
        super().__init__(0, True, "S")
        self.empty = False

    def in_sanctuary(self):
        #  lootable treasure, if rope in inventory its harmless, else 50% chance on catastrophe and 20 on curse
        if self.empty:
            input("You have already cleared this Sanctuary...")
        else:
            player.inventory.add_item(Treasure())

            if Rope() in player.inventory.contents:
                player.inventory.remove_item(Rope(1))
                print("You used up a rope to secure yourself on the cliff")
            else:
                bad_luck = random.randint(1, 101)
                if bad_luck <= 50:
                    input("Catastrophe will happen!")
                    catastrophe()

                elif 51 <= bad_luck <= 70:
                    input("Curse will happen!")
                    curse_chance = random.randint(1, 101)
                    if curse_chance <= 65:
                        display_curse_geyser()
                        curse_geyser(game_map, player.position)

                    else:
                        four_steps.append(moves)
                        display_curse_volcano()
                        curse_volcano(game_map, player.position)

                else:
                    input("Nothing will happen!")


class Cave(Terrain):
    def __init__(self):
        super().__init__(0, True, "B")
        self.empty = False

    def in_cave(self):
        # lootable treasure, if torch in inventory its harmless, else 65% chance on catastrophe
        if self.empty:
            input("You have already cleared this Cave...")
        else:
            player.inventory.add_item(Treasure())
            if Torch() in player.inventory.contents:
                player.inventory.remove_item(Torch(1))
                print("You burnt 1 torch in the Cave and avoided catastrophe")
            else:
                catastrophe_chance = random.randint(1, 101)
                if catastrophe_chance <= 65:
                    input('CATASTROOOPHE')  # not here
                    catastrophe()
                else:
                    input("you got lucky! catastrophe could have happened!")


Volcano_coordinate = []  # coordinates of H-s being changed to volcanos (@)
L_coordinate = []  # types and coordinates of terrains that are being changed to lava (L)


def curse_volcano(current_map, current_position):
    # turn the closest mountain to volcano, and the neighbour terrains to lava
    mountain_coordinates = []  # Actual coordinates of H-s, like : [3, 5]
    steps = []  # Number of steps between position and H, like: 5

    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == Mountain():
                mountain_coordinates.append([row_index, column_index])
                steps.append(sum([abs(current_position[0] - row_index), (abs(current_position[1] - column_index))]))

    h = mountain_coordinates[steps.index(min(steps))]  # coordinate of the closest H to our position

    current_map[h[0]][h[1]].icon = "@"  # Change the closest H to our position to @ (volcano)
    Volcano_coordinate.append([current_map.index(current_map[h[0]]), current_map.index(current_map[h[1]])])

    if h[0] - 1 > 0 and current_map[h[0] - 1][h[1]].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1]],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1]])])
        current_map[h[0] - 1][h[1]] = Lava()

    if h[0] + 1 < 15 and current_map[h[0] + 1][h[1]].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1]],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1]])])
        current_map[h[0] + 1][h[1]] = Lava()

    if h[1] - 1 > 0 and current_map[h[0]][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0]][h[1] - 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0]][h[1] - 1] = Lava()

    if h[1] + 1 < 15 and current_map[h[0]][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0]][h[1] + 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0]][h[1] + 1] = Lava()

    if h[0] - 1 > 0 and h[1] - 1 > 0 and current_map[h[0] - 1][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1] - 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0] - 1][h[1] - 1] = Lava()

    if h[0] + 1 < 15 and h[1] + 1 < 15 and current_map[h[0] + 1][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1] + 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0] + 1][h[1] + 1] = Lava()

    if h[0] - 1 > 0 and h[1] + 1 < 15 and current_map[h[0] - 1][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1] + 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] + 1])])
        current_map[h[0] - 1][h[1] + 1] = Lava()

    if h[0] + 1 < 15 and h[1] - 1 > 0 and current_map[h[0] + 1][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1] - 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] - 1])])
        current_map[h[0] + 1][h[1] - 1] = Lava()


def volcano_back(current_map):
    # turn back the lava terrain to plain ground
    for e in L_coordinate:
        current_map[e[1]][e[2]] = Meadow()


def curse_geyser(current_map, current_position):
    # turns lakes into geysers, and turns neighboring terrain wet.
    lake_coordinates = []  # Actual coordinates of V-s, las list coordinates [x,y]
    steps = []  # Number of steps between position and V, as int

    for row_index, row in enumerate(current_map):  # <- with the enumerate, I can get the indexes
        for column_index, column in enumerate(row):  # <- with the enumerate, I can get the indexes
            if column == Lake():
                lake_coordinates.append([row_index, column_index])
                steps.append(sum([abs(current_position[0] - row_index), (abs(current_position[1] - column_index))]))

    w = lake_coordinates[steps.index(min(steps))]  # coordinate of the closest V to our position

    current_map[w[0]][w[1]].icon = "G"  # change the closest V's icon to G

    coordinate_number = (0, 1, 2)

    for num1 in coordinate_number:
        for num2 in coordinate_number:
            try:
                if current_map[w[0] + num1][w[1] + num2].icon in ".RFJ":
                    current_map[w[0] + num1][w[1] + num2].wet = True
            except IndexError:
                continue

            try:
                if current_map[w[0] + num1][w[1] - num2].icon in ".RFJ":
                    current_map[w[0] + num1][w[1] - num2].wet = True
            except IndexError:
                continue

            try:
                if current_map[w[0] - num1][w[1] + num2].icon in ".RFJ":
                    current_map[w[0] - num1][w[1] + num2].wet = True
            except IndexError:
                continue

            try:
                if current_map[w[0] - num1][w[1] - num2].icon in ".RFJ":
                    current_map[w[0] - num1][w[1] - num2].wet = True
            except IndexError:
                continue


def catastrophe():
    # 70% chance on 35 energy loss, 10% chance on injury, 20% that a companion immediately leaves the group (traitor).

    x = random.randint(1, 101)

    if x <= 65:

        input("You lost 35 energy!")
        player.energy -= 35

    elif 80 > x > 65:
        if len(player.companions) != 0:
            player.injured = True
            companion = random.choice(list(player.companions))
            player.injured_companions[companion] = "    ~ Injured ~ :("
            del player.companions[companion]
            input("Oh no! Your " + companion + " companion got injured... There is a chance he can't keep up...")
            if companion == "scout":
                scout_out()
            if companion == "donkey":
                donkey_out()

    else:
        if len(player.companions) != 0:
            traitor()


def traitor():
    # a companion leaves the group and steals an item from inventory
    companion = random.choice(list(player.companions))
    item = random.choice(list(player.inventory.contents))
    if item == Treasure():
        input("Your " + companion + " companion betrayed you! He took the " + item + " and run away with it...")
    else:
        input("Your " + companion + " companion betrayed you! He left your group and stole 1 " + item +
              " from you backpack...")
    del player.companions[companion]
    player.inventory.remove_item(item(1))
