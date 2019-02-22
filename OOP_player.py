import random
from copy import copy
from OOP_village_items import Whiskey, Chocolate, Fruit, Meat, Medicine, Torch, Rope
from OOP_displays import display_bag
from termcolor import colored
import time


class Player:

    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.gold = 250
        self.inventory = Inventory()
        self.companions = {}
        self.injured = False
        self.injured_companions = {}
        self._lives = 3
        self.health_point = 100
        self.mana_point = 5
        self.alive = True
        self.position = [0, 0]
        self.sight = [0, 1]

    def get_lives(self):
        return self._lives

    def get_hp(self):
        return self.health_point

    def lose_companion(self, companion):
        del self.companions[companion]

    def take_dmg(self, dmg):
        remaining_hp = self.health_point - dmg
        if remaining_hp > 0:
            self.health_point -= dmg
            print("Ouch, " + self.name + " took " + colored(str(dmg), "red") + "damage")
            time.sleep(2.5)
        else:
            self.health_point = 0
            self.alive = False

    def deal_dmg(self, enemy):
        while True:
            attack = input("type 'sword' for a melee attack or 'firebolt' for spellcasting")
            if attack == "firebolt":
                print(self.name + " is casting a firebolt")
                time.sleep(2.5)
                enemy.take_dmg(self.firebolt())
                time.sleep(2.5)
                break
            elif attack == "sword":
                print(self.name + " is swinging his sword")
                time.sleep(2.5)
                enemy.take_dmg(self.sword())
                time.sleep(2.5)
                break

    def firebolt(self):
        if self.mana_point > 0:
            self.mana_point -= 1
            return random.randint(6, 15)
        else:
            print("Not enough mana!")

    def sword(self):
        self.energy -= 3
        return random.randint(3, 8)

    def display_inventory(self):
        # display inventory, shows free slots or excess item number, prints energy bar,
        # allow the player to consume food or drink to restore energy
        display_bag()
        if len(self.inventory.contents) > self.inventory.slot_limit:
            print(str(len(self.inventory.contents)) + " out of " + str(self.inventory.slot_limit) + ". You are carrying"
                  + str(len(self.inventory.contents) - self.inventory.slot_limit) + "extra items in your hand.")
        else:
            print(str(len(self.inventory.contents)) + " out of " + str(self.inventory.slot_limit) + ". You have " +
                  str(self.inventory.slot_limit - len(self.inventory.contents)) + " free slots left.")
        for e in self.inventory.contents:
            print(str(e) + e.usage)  # print inventory elements if have any of it.

        if "soldier" in self.companions:
            print("Because you have a Soldier companion, you get extra 20% energy when drinking whiskey")
        if "shaman" in self.companions:
            print("Because you have a Shaman companion, you get extra 20% energy when using medicine")

        self.consume_food()

    def consume_food(self):
        while True:
            print("     min _________________________ max")
            print("energy: |" + colored(str(int(self.energy / 4) * u"\u25A0"), "green"))

            if "soldier" in self.companions:
                print("Because you have a Soldier companion, you get extra 20% energy when drinking whiskey")
            if "shaman" in self.companions:
                print("Because you have a Shaman companion, you get extra 20% energy when using medicine")

            food = input("choose food or drink to consume for energy or press 'Q' to exit: \n")
            if food == "q".lower():
                break
            else:
                amount = input("How many would you like to eat/drink?")
                try:
                    if food == "whiskey".lower():
                        food = Whiskey(int(amount))
                        success = self.inventory.remove_item(food)
                        if success:
                            self.energy += food.energy_bonus * 1.2 * int(amount) if "soldier" in self.companions \
                                else food.energy_bonus * int(amount)
                            if self.energy > 100:
                                self.energy = 100

                    elif food == "medicine".lower():
                        food = Medicine(int(amount))
                        success = self.inventory.remove_item(food)
                        if success:
                            self.energy += food.energy_bonus * 1.2 * int(amount) if "shaman" in self.companions \
                                else food.energy_bonus * int(amount)
                            if self.energy > 100:
                                self.energy = 100

                    elif food == "meat".lower():
                        food = Meat(int(amount))
                        success = self.inventory.remove_item(food)
                        if success:
                            self.energy += food.energy_bonus * int(amount)
                            if self.energy > 100:
                                self.energy = 100

                    elif food == "chocolate".lower():
                        food = Chocolate(int(amount))
                        success = self.inventory.remove_item(food)
                        if success:
                            self.energy += food.energy_bonus * int(amount)
                            if self.energy > 100:
                                self.energy = 100

                    elif food == "fruit".lower():
                        food = Fruit(int(amount))
                        success = self.inventory.remove_item(food)
                        if success:
                            self.energy += food.energy_bonus * int(amount)
                            if self.energy > 100:
                                self.energy = 100

                    else:
                        print("You don't have that in your inventory")
                except ValueError:
                    print("Enter a valid number!")

    def injury(self):
        companion = random.choice(self.injured_companions)
        print("Your " + companion + " can't keep up because of his injuries. He leaves your group!")
        del self.injured_companions[companion]
        if len(self.injured_companions) == 0:
            self.injured = False

    def __str__(self):
        return self.name + "   " + str(self.energy) + " energy   " + str(self.gold) + " gold   inv:" \
               + str(self.inventory.contents)


class Inventory:
    def __init__(self):
        self.stack_limit = 10
        self.slot_limit = 8
        self.contents = [Whiskey(5), Meat(5), Rope(2), Torch(2)]

    def add_item(self, it):
        item = copy(it)
        if item in self.contents:
            for current in reversed(self.contents):
                if current == item:
                    while item.pieces > 0:
                        diff = min(self.stack_limit - current.pieces, item.pieces)
                        if item.pieces > diff:
                            current.pieces += diff
                            item.pieces -= diff
                            new_item = copy(item)
                            new_item.pieces = 0
                            current = new_item
                            self.contents.append(new_item)
                        elif item.pieces > 0:
                            current.pieces += item.pieces
                            item.pieces = 0
        else:
            while item.pieces > 0:
                diff = min(self.stack_limit, item.pieces)

                new_item = copy(item)
                new_item.pieces = 0
                self.contents.append(new_item)

                if item.pieces > diff:
                    new_item.pieces += diff
                    item.pieces -= diff
                elif item.pieces > 0:
                    new_item.pieces += item.pieces
                    item.pieces = 0

    def remove_item(self, it):
        item = copy(it)
        current_amount = 0
        if item in self.contents:
            for current in self.contents:
                if current == item:
                    current_amount += current.pieces

            if current_amount >= item.pieces:
                for current in reversed(self.contents):
                    if current == item:
                        while item.pieces > 0 and current.pieces > 0:
                            diff = min(current.pieces, item.pieces)
                            if item.pieces >= current.pieces:
                                self.contents.reverse()
                                self.contents.remove(current)
                                self.contents.reverse()
                                item.pieces -= diff
                                current.pieces = 0
                            elif item.pieces > 0:
                                current.pieces -= item.pieces
                                item.pieces = 0
                return True
            else:
                print("You don't have that many!")
                return False
        else:
            print("You don't have that item in your inventory!")
            return False


def scout():
    player.sight.append(2)


def scout_out():
    player.sight.remove(2)


def donkey():
    # If donkey chosen as companion, increase inventory slots
    player.inventory.slot_limit += 2


def donkey_out():
    # If donkey leaves the group, change back inventory slots to original
    player.inventory.slot_limit -= 2


def fight(enemy):

    while player.alive and enemy.alive and player.energy > 0:
        print("\n" * 30)
        print("     Endron:                                            " + enemy.name + ":")
        print("     min _________________________ max                  min _________________________ max")
        print("HP:     |" + colored(str(int(player.health_point // 4) * u"\u25A0"), "green") +
              str(int(player.health_point)) + (" " * (100//4 - player.health_point // 4)) + "                        " +
              colored(str(int(enemy.health_point // 4) * u"\u25A0"), "green") + str(int(enemy.health_point)))
        print("energy: |" + colored(str(int(player.energy // 4) * u"\u25A0"), "yellow") + str(int(player.energy)))
        print("Mana:   |" + colored(str(int(player.mana_point) * ("|" + u"\u25A0" + "|")), "blue") + str(
            int(player.mana_point)))

        player.deal_dmg(enemy)
        enemy.deal_dmg(player)


player = Player("Endron")
print(player.name, player.health_point, "hp")
