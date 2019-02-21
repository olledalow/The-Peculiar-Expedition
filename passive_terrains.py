# THIS FILE CONTAINS:
# Functions for terrain types that have no interactive interface

import random
from OOP_player import fight
from OOP_monsters import Troll, Tiger
from GAME_displays import display_troll, display_tiger


def dot(current_energy, current_companions, current_inventory, slot_cost, companions_cost):
    # only burns energy to move on it if there are more items in the inventory than allowed,
    # or when traveling with companions
    if len(current_companions) != 0 and len(current_inventory) > 8:
        current_energy -= slot_cost * companions_cost
        return current_energy
    if len(current_companions) != 0:
        current_energy -= companions_cost
        return current_energy
    if len(current_inventory) > 8:
        current_energy -= slot_cost
        return current_energy
    else:
        current_energy -= 0
        return current_energy


def dot_wet(current_energy, move_cost, slot_cost, companions_cost):
    # Wet ground: burns more energy
    current_energy -= (move_cost * 1.8) * slot_cost * companions_cost
    return current_energy


def r(current_energy, move_cost, slot_cost, companions_cost):
    # burns energy
    fight_chance = random.randint(1, 100)
    if fight_chance <= 3:
        tiger = Tiger()
        display_tiger()
        input("A Prowling Tiger attacked you!")
        fight(tiger)
    current_energy -= (move_cost * 1.4) * slot_cost * companions_cost
    return current_energy


def r_wet(current_energy, move_cost, slot_cost, companions_cost):
    # wet thickets: burns more energy than simple thicket
    current_energy -= (move_cost * 2.1) * slot_cost * companions_cost
    return current_energy


def j(current_energy, current_map, current_position, current_inventory, move_cost, slot_cost, companions_cost,
      def_slot):
    # Jungle: use up a machete to turn it to plain ground. Else it burns more energy.
    fight_chance = random.randint(1, 100)
    if fight_chance <= 3:
        troll = Troll()
        display_troll()
        input("A jungle Troll attacked you!")
        fight(troll)
    if "machete" in current_inventory:
        if current_inventory["machete"][0] >= 1:
            current_inventory["machete"][0] -= 1
            current_map[current_position[0]][current_position[1]] = "."
            current_energy -= move_cost * slot_cost * companions_cost
            if current_inventory["machete"][0] == 0:
                current_inventory.pop("machete", None)
        current_slot = def_slot()
        return current_energy, current_slot
    else:
        current_energy -= (move_cost * 2) * slot_cost * companions_cost
        current_slot = def_slot()
        return current_energy, current_slot
