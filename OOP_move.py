from OOP_player import player
from OOP_map_position import game_map
from OOP_map_generator import display_map
from termcolor import colored


def move():
    call_functions()
    display_map()
    while player.energy > 0:
        moving = input("move with 'w a s d', check your bag with 'b', see your companions with 'c'. ")
        if moving == "w" and player.position[0] > 0:
            if game_map[player.position[0] - 1][player.position[1]].step:
                player.position[0] -= 1
                call_functions()

        if moving == "a" and player.position[1] > 0:
            if game_map[player.position[0]][player.position[1] - 1].step:
                player.position[1] -= 1
                call_functions()

        if moving == "s" and player.position[0] < 15:
            if game_map[player.position[0] + 1][player.position[1]].step:
                player.position[0] += 1
                call_functions()

        if moving == "d" and player.position[1] > 0:
            if game_map[player.position[0]][player.position[1] + 1].step:
                player.position[1] += 1
                call_functions()

        if moving == "b":
            player.display_inventory()

        if moving == "c":
            if len(player.companions) > 0 or len(player.injured_companions) > 0:
                for e in player.companions:
                    print(e, player.companions[e])
                for i in player.injured_companions:
                    print(i, player.injured_companions[i])
                input("")
            else:
                input("You have no companions!")

        display_map()
        print("     min _________________________ max")
        print("HP:     |" + colored(str(int(player.health_point // 4) * u"\u25A0"), "green") +
              str(int(player.health_point)))
        print("energy: |" + colored(str(int(player.energy // 4) * u"\u25A0"), "yellow") + str(int(player.energy)))
        print("Mana:   |" + colored(str(int(player.mana_point) * ("|" + u"\u25A0" + "|")), "blue") +
              str(int(player.mana_point)))
        print("gold: " + colored(str(player.gold), "yellow"))


def call_functions():
    terrain = game_map[player.position[0]][player.position[1]]
    slot_cost = 1 if len(player.inventory.contents) <= 8 else 1 + ((len(player.inventory.contents) - 8) * 0.2)
    companion_cost = 1 if len(player.companions) == 0 else 1 + (len(player.companions) * 0.25)
    print("slot cost: " + str(slot_cost))
    print("companion cost: " + str(companion_cost))

    player.energy -= terrain.cost * slot_cost * companion_cost
    if terrain.icon == "F":
        terrain.in_village()
    if terrain.icon == "O":
        terrain.in_altar()
    if terrain.icon == "S":
        terrain.in_sanctuary()
    if terrain.icon == "B":
        terrain.in_cave()
    if terrain.icon == "L":
        terrain.damage()
    if terrain.icon == "C":
        terrain.in_boat()
    if terrain.icon in "JR":
        terrain.attacked()


move()
