import random
import time
from player import player as PLAYER

weapons = [
    ["rusty sword", 6, 10],
    ["great axe", 8, 14],
    ["huge mace", 10, 18]
]


class Monster:
    def __init__(self, race="Monster", name="Monster", lives=1, health_point=10, strength=0, armor=0, min_dmg=1,
                 max_dmg=2):
        self._race = race
        self.name = name
        self._lives = lives
        self.health_point = health_point
        self.strength = strength
        self.armor = armor
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.weapon = random.choice(weapons)
        self.alive = True

    def take_dmg(self, dmg):
        dmg -= self.armor
        if dmg <= 0:
            print(self.name + " blocked your attack")
            return

        remaining_hp = self.health_point - dmg
        if remaining_hp > 0:
            self.health_point -= dmg
            # print(self.name + " took " + colored(str(dmg), "red") + " damage")
        else:
            self.health_point -= dmg
            self.alive = False
            print(self.name + " died")

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.health_point

    def deal_dmg(self, player):
        if not self.alive:
            return

        if self.alive:
            print(self.name + " is swinging his " + self.weapon[0] + " at you!")
            # time.sleep(2.5)
            player.take_dmg(int(random.randint(self.weapon[1] + self.min_dmg, self.weapon[2] + self.max_dmg)
                            + self.strength))

    def __str__(self):
        return "Race: {0._race}, Name: {0.name}, Lives: {0._lives} HP: {0.health_point}, " \
               "Weapon: {0.weapon[0]}".format(self)


class Troll(Monster):
    def __init__(self):
        super().__init__(race="Troll", name="Jungle Troll", health_point=int(30*PLAYER.level/2),
                         strength=int(3*PLAYER.level), armor=int(1*PLAYER.level/2))


class Dragon(Monster):
    def __init__(self):
        super().__init__(race="Dragon", name="Emerald Dragon", health_point=int(50*PLAYER.level/2),
                         strength=int(2*PLAYER.level), armor=int(1*PLAYER.level/2), min_dmg=5, max_dmg=10)

    def deal_dmg(self, player):
        if not self.alive:
            return

        if self.alive:
            player.take_dmg(int(random.randint(self.min_dmg, self.max_dmg) + self.strength))


class Tiger(Monster):
    def __init__(self):
        super().__init__(race="Beast", name="Tiger", health_point=int(20*PLAYER.level/2),
                         strength=int(2*PLAYER.level), armor=int(1*PLAYER.level/2), min_dmg=5, max_dmg=10)

    def take_dmg(self, dmg):
        dmg -= self.armor
        if dmg <= 0:
            print(self.name + " blocked your attack")
            return

        if random.randint(1, 10) <= 3:
            print("***** " + self.name + " Dodges *****")
        else:
            remaining_hp = self.health_point - dmg
            if remaining_hp > 0:
                self.health_point -= dmg
                # print(self.name + " took " + colored(str(dmg), "red") + " damage")

            else:
                self.health_point = 0
                self.alive = False
                print(self.name + " died")

    def deal_dmg(self, player):
        if not self.alive:
            return

        if self.alive:
            bite_or_claw = random.randint(1, 2)
            if bite_or_claw == 1:
                print(self.name + " is biting you")
                time.sleep(2.5)
                player.take_dmg(int(random.randint(self.min_dmg, self.max_dmg) + self.strength))
            else:
                print(self.name + " is clawing you")
                time.sleep(2.5)
                player.take_dmg(int((random.randint(self.min_dmg, self.max_dmg) + self.strength)*1.5))


class Crocolisk(Monster):
    def __init__(self):
        super().__init__(race="Beast", name="Crocolisk", health_point=int(40*PLAYER.level/2),
                         strength=int(4*PLAYER.level), armor=int(2*PLAYER.level/2), min_dmg=8, max_dmg=16)

    def deal_dmg(self, player):
        if not self.alive:
            return

        if self.alive:
            print(self.name + " is biting you")
            time.sleep(2.5)
            player.take_dmg(int(random.randint(self.min_dmg, self.max_dmg) + self.strength))
            if random.randint(1, 4) == 1:
                print(self.name + " starting a Death Roll")
                time.sleep(2)
                player.take_dmg(random.randint(1, self.strength))
                player.take_dmg(random.randint(1, self.strength))
                player.take_dmg(random.randint(1, self.strength))


class Bandit(Monster):
    def __init__(self):
        super().__init__(race="Humanoid", name="Bandit", health_point=int(25*PLAYER.level/2),
                         strength=int(1*PLAYER.level), armor=int(2*PLAYER.level/2), min_dmg=1, max_dmg=5)

    def take_dmg(self, dmg):
        dmg -= self.armor
        if dmg <= 0:
            print(self.name + " blocked your attack")
            return

        if random.randint(1, 10) <= 2:
            print("***** " + self.name + " Dodges *****")
        else:
            remaining_hp = self.health_point - dmg
            if remaining_hp > 0:
                self.health_point -= dmg
                # print(self.name + " took " + colored(str(dmg), "red") + " damage")

            else:
                self.health_point = 0
                self.alive = False
                print(self.name + " died")

    def deal_dmg(self, player):
        if not self.alive:
            return

        if self.alive:
            print(self.name + " is swinging his daggers at you!")
            time.sleep(2)
            player.take_dmg(int(random.randint(self.min_dmg, self.max_dmg) + self.strength))
            player.take_dmg(int(random.randint(self.min_dmg, self.max_dmg) + self.strength))
