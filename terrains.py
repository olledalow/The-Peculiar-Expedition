import time
import random


from village_items import Treasure, Rope, Torch, Vendor, Emerald
from player import player, Whiskey, Elixir, Meat, Medicine, Fruit, scout, scout_out, donkey, donkey_out, fight
from map_coordinates import game_map
from monsters import Troll, Tiger, Crocolisk, Bandit, Dragon
from images import *


class Terrain:
    def __init__(self, cost, step, icon, fog_image, image, action_image, label, coordinate):
        self.name = str(type(self).__name__)
        self.cost = cost
        self.step = step
        self.icon = icon
        self.fog_image = fog_image
        self.image = image
        self.action_image = action_image
        self.label = label
        self.coordinate = coordinate
        self.monsters = []
        self.actual_image = fog_image

    def __eq__(self, other):
        return type(self) == type(other)


class Village(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(cost=0, step=True, icon="F", fog_image=tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         image=tk.PhotoImage(file='GAME_IMAGES/village.png'), action_image=in_village,
                         label="label_will_be_assigned_here", coordinate=coordinate)
        self.villagers = {  # contains the rentable companions in the village
                          "scout": "  +1 vision",
                          "shaman": " Medicine gives +20% health points, heals you in combat",
                          "wise": "   +100 gold on new maps"
                         }
        self.vendor = Vendor()

    def buy(self, item):

        if item == "elixir":
            item = Elixir(1)
        elif item == "meat":
            item = Meat(1)
        elif item == "whiskey":
            item = Whiskey(1)
        elif item == "medicine":
            item = Medicine(1)
        elif item == "fruit":
            item = Fruit(1)
        elif item == "rope":
            item = Rope(1)
        elif item == "torch":
            item = Torch(1)
        else:
            item = None
            print("VILLAGE_SELF NOT ASSOCIATED AN ITEM. REKT.")

        if item is not None:
            for element in self.vendor.contents:
                if element.price <= player.gold:
                    self.vendor.sell_item(item)
                    player.inventory.add_item(item)
                    player.gold -= item.pieces * int(element.price * 0.9) \
                        if "trader" in player.companions else item.pieces * element.price
                    if "trader" in player.companions:
                    #     print("You saved " +
                    #           colored(str((item.pieces * element.price) -
                    #                       int(item.pieces * element.price * 0.9)), "yellow") +
                    #           " gold. Thanks to your Trader!")
                    # print("My gold: " + colored(str(player.gold), "yellow"))
                        pass
                    break
                print("Not enough item or gold.")
                break

    @staticmethod
    def sell(item):

        if item == "elixir":
            item = Elixir(1)
        elif item == "meat":
            item = Meat(1)
        elif item == "whiskey":
            item = Whiskey(1)
        elif item == "medicine":
            item = Medicine(1)
        elif item == "fruit":
            item = Fruit(1)
        elif item == "rope":
            item = Rope(1)
        elif item == "torch":
            item = Torch(1)
        elif item == "treasure":
            item = Treasure(1)
        else:
            item = None
            print("VILLAGE_SELF NOT ASSOCIATED AN ITEM. REKT.")

        for element in player.inventory.contents:
            if item == element:
                if item.pieces <= element.pieces:
                    player.inventory.remove_item(item)
                    print()
                    player.gold += item.pieces * int(item.price * 1.1) \
                        if "trader" in player.companions else item.pieces * element.price

                    if "trader" in player.companions:
                    #     print("You earned " +
                    #           colored(str(int(item.pieces * element.price * 1.1) -
                    #                       (item.pieces * element.price)), "yellow") +
                    #           " extra gold. Thanks to your Trader!")
                    # print("My gold: " + colored(str(player.gold), "yellow"))
                        pass
                    break
                print("You don't have that many")
                break

    @staticmethod
    def rest():
        player.energy += 4
        if int(player.energy) > 96:
            player.energy = 100

    # def display_vendor(self):
    #     print("ITEM, AMOUNT, COST")
    #     for e in self.vendor.contents:
    #         print(str(e) + ",  " + str(int(e.price * 0.9) if "trader" in player.companions else e.price))
    #
    #     print()
    #     print("My inventory:")
    #     for e in player.inventory.contents:
    #         print(str(e) + ",  " + str(int(e.price * 1.1) if "trader" in player.companions else e.price))
    #
    #     print("My gold: " + colored(str(player.gold), "yellow"))
    #     if "trader" in player.companions:
    #         print("Because You have a Trader companion, You make better deals!")

    def add_companion(self, companion):
        try:
            if len(player.companions) >= 3 or companion in player.companions or player.gold < 150:
                return "You cannot have more than 3 companions at a time"
            else:
                player.companions[companion] = self.villagers[companion]
                player.gold -= 150
                del self.villagers[companion]
                if companion == "scout":
                    scout()
        except KeyError:
            pass


class Sea(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, False, "T", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/sea.png"), "none", "label_will_be_assignes_here", coordinate)


class Ship(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, True, "C", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/ship.png"), in_ship, "label_will_be_assignes_here", coordinate)
        self.crew = {  # contains the rentable companions in the ship
                     "trader": "    10% price bonus for trading",
                     "soldier": "   Whiskey gives + 20% Energy, fight beside you in combat",
                     "donkey": "    +2 inventory slots"
                    }

    def in_boat(self):
        if Emerald() in player.inventory.contents:
            pass
        else:
            while True:
                # clear_screen()
                # display_boat()
                choice = input("For resting type 'rest', for hiring 'hire' or hit 'Q' to leave the Ship ").lower()

                if choice == "rest":  # restoring energy
                    # clear_screen()
                    if player.energy < 100:
                        print("\n" * 10)
                        # display_rest()
                        print()
                        print("You are resting in this fancy bed!")
                        print("     min _________________________ max")
                        # print("energy: |" + colored(str(int(player.energy / 4) * u"\u25A0"), "green"), end='')
                        while int(player.energy) <= 96:
                            time.sleep(0.5)  # every 0.5 seconds we add +4 to the current energy
                            player.energy += 4
                            # print(colored(str(u"\u25A0"), "green"),
                            #       end='')  # with the "end=''" parameter the bar is adding up
                            if int(player.energy) > 96:
                                player.energy = 100
                        print()
                        print("Rise and Shine beautiful! You are rested!")
                        input(" ")
                    else:
                        print("You are rested already... Go and kick some asses You lazy pig!")
                        input(" ")

                elif choice == "hire":
                    # clear_screen()
                    # display_crew()
                    print("Some of your Crew members are ready to help you! for some gold... (150 each)")
                    for crew_member in self.crew:
                        print(crew_member, self.crew[crew_member])
                    # print("current gold: " + colored(str(player.gold), "yellow"))
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
        try:
            if len(player.companions) >= 3 or companion in player.companions or player.gold < 150:
                return "You cannot have more than 3 companions at a time"
            else:
                player.companions[companion] = self.crew[companion]
                player.gold -= 150
                del self.crew[companion]
                if companion == "donkey":
                    donkey()
        except KeyError:
            pass


class Lake(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, False, "V", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/lake.png"), "none", "label_will_be_assignes_here", coordinate)


class Pyramid(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, True, "P", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/pyramid.png"), in_pyramid, "label_will_be_assignes_here",
                         coordinate)
        self.empty = False
        self.adventure1_img = pyramid_adventure1
        self.adventure2_img = pyramid_adventure2
        self.adventure3_img = pyramid_adventure3
        self.adventure4_img = pyramid_adventure4
        self.adventure5_img = pyramid_adventure5
        self.monsters = [Dragon]

    @staticmethod
    def use_needed_item():
        pass

    @staticmethod
    def luck_chance():
        catastrophe_chance = random.randint(0, 100)
        if catastrophe_chance <= 80:
            catastrophe_text = catastrophe()
            return False, catastrophe_text
        else:
            return True, "You go past the ancient tomb quickly, and quitely..."

    def attacked(self):
        monster = self.monsters[0]()
        return monster


class Mountain(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, False, "H", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/mountain.png"), "none", "label_will_be_assignes_here",
                         coordinate)


wet_lands = []


class Meadow(Terrain):
    def __init__(self, cost=1, coordinate=(0, 0)):
        super().__init__(cost, True, ".", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/meadow.png"), in_meadow, "label_will_be_assignes_here",
                         coordinate)
        self.wet = False
        self.monsters = [Bandit, Crocolisk]

    def if_wet(self):
        if self.wet:
            self.cost = 2
            if self.actual_image == self.image:
                self.actual_image = tk.PhotoImage(file='GAME_IMAGES/wet_meadow.png')
            else:
                self.image = tk.PhotoImage(file='GAME_IMAGES/wet_meadow.png')

    def attacked(self):
        fight_chance = random.randint(1, 100)
        threshold = 15 if self.wet else 3
        monster_type = 1 if self.wet else 0

        if fight_chance <= threshold:
            monster = self.monsters[monster_type]()
            if monster_type == 0:
                # display_bandit()
                pass
            else:
                # display_crocolisk()
                pass
            input("A " + monster.name + " attacked you!")
            fight(monster)


class Jungle(Terrain):
    def __init__(self, cost=3, coordinate=(0, 0)):
        super().__init__(cost, True, "J", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/jungle.png"), in_jungle, "label_will_be_assignes_here",
                         coordinate)
        self.wet = False
        self.monsters = [Troll, Crocolisk]

    def if_wet(self):
        if self.wet:
            self.cost = 6
            if self.actual_image == self.image:
                self.actual_image = tk.PhotoImage(file='GAME_IMAGES/wet_jungle.png')
            else:
                self.image = tk.PhotoImage(file='GAME_IMAGES/wet_jungle.png')

    def attacked(self):
        fight_chance = random.randint(1, 100)
        threshold = 30 if self.wet else 3
        monster_type = 1 if self.wet else 0

        if fight_chance <= threshold:
            monster = self.monsters[monster_type]()
            if monster_type == 0:
                pass
                # display_troll()
            else:
                pass
                # display_crocolisk()
            input("A " + monster.name + " attacked you!")
            fight(monster)


class Thicket(Terrain):
    def __init__(self, cost=2, coordinate=(0, 0)):
        super().__init__(cost, True, "R", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/thicket.png"), in_thicket, "label_will_be_assignes_here",
                         coordinate)
        self.wet = False
        self.monsters = [Tiger, Crocolisk]

    def if_wet(self):
        if self.wet:
            self.cost = 4
            if self.actual_image == self.image:
                self.actual_image = tk.PhotoImage(file='GAME_IMAGES/wet_thicket.png')
            else:
                self.image = tk.PhotoImage(file='GAME_IMAGES/wet_thicket.png')

    def attacked(self):
        fight_chance = random.randint(1, 100)
        threshold = 20 if self.wet else 3
        monster_type = 1 if self.wet else 0

        if fight_chance <= threshold:
            monster = self.monsters[monster_type]()
            if monster_type == 0:
                pass
                # display_tiger()
            else:
                pass
                # display_crocolisk()
            input("A " + monster.name + " attacked you!")
            fight(monster)


class Lava(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(10, True, "L", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/lava.png"), in_lava, "label_will_be_assignes_here",
                         coordinate)

    @staticmethod
    def damage():
        player.health_point -= 15


class Altar(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, True, "O", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/altar.png"), in_altar, "label_will_be_assignes_here",
                         coordinate)
        self.empty = False
        self.adventure1_img = altar_adventure1
        self.adventure2_lucky_img = altar_adventure2_lucky
        self.adventure3_lucky_img = altar_adventure3_lucky
        self.adventure4_lucky_img = altar_adventure4_lucky
        self.adventure5_lucky_img = altar_adventure5_lucky
        self.adventure2_not_lucky_img = altar_adventure2_lucky
        self.adventure3_not_lucky_img = altar_adventure3_not_lucky
        self.adventure4_not_lucky_img = altar_adventure4_not_lucky
        self.adventure5_not_lucky_img = altar_adventure5_not_lucky

    @staticmethod
    def luck_chance():
        curse_chance = random.randint(0, 100)
        if curse_chance <= 40:
            curse_text = curse_volcano(game_map, player.position)
            return False, curse_text
        elif 40 < curse_chance <= 80:
            curse_text = curse_volcano(game_map, player.position)
            return False, curse_text
        else:
            return True, "You go past the ancient tomb quickly, and quitely... You reckon' you didn't disturbed the" \
                         " resting spirits..."


class Sanctuary(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, True, "S", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/sanctuary.png"), in_sanctuary, "label_will_be_assignes_here",
                         coordinate)
        self.empty = False
        self.adventure1_img = sanctuary_adventure1
        self.adventure2_img = sanctuary_adventure2
        self.adventure3_img = sanctuary_adventure3
        self.adventure4_img = sanctuary_adventure4
        self.adventure5_img = sanctuary_adventure5
        self.adventure2_lucky_img = sanctuary_adventure2_lucky
        self.adventure3_lucky_img = sanctuary_adventure3_lucky
        self.adventure4_lucky_img = sanctuary_adventure4_lucky
        self.adventure5_lucky_img = sanctuary_adventure5_lucky
        self.adventure2_not_lucky_img = sanctuary_adventure2_catastrophe
        self.adventure3_not_lucky_img = sanctuary_adventure3_not_lucky
        self.adventure4_not_lucky_img = sanctuary_adventure4_not_lucky
        self.adventure5_not_lucky_img = sanctuary_adventure5_not_lucky

    @staticmethod
    def use_needed_item():
        player.inventory.remove_item(Rope(1))

    @staticmethod
    def luck_chance():
        catastrophe_chance = random.randint(0, 100)
        if catastrophe_chance <= 40:
            catastrophe_text = catastrophe()
            return False, catastrophe_text
        elif 40 < catastrophe_chance <= 60:
            curse_text = curse_geyser(game_map, player.position)
            return False, curse_text
        elif 60 < catastrophe_chance <= 80:
            curse_text = curse_volcano(game_map, player.position)
            return False, curse_text
        else:
            return True, "You found a secret passage up to the Sanctuary..."


class Cave(Terrain):
    def __init__(self, coordinate=(0, 0)):
        super().__init__(0, True, "B", tk.PhotoImage(file='GAME_IMAGES/fog.png'),
                         tk.PhotoImage(file="GAME_IMAGES/cave.png"), in_cave, "label_will_be_assignes_here", coordinate)
        self.empty = False
        self.adventure1_img = cave_adventure1
        self.adventure2_img = cave_adventure2
        self.adventure3_img = cave_adventure3
        self.adventure4_img = cave_adventure4
        self.adventure5_img = cave_adventure5
        self.adventure2_lucky_img = cave_adventure2_lucky
        self.adventure3_lucky_img = cave_adventure3_lucky
        self.adventure4_lucky_img = cave_adventure4_lucky
        self.adventure5_lucky_img = cave_adventure5_lucky
        self.adventure2_not_lucky_img = cave_adventure2_not_lucky
        self.adventure3_not_lucky_img = cave_adventure3_not_lucky
        self.adventure4_not_lucky_img = cave_adventure4_not_lucky
        self.adventure5_not_lucky_img = cave_adventure5_not_lucky

    @staticmethod
    def use_needed_item():
        player.inventory.remove_item(Torch(1))

    @staticmethod
    def luck_chance():
        catastrophe_chance = random.randint(0, 100)
        if catastrophe_chance <= 65:
            catastrophe_text = catastrophe()
            return False, catastrophe_text
        else:
            return True, "The Cave is so dark that You can't see anything. You are touching the wall to navigate..."


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
    current_map[h[0]][h[1]].image = tk.PhotoImage(file="GAME_IMAGES/volcano.png")
    current_map[h[0]][h[1]].actual_image = current_map[h[0]][h[1]].image
    Volcano_coordinate.append([current_map.index(current_map[h[0]]), current_map.index(current_map[h[1]])])

    if h[0] - 1 > 0 and current_map[h[0] - 1][h[1]].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1]],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1]])])

        current_map[h[0] - 1][h[1]] = \
            Lava(coordinate=(current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1]])))

        current_map[h[0] - 1][h[1]].actual_image = current_map[h[0] - 1][h[1]].image

    if h[0] + 1 < 15 and current_map[h[0] + 1][h[1]].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1]],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1]])])

        current_map[h[0] + 1][h[1]] = \
            Lava(coordinate=(current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1]])))

        current_map[h[0] + 1][h[1]].actual_image = current_map[h[0] + 1][h[1]].image

    if h[1] - 1 > 0 and current_map[h[0]][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0]][h[1] - 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] - 1])])

        current_map[h[0]][h[1] - 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] - 1])))

        current_map[h[0]][h[1] - 1].actual_image = current_map[h[0]][h[1] - 1].image

    if h[1] + 1 < 15 and current_map[h[0]][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0]][h[1] + 1],
                             current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] + 1])])

        current_map[h[0]][h[1] + 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0]]), current_map.index(current_map[h[1] + 1])))

        current_map[h[0]][h[1] + 1].actual_image = current_map[h[0]][h[1] + 1].image

    if h[0] - 1 > 0 and h[1] - 1 > 0 and current_map[h[0] - 1][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1] - 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] - 1])])

        current_map[h[0] - 1][h[1] - 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] - 1])))

        current_map[h[0] - 1][h[1] - 1].actual_image = current_map[h[0] - 1][h[1] - 1].image

    if h[0] + 1 < 15 and h[1] + 1 < 15 and current_map[h[0] + 1][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1] + 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] + 1])])

        current_map[h[0] + 1][h[1] + 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] + 1])))

        current_map[h[0] + 1][h[1] + 1].actual_image = current_map[h[0] + 1][h[1] + 1].image

    if h[0] - 1 > 0 and h[1] + 1 < 15 and current_map[h[0] - 1][h[1] + 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] - 1][h[1] + 1],
                             current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] + 1])])

        current_map[h[0] - 1][h[1] + 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0] - 1]), current_map.index(current_map[h[1] + 1])))

        current_map[h[0] - 1][h[1] + 1].actual_image = current_map[h[0] - 1][h[1] + 1].image

    if h[0] + 1 < 15 and h[1] - 1 > 0 and current_map[h[0] + 1][h[1] - 1].icon not in "TVSHOB":
        L_coordinate.append([current_map[h[0] + 1][h[1] - 1],
                             current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] - 1])])

        current_map[h[0] + 1][h[1] - 1] = \
            Lava(coordinate=(current_map.index(current_map[h[0] + 1]), current_map.index(current_map[h[1] - 1])))

        current_map[h[0] + 1][h[1] - 1].actual_image = current_map[h[0] + 1][h[1] - 1].image

    game_map[player.position[0]][player.position[1]].adventure2_not_lucky_img = sanctuary_adventure2_curse_volcano
    return "You walked into an ancient and sacred place... And the spirits are not happy about it..." \
           "The air is filled with smoke... The ground starts shaking beneath your legs..." \
           "As you look around you see that the closest mountain turned into a volcano..."


# def volcano_back(current_map):
#     # turn back the lava terrain to plain ground
#     for e in L_coordinate:
#         current_map[e[1]][e[2]] = Meadow()


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
                if current_map[w[0] + num1][w[1] + num2].icon in ".RJ":
                    current_map[w[0] + num1][w[1] + num2].wet = True
                    current_map[w[0] + num1][w[1] + num2].if_wet()
            except IndexError:
                continue

            try:
                if current_map[w[0] + num1][w[1] - num2].icon in ".RJ":
                    current_map[w[0] + num1][w[1] - num2].wet = True
                    current_map[w[0] + num1][w[1] - num2].if_wet()
            except IndexError:
                continue

            try:
                if current_map[w[0] - num1][w[1] + num2].icon in ".RJ":
                    current_map[w[0] - num1][w[1] + num2].wet = True
                    current_map[w[0] - num1][w[1] + num2].if_wet()
            except IndexError:
                continue

            try:
                if current_map[w[0] - num1][w[1] - num2].icon in ".RJ":
                    current_map[w[0] - num1][w[1] - num2].wet = True
                    current_map[w[0] - num1][w[1] - num2].if_wet()
            except IndexError:
                continue

    game_map[player.position[0]][player.position[1]].adventure2_not_lucky_img = sanctuary_adventure2_curse_geyser
    return "You entered a sacred place... And you disturbed it... The ground starts shaking beneath you... " \
           "As you look around you see a great pillar of water shooting towards the sky from the nearest lake..."


def catastrophe():
    # 50% chance on energy loss, 25% chance on injury, 25% that a companion immediately leaves the group (traitor).

    x = random.randint(0, 100)
    print("CATASTROPHE " + str(x))
    if x <= 50:
        energy_loss = random.randint(15, 35)
        player.energy -= energy_loss
        if game_map[player.position[0]][player.position[1]].icon == "C":
            return "You got lost in the dark caverns, going in circles... You lost " + str(energy_loss) + " energy..."
        elif game_map[player.position[0]][player.position[1]].icon == "O":
            return "You hear something moving in the shadows... Something creeping in the tomb. As you run as fast" \
                   " as you can you lost " + str(energy_loss) + " energy..."
        else:
            return "The way up without a rope is very hard... As You climb you lost " + str(energy_loss) + " energy..."

    elif 75 > x > 50:
        if len(player.companions) != 0:
            player.injured = True
            companion = random.choice(list(player.companions))
            player.injured_companions[companion] = "    ~ Injured ~ :("
            del player.companions[companion]
            if companion == "scout":
                scout_out()
            if companion == "donkey":
                donkey_out()
            return "Oh no! Your " + companion + " companion got injured... You knew this place could be dangerous, " \
                                                "but you kept on going anyway... There is a chance he can't keep up..."
        else:
            energy_loss = random.randint(15, 35)
            player.energy -= energy_loss
            if game_map[player.position[0]][player.position[1]].icon == "C":
                return "You got lost in the dark caverns, going in circles... You lost " + str(energy_loss) +\
                       " energy..."
            elif game_map[player.position[0]][player.position[1]].icon == "O":
                return "You hear something moving in the shadows... Something creepying in the tomb." \
                       " As you run as fast as you can you lost " + str(energy_loss) + " energy..."
            else:
                return "The way up without a rope is very hard... As You climb you lost " + str(energy_loss) +\
                       " energy..."
    else:
        if len(player.companions) != 0:
            return traitor()


def traitor():
    # a companion leaves the group and steals an item from inventory
    companion = random.choice(list(player.companions))
    item = random.choice(list(player.inventory.contents))
    del player.companions[companion]
    player.inventory.remove_item(item)
    return " You came to a very dangerous place...  Your " + companion + " companion got enough of it and betrayed " \
                                                                         "you! He left your group and stole 1 " \
           + item.name + " from you backpack..."
