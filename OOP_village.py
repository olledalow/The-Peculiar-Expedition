from copy import copy


class Item:
    def __init__(self, pieces, price, energy_bonus):
        self.pieces = pieces
        self.price = price
        self.energy_bonus = energy_bonus

    def __eq__(self, other):
        return type(self) == type(other)

    def __repr__(self):
        return str(type(self).__name__) + " " + str(self.pieces)


class Chocolate(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 50, 20)


class Fruit(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 45, 15)


class Meat(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 60, 25)


class Whiskey(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 50, 20)


class Medicine(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 50, 20)


class Vendor:
    def __init__(self):
        self.contents = [Whiskey(5), Meat(10), Fruit(10), Medicine(10), Chocolate(2)]

    def sell_item(self, it):
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


villagers = {  # contains the rentable companions in the village
    "scout": "  + 1 vision",
    "shaman": " Medicine gives +20% energy",
    "wise": "   + 3 reputation on new maps"
}

crew = {  # contains the rentable companions in the ship
    "trader": "- 10% price bonus for trading",
    "soldier": "- Whiskey gives + 20% Energy",
    "donkey": "- +2 inventory slots"
}


def company(current_companions):
    # if player has companions, the energy cost of moves increases by 15%
    if len(current_companions) > 0:
        return (len(current_companions) * 0.15) + 1
    else:
        return 1


def scout(scout_sight):
    scout_sight.append(2)


def scout_out(scout_sight):
    scout_sight.remove(2)


def donkey(max_slots):
    # If donkey chosen as companion, increase inventory slots
    max_slots += 2
    return max_slots


def donkey_out(max_slots):
    # If donkey leaves the group, change back inventory slots to original
    max_slots -= 2
    return max_slots


def shaman_out(current_inventory):
    # If soldier leaves the group, change back medicine energy cost to original
    pass


def soldier_out(current_inventory):
    # If soldier leaves the group, change back whiskey energy cost to original
    pass
