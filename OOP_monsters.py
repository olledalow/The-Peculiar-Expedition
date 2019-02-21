import random
import time

weapons = [
    ["sword", 1, 5],
    ["axe", 5, 10],
    ["mace", 10, 15]
]

class Monster:

    def __init__(self, race="Monster", name="Monster", lives=1, health_point=10):
        self._race = race
        self.name = name
        self._lives = lives
        self.health_point = health_point
        self._weapon = random.choice(weapons)
        self.alive = True

    def take_dmg(self, dmg):
        remaining_hp = self.health_point - dmg
        if remaining_hp > 0:
            self.health_point -= dmg
            print(self.name + " took " + str(dmg) + " damage")
        else:
            self.health_point = 0
            self.alive = False
            print(self.name + "died")

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.health_point

    def deal_dmg(self, player):
        if self.alive:
            print(self.name + " is swinging his " + self._weapon[0] + " at you!")
            time.sleep(2.5)
            player.take_dmg(random.randint(self._weapon[1], self._weapon[2]))

    def __str__(self):
        return "Race: {0._race}, Name: {0._name}, Lives: {0._lives} HP: {0._health_point}, " \
               "Weapon: {0._weapon[0]}".format(self)


class Troll(Monster):

    def __init__(self):
        super().__init__(race="Troll", name="Jungle Troll", health_point=30)


class Tiger(Monster):

    def __init__(self):
        super().__init__(race="Tiger", name="Tiger", health_point=20)

    def take_dmg(self, dmg):
        if random.randint(1, 10) <= 4:
            print("***** " + self.name + "Dodges *****")
        else:
            remaining_hp = self.health_point - dmg
            if remaining_hp > 0:
                self.health_point -= dmg
                print(self.name + " took " + str(dmg) + " damage")
            else:
                self.health_point = 0
                self.alive = False
                print(self.name + "died")

    def deal_dmg(self, player):
        if self.alive:
            print(self.name + " is biting you")
            time.sleep(2.5)
            player.take_dmg(random.randint(4, 8))


