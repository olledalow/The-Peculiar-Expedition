from copy import copy


class Item:
    def __init__(self, pieces, price, energy_bonus, usage="   ~ consume for energy"):
        self.pieces = pieces
        self.price = price
        self.energy_bonus = energy_bonus
        self.usage = usage

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


class Treasure(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 100, 0, usage="   ~ Worth 100 golds!")


class Rope(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 0, 0, usage="   ~ Helpful at Sanctuaries to secure passages")


class Torch(Item):
    def __init__(self, pieces=0):
        super().__init__(pieces, 0, 0, usage="   ~ Helpful at Caves to see in the dark")


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
