from GAME_displays import display_village, display_rest, display_crew, display_merchant
from OOP_village import Vendor
from OOP_player import player, Whiskey, Chocolate, Meat, Medicine, Fruit
from termcolor import colored
import time


class Terrain:
    def __init__(self, cost, step, icon):
        self._step = step
        self._cost = cost
        self.icon = icon


class Village(Terrain):
    def __init__(self):
        super().__init__(0, True, "F")
        self.villagers = {  # contains the rentable companions in the village
                          "scout": "  + 1 vision",
                          "shaman": " Medicine gives +20% energy",
                          "wise": "   + 3 reputation on new maps"
                         }

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

                        for element in current_vendor.contents:
                            if item.pieces <= element.pieces and item.pieces * element.price <= player.gold:
                                current_vendor.sell_item(item)
                                print()
                                player.inventory.add_item(item)
                                player.gold -= item.pieces * int(element.price * 0.9) \
                                    if "trader" in player.companions else element.price
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
                            item = Fruit(int(input("how many would you like to buy? (enter a number) ")))
                        else:
                            print("You don't have that in your Inventory")
                            break

                        for element in player.inventory.contents:
                            if item.pieces <= element.pieces:
                                player.inventory.sell_item(item)
                                print()
                                player.gold += item.pieces * int(element.price * 1.1) \
                                    if "trader" in player.companions else element.price
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
                print("WOW! Your reputation precedes you! These villagers offer their services for you:")
                for villager in self.villagers:
                    print(villager, self.villagers[villager])
                chosen_companion = input("Type the name of the chosen companion!")
                player.add_companion(chosen_companion)
                print(player.companions)

            elif choice == "q".lower():
                break

    def display_vendor(self):
        display_merchant()

        print("ITEM, AMOUNT, COST")
        for e in current_vendor.contents:
            print(str(e) + ",  " + str(int(e.price * 0.9) if "trader" in player.companions else e.price))

        print()
        print("My inventory:")
        for e in player.inventory.contents:
            print(str(e) + ",  " + str(int(e.price * 1.1) if "trader" in player.companions else e.price))

        print("My gold: " + colored(str(player.gold), "yellow"))
        if "trader" in player.companions:
            print("Because You have a Trader companion, You make better deals!")


current_vendor = Vendor()
print(current_vendor)
