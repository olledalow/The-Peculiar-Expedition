import tkinter as tk
root = tk.Tk()
from tkinter import messagebox
from map_generator import game_map, generate_map, reset_map, remove_fog
from player import player
from images import *
from village_items import *

root.title("THE PECULIAR EXPEDITION")

HEIGHT = 750
WIDTH = 1260

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#42b3f4', bd=5)
canvas.pack(side='right')

frame_map = tk.Frame(canvas, bd=5, bg='brown')
frame_map.place(relx=0.705, rely=0.005, relwidth=0.585, relheight=0.99, anchor='n')


######################################################################################################################
# CREATING THE MAP: ##################################################################################################
def create_map():
    generate_map()
    for BLOCK_INDEX, BLOCK in enumerate(game_map):  # <- with the enumerate, I can print the indexes
        for TERRAIN_OBJECT_INDEX, TERRAIN_OBJECT in enumerate(BLOCK):  # <- with the enumerate, I can print the indexes

            label = tk.Label(frame_map, image=TERRAIN_OBJECT.actual_image, relief='sunken')
            label.grid(row=TERRAIN_OBJECT.coordinate[0], column=TERRAIN_OBJECT.coordinate[1])
            TERRAIN_OBJECT.label = label  # <-- SAVING THE LABEL ON THE TERRAIN OBJECT

            if BLOCK_INDEX == player.position[0] and TERRAIN_OBJECT_INDEX == player.position[1]:
                TERRAIN_OBJECT.label.config(relief='raised', bg='red')
    remove_fog()


create_map()
terrain = game_map[player.position[0]][player.position[1]]


def update_map():
    for BLOCK_INDEX, BLOCK in enumerate(game_map):  # <- with the enumerate, I can print the indexes
        for TERRAIN_OBJECT_INDEX, TERRAIN_OBJECT in enumerate(BLOCK):  # <- with the enumerate, I can print the indexes

            label = tk.Label(frame_map, image=TERRAIN_OBJECT.actual_image, relief='sunken')
            label.grid(row=TERRAIN_OBJECT.coordinate[0], column=TERRAIN_OBJECT.coordinate[1])
            TERRAIN_OBJECT.label = label  # <-- SAVING THE LABEL ON THE TERRAIN OBJECT

            if BLOCK_INDEX == player.position[0] and TERRAIN_OBJECT_INDEX == player.position[1]:
                TERRAIN_OBJECT.label.config(relief='raised', bg='red')


# This is for debugging only:
def show_map():
    for BLOCK_INDEX, BLOCK in enumerate(game_map):  # <- with the enumerate, I can print the indexes
        for TERRAIN_OBJECT_INDEX, TERRAIN_OBJECT in enumerate(BLOCK):  # <- with the enumerate, I can print the indexes

            label = tk.Label(frame_map, image=TERRAIN_OBJECT.image, relief='sunken')
            label.grid(row=TERRAIN_OBJECT.coordinate[0], column=TERRAIN_OBJECT.coordinate[1])
            TERRAIN_OBJECT.label = label  # <-- SAVING THE LABEL ON THE TERRAIN OBJECT

            if BLOCK_INDEX == player.position[0] and TERRAIN_OBJECT_INDEX == player.position[1]:
                TERRAIN_OBJECT.label.config(relief='raised', bg='red')


######################################################################################################################
# CREATING THE MOVE FUNCTIONS ########################################################################################
def move_up():
    # MOVE UP IF NOT OUT OF INDEX
    if player.position[0]-1 >= 0 and game_map[player.position[0]-1][player.position[1]].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[0] -= 1
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        call_functions()


def move_down():
    # MOVE DOWN IF NOT OUT OF INDEX
    if player.position[0]+1 <= 15 and game_map[player.position[0]+1][player.position[1]].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[0] += 1
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        call_functions()


def move_left():
    # MOVE LEFT IF NOT OUT OF INDEX
    if player.position[1]-1 >= 0 and game_map[player.position[0]][player.position[1]-1].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[1] -= 1
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        call_functions()


def move_right():
    # MOVE RIGHT IF NOT OUT OF INDEX
    if player.position[1]+1 <= 15 and game_map[player.position[0]][player.position[1]+1].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[1] += 1
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        call_functions()


def call_functions():
    global button_action_1, button_action_2, button_action_3, terrain

    terrain = game_map[player.position[0]][player.position[1]]
    slot_cost = 1 if len(player.inventory.contents) <= 8 else 1 + ((len(player.inventory.contents) - 8) * 0.2)
    companion_cost = 1 if len(player.companions) == 0 else 1 + (len(player.companions) * 0.25)
    player.energy -= int(terrain.cost * slot_cost * companion_cost)
    update_character_panel()
    update_debugging_text()

    if check_if_game_over():
        return

    if check_if_level_won():
        return

    clear_action_buttons()
    clear_action_label_text()
    bind_movement()
    place_character_buttons()
    remove_fog()
    if player.injured:
        player.injury()

    if terrain.icon == "F":
        village_in()
    if terrain.icon == "O":
        altar_in()
    if terrain.icon == "S":
        sanctuary_in()
    if terrain.icon == "B":
        cave_in()
    if terrain.icon == "L":
        lava_in()
    if terrain.icon == "C":
        ship_in()
    if terrain.icon == "J":
        jungle_in()
    if terrain.icon == "R":
        thicket_in()
    if terrain.icon == ".":
        meadow_in()
    if terrain.icon == "P":
        pyramid_in()


######################################################################################################################
# CREATE DEBUGGING WINDOW ############################################################################################
frame_text = tk.Frame(canvas, bd=5, bg='brown')
frame_text.place(relx=0.2, rely=0.01, relwidth=0.2, relheight=0.17, anchor='n')

db_label_text = tk.Label(frame_text, text='This is the Debugging Window:', bg="SkyBlue4", fg="white")
db_label_text.pack(side='top')

label_text = tk.Label(frame_text)
label_text.pack(side='left')

button_db_show_map = tk.Button(frame_text, text='show map', command=show_map, relief='raised')
button_db_show_map.pack(side='right')


def update_debugging_text():
    slot_cost = 1 if len(player.inventory.contents) <= 8 else 1 + ((len(player.inventory.contents) - 8) * 0.2)
    companion_cost = 1 if (len(player.companions) + len(player.injured_companions)) == 0 else \
        1 + ((len(player.companions) + len(player.injured_companions)) * 0.25)
    # print("slot cost: " + str(slot_cost))
    # print("companion cost: " + str(companion_cost))
    label_text.config(text=terrain.name + str(player.position) + "\n terrain cost: " + str(terrain.cost) +
                      "\nslot cost: " + str(slot_cost) + "\n companion cost: " + str(companion_cost) +
                      "\n all cost: " + str(int(terrain.cost * slot_cost*companion_cost)))


update_debugging_text()


######################################################################################################################
# CREATE CHARACTER PANEL #############################################################################################
frame_character = tk.Frame(canvas, bd=5, bg='brown')
frame_character.place(relx=0.2, rely=0.2, relwidth=0.32, relheight=0.2, anchor='n')

label_character_hp_text = tk.Label(frame_character, text='health: ').grid(row=0, sticky='we')
label_character_energy_text = tk.Label(frame_character, text='energy:').grid(row=1, sticky='we')
label_character_mana_text = tk.Label(frame_character, text='mana:  ').grid(row=2, sticky='we')
label_character_gold_text = tk.Label(frame_character, text='gold:  ').grid(row=3, sticky='we')


label_character_hp = tk.Label(frame_character, text=str(player.health_point//4 * u"\u25A0" +
                                                        " " + str(player.health_point)), bg="gray", fg='green2')
label_character_hp.grid(row=0, column=1, sticky='w')

label_character_energy = tk.Label(frame_character, text=str(player.energy//4 * u"\u25A0" + " " +
                                                            str(player.energy)), bg="gray", fg='green2')
label_character_energy.grid(row=1, column=1, sticky='w')

label_character_mana = tk.Label(frame_character, text=str(player.mana_point * u"\u25A0" + " " +
                                                          str(player.mana_point)), bg="gray", fg='blue')
label_character_mana.grid(row=2, column=1, sticky='w')

label_character_gold = tk.Label(frame_character, text=player.gold, bg="gray", fg='yellow')
label_character_gold.grid(row=3, column=1, sticky='w')


def update_character_panel():
    if player.energy > 50:
        energy_color = 'green2'
    elif player.energy > 20:
        energy_color = 'yellow'
    else:
        energy_color = 'red'

    if player.health_point > 50:
        hp_color = 'green2'
    elif player.health_point > 20:
        hp_color = 'yellow'
    else:
        hp_color = 'red'

    label_character_hp.config(text=str(int(player.health_point//4) *
                                       u"\u25A0" + " " + str(int(player.health_point))), fg=hp_color)
    label_character_energy.config(text=str(int(player.energy//4) *
                                           u"\u25A0" + " " + str(player.energy)), fg=energy_color)
    label_character_mana.config(text=str(player.mana_point * u"\u25A0" + " " + str(player.mana_point)))
    label_character_gold.config(text=str(player.gold))


######################################################################################################################
#  CREATE ACTION WINDOW ##############################################################################################
#  ACTION WINDOW 1:
frame_action = tk.Frame(canvas, bd=5, bg='brown')
frame_action.place(relx=0.2, rely=0.43, relwidth=0.35, relheight=0.35, anchor='n')

label_action = tk.Label(frame_action, image=in_meadow)
label_action.place(width=437, height=253)

button_action_1 = tk.Button(frame_action, text='action1', state='disabled')
button_action_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
button_action_2 = tk.Button(frame_action, text='action2', state='disabled')
button_action_2.place(relx=0.25, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
button_action_3 = tk.Button(frame_action, text='action3', state='disabled')
button_action_3.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')

label_action_text = tk.Label(label_action, anchor='w', bg='SkyBlue3', wraplength=448, justify='left')


def create_listbox_action(pasted_list):
    global listbox_action

    if type(pasted_list) == list:
        listbox_action = tk.Listbox(label_action, border=2, relief='sunken', width=28, height=5, bg='salmon3')
        listbox_action.bind('<Double-1>', lambda x: consume_item())
    else:
        listbox_action = tk.Listbox(label_action, border=2, relief='sunken', height=3, width=50, bg='salmon3')
        if terrain.icon in "FC":
            listbox_action.bind('<Double-1>', lambda x: buy_companion())

    listbox_action.grid(sticky='nw')

    for e in pasted_list:
        if type(pasted_list) == list:
            listbox_action.insert(tk.END, e.name + " " + str(e.pieces) + " " + str(e.usage))
        else:
            listbox_action.insert(tk.END, e + pasted_list.get(e))

    if player.injured:
        for e in player.injured_companions:
            listbox_action.insert(tk.END, e + player.injured_companions.get(e))


#  ACTION WINDOW 2: (SECONDARY)
def create_action_ii_frame_label(img):
    global frame_action_II, label_action_II
    frame_action_II = tk.Frame(frame_action)
    frame_action_II.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')
    label_action_II = tk.Label(frame_action_II, image=img)
    label_action_II.place(width=437, height=253)


def create_action_ii_buttons():
    global button_action_II_1, button_action_II_2, button_action_II_3
    button_action_II_1 = tk.Button(frame_action_II, text='action1')
    button_action_II_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_II_2 = tk.Button(frame_action_II, text='action2')
    button_action_II_2.place(relx=0.25, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_II_3 = tk.Button(frame_action_II, text='action3')
    button_action_II_3.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')


def create_listbox_action_ii(pasted_list, buy_or_sell):
    global listbox_action_II
    listbox_action_II = tk.Listbox(label_action_II, border=2, relief='sunken', width=28, height=5, bg="SkyBlue3")
    listbox_action_II.grid(sticky='nw')

    trader_discount = 1
    if 'trader' in player.companions:
        trader_discount = 1.1 if buy_or_sell == 'sell' else 0.9

    for e in pasted_list:
        if e.pieces > 0:
            listbox_action_II.insert(tk.END, str(e.name) + " " + str(e.pieces) + " " +
                                     str(int(e.price*trader_discount)) + " " + str(e.usage))

    listbox_action_II.bind('<Double-1>', lambda x: village_delete_item(buy_or_sell))


def destroy_secondary_action_frame():
    frame_action_II.destroy()
    place_bag()  # turn bag button ON!
    place_companions()  # turn comp. button ON!

    bind_movement()  # turn movement ON!


def clear_action_buttons():
    button_action_1.place_forget()
    button_action_2.place_forget()
    button_action_3.place_forget()


def clear_action_ii_buttons():
    button_action_II_1.place_forget()
    button_action_II_2.place_forget()
    button_action_II_3.place_forget()


def clear_action_label_text():
    label_action_text.grid_forget()


def show_action_buttons():
    button_action_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_2.place(relx=0.25, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_3.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')


######################################################################################################################
#  CREATING THE CHARACTER BUTTONS ####################################################################################
#  CREATING THE BAG OPENING BUTTON AND FUNCTIONS + CONSUMING FOOD
bag_opened = True


def open_bag():
    global bag_opened
    if bag_opened:
        label_action.config(image=in_bag)
        create_listbox_action(player.inventory.contents)
        stop_movement()
        button_companions.place_forget()
        clear_action_buttons()
        bag_opened = False
    else:
        if terrain.icon in "FC":
            if terrain.icon == "F":
                village_in()
            else:
                ship_in()
            listbox_action.destroy()
            show_action_buttons()
            bind_movement()
            place_companions()
            bag_opened = True
        else:
            listbox_action.destroy()
            label_action.config(image=terrain.action_image)
            bind_movement()
            place_companions()
            bag_opened = True


button_bag = tk.Button(canvas, image=bag, highlightcolor='brown', relief='raised', command=open_bag)


def place_bag():
    button_bag.place(relx=0.07, rely=0.79, relwidth=0.07, relheight=0.14, anchor='n')


place_bag()


def consume_item():
    item = listbox_action.selection_get().split(" ")  # item name is string like: Meat 2 50  <- split it in 2 piece
    item_name = item[0].lower()    # get the first element of the split item name like: Meat  then make it lower case

    player.consume_food(item_name)
    listbox_action.destroy()
    create_listbox_action(player.inventory.contents)

    update_character_panel()


######################################################################################################################
#  CREATING THE COMPANIONS BUTTON AND FUNCTIONS#######################################################################
companions_opened = True


def show_companions():
    global companions_opened

    if companions_opened:
        label_action.config(image=companions_big)
        create_listbox_action(player.companions)
        stop_movement()
        button_bag.place_forget()
        clear_action_buttons()
        companions_opened = False
    else:
        if terrain.icon in "FC":
            if terrain.icon == "F":
                village_in()
            else:
                ship_in()
            listbox_action.destroy()
            show_action_buttons()
            bind_movement()
            place_bag()
            companions_opened = True
        else:
            listbox_action.destroy()
            label_action.config(image=terrain.action_image)
            bind_movement()
            place_bag()
            companions_opened = True


button_companions = tk.Button(canvas, image=companions, highlightcolor='brown', relief='raised',
                              command=show_companions)


def place_companions():
    button_companions.place(relx=0.16, rely=0.79, relwidth=0.07, relheight=0.14, anchor='n')


place_companions()


def place_character_buttons():
    place_bag()
    place_companions()


def clear_character_buttons():
    button_bag.place_forget()
    button_companions.place_forget()


######################################################################################################################
# KEY BINDING THE MOVE FUNCTIONS #####################################################################################
def bind_movement():
    root.bind('w', lambda event: move_up())
    root.bind('s', lambda event: move_down())
    root.bind('a', lambda event: move_left())
    root.bind('d', lambda event: move_right())


bind_movement()


def pass_function():
    pass


def stop_movement():
    root.bind('w', lambda event: pass_function())
    root.bind('s', lambda event: pass_function())
    root.bind('a', lambda event: pass_function())
    root.bind('d', lambda event: pass_function())


######################################################################################################################
# GAME RULES #########################################################################################################
def check_if_game_over():
    if player.health_point <= 0 or player.energy <= 0:
        messagebox.showinfo("GAME OVER", "You Lost")
        root.destroy()
        return True


def check_if_level_won():
    if terrain.icon == "C" and Emerald() in player.inventory.contents:
        player.inventory.remove_item(Emerald(1))
        if player.level == 4:
            messagebox.showinfo("You Win!", "Congratulations!!! You Completed all 5 levels!")
            return

        messagebox.showinfo("You Win!", "Level " + str(player.level) + " Completed!\nLevel " + str(player.level + 1)
                            + " is Loading up!")
        player.level += 1
        player.gold += 200 if "wise" in player.companions else 100
        player.health_point += 20
        if player.health_point > 100:
            player.health_point = 100
        player.energy = 100
        player.mana_point += 1
        if player.mana_point > 5:
            player.mana_point = 5
        reset_map()
        create_map()
        update_character_panel()
        ship_in()
        return True


help_images = [help0, help1, help2, help3]
next_image = 0


def help_function():
    global help_window, help_canvas, help_img, help_button_frame, help_previous_button, help_next_button
    help_window = tk.Toplevel(root)
    help_canvas = tk.Canvas(help_window, height=HEIGHT, width=WIDTH//1.2)
    help_canvas.pack(side='left')
    help_img = tk.Label(help_canvas, image=help0)
    help_img.pack()
    help_button_frame = tk.Frame(help_canvas)
    help_button_frame.pack(side="bottom")
    help_previous_button = tk.Button(help_button_frame, text='previous', command=help_previous)
    help_previous_button.grid(column=0, row=0)
    help_next_button = tk.Button(help_button_frame, text='next', command=help_next)
    help_next_button.grid(column=1, row=0)


def help_previous():
    global next_image

    next_image -= 1
    if next_image < 0:
        next_image = 0

    help_img.config(image=help_images[next_image])


def help_next():
    global next_image

    next_image += 1
    if next_image > len(help_images)-1:
        next_image = len(help_images)-1

    help_img.config(image=help_images[next_image])


help_button = tk.Button(canvas, text="Help", command=help_function)
help_button.place(relx=0.02, rely=0.01, anchor='n')


######################################################################################################################
# TERRAIN FUNCTIONS ##################################################################################################
# VILLAGE ############################################################################################################
def village_in():
    show_action_buttons()
    label_action_text.grid_forget()
    label_action.config(image=terrain.action_image)
    button_action_1.config(text='trade', state='active', command=village_trade)
    button_action_2.config(text='rest', state='active', command=village_rest)
    button_action_3.config(text='hire', state='active', command=village_ship_hire)


def village_rest():
    if player.gold >= 20 or terrain.icon == "C":
        label_action.config(image=bed)
        clear_action_buttons()
        button_action_1.config(text='get up', state='active', command=call_functions)
        button_action_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
        label_action_text.config(text="You are resting in this compfy bed")
        label_action_text.grid()
        player.gold -= 20 if terrain.icon == "F" else 0
        player.energy = 100
        update_character_panel()
    else:
        messagebox.showinfo("not enough gold", "You don't have enough gold... resting is 20 gold!")


def village_trade():
    create_action_ii_frame_label(trade)
    create_action_ii_buttons()
    button_action_II_1.config(text='buy', state='active', command=village_buy)
    button_action_II_2.config(text='sell', state='active', command=village_sell)
    button_action_II_3.config(text='back', state='active', command=destroy_secondary_action_frame)
    clear_character_buttons()
    stop_movement()


def village_buy():
    try:  # IF BUYING FOR THE FIRST TIME
        listbox_action_II.destroy()
    except NameError:
        pass

    create_listbox_action_ii(terrain.vendor.contents, "buy")


def village_sell():
    try:
        listbox_action_II.destroy()
    except NameError:
        pass

    create_listbox_action_ii(player.inventory.contents, "sell")


def village_delete_item(buy_or_sell):
    item = listbox_action_II.selection_get().split(" ")  # item name is string like: Meat 2   <- split it in 2 piece
    item_name = item[0].lower()    # get the first element of the split item name like: Meat  then make it lower case
    if buy_or_sell == "buy":
        terrain.buy(item_name)
        listbox_action_II.destroy()
        create_listbox_action_ii(terrain.vendor.contents, "buy")
    else:
        terrain.sell(item_name)
        listbox_action_II.destroy()
        create_listbox_action_ii(player.inventory.contents, "sell")

    update_character_panel()


villagers_crew_opened = True


def village_ship_hire():
    global villagers_crew_opened

    if terrain.icon == "F":
        comp_dict = terrain.villagers
        image = villagers
    else:
        comp_dict = terrain.crew
        image = crew

    if villagers_crew_opened:
        label_action.config(image=image)
        create_listbox_action(comp_dict)
        button_action_3.config(text="back")
        button_action_1.config(state='disabled')
        button_action_2.config(state='disabled')
        stop_movement()
        button_bag.place_forget()
        button_companions.place_forget()
        villagers_crew_opened = False
    else:
        if terrain.icon == "F":
            village_in()
            listbox_action.destroy()
            button_action_3.config(text="hire")
            button_action_1.config(state='active')
            button_action_2.config(state='active')
            bind_movement()
            place_bag()
            place_companions()
            villagers_crew_opened = True
        elif game_map[player.position[0]][player.position[1]].icon == "C":
            ship_in()
            listbox_action.destroy()
            button_action_1.config(text="hire")
            button_action_2.config(state='active')
            bind_movement()
            place_bag()
            place_companions()
            villagers_crew_opened = True
        else:
            listbox_action.destroy()
            button_action_3.config(text="hire")
            button_action_1.config(state='active')
            button_action_2.config(state='active')
            label_action.config(image=in_meadow)
            bind_movement()
            place_bag()
            place_companions()
            villagers_crew_opened = True


def buy_companion():
    companion = listbox_action.selection_get().split(" ")
    terrain.add_companion(companion[0])
    listbox_action.destroy()
    if terrain.icon == "F":
        create_listbox_action(terrain.villagers)
    else:
        create_listbox_action(terrain.crew)
    update_character_panel()
    update_debugging_text()


#  SHIP - has some common functions with village above ###############################################################
def ship_in():
    show_action_buttons()
    label_action.config(image=terrain.action_image)
    button_action_1.config(text='sail', state='active', command=sail_away)
    button_action_2.config(text='rest', state='active', command=village_rest)
    button_action_3.config(text='hire', state='active', command=village_ship_hire)


def sail_away():
    if messagebox.askyesno("Sail away?", "Are you sure you want to sail away to a new island? "
                           "(It will generate a new map...)"):
        reset_map()
        create_map()


#  JUNGLE ############################################################################################################
def jungle_in():
    label_action.config(image=terrain.action_image)


#  THICKET ###########################################################################################################
def thicket_in():
    label_action.config(image=terrain.action_image)


#  MEADOW ############################################################################################################
def meadow_in():
    label_action.config(image=terrain.action_image)


#  LAVA ##############################################################################################################
def lava_in():
    label_action.config(image=terrain.action_image)
    terrain.damage()
    update_character_panel()


#  ALTAR #############################################################################################################
def altar_in():
    label_action.config(image=terrain.action_image)
    button_action_1.place(relx=0.11, rely=0.85, relwidth=0.2, relheight=0.1, anchor='n')
    button_action_1.config(text='Enter Altar', state='active', command=adventure1)


def sanctuary_in():
    label_action.config(image=terrain.action_image)
    button_action_1.place(relx=0.12, rely=0.85, relwidth=0.22, relheight=0.1, anchor='n')
    button_action_1.config(text='Enter Sanctuary', state='active', command=adventure1)


def cave_in():
    label_action.config(image=terrain.action_image)
    button_action_1.place(relx=0.11, rely=0.85, relwidth=0.2, relheight=0.1, anchor='n')
    button_action_1.config(text='Enter Cave', state='active', command=adventure1)


def pyramid_in():
    label_action.config(image=terrain.action_image)
    button_action_1.place(relx=0.11, rely=0.85, relwidth=0.21, relheight=0.1, anchor='n')
    button_action_1.config(text='Enter Pyramid', state='active', command=adventure1)


adventure_line = "Adventure text filename will be assigned here in the function below"
needed_item = "Needed item will be assigned here in the function below"
lucky = False  # Determines whether catastrophe/curse will happen in an adventure or not.


def adventure1():
    global adventure_line
    global needed_item
    global lucky
    if terrain.empty:
        label_action_text.config(text="You have already been in this " + terrain.name + "...")
        button_action_1.config(text='Turn back', state='active', command=call_functions)
        label_action.config(image=terrain.adventure1_img)
        label_action_text.grid()
    else:
        if terrain.name == "Cave" and Torch() in player.inventory.contents:
            needed_item = "Use Torch"
            lucky = True
        elif terrain.name == "Sanctuary" and Rope() in player.inventory.contents:
            needed_item = "Use Rope"
            lucky = True
        else:
            needed_item = "Go ahead"

        button_action_1.config(text=needed_item, state='active', command=adventure2)
        button_action_2.place(relx=0.3, rely=0.85, relwidth=0.2, relheight=0.1, anchor='n')
        button_action_2.config(text='Turn back', state='active', command=call_functions)

        label_action.config(image=terrain.adventure1_img)

        adventure_line = terrain.name.lower()
        with open('ADVENTURE_TEXTS/' + adventure_line) as file:
            adventure_line = file.readlines()

        label_action_text.config(text=adventure_line[0])
        label_action_text.grid()
        stop_movement()
        clear_character_buttons()


def adventure2():
    global lucky

    if needed_item == "Use Torch" or needed_item == "Use Rope" or terrain.icon == "P":
        terrain.use_needed_item()
        label_action.config(image=terrain.adventure2_img)
        label_action_text.config(text=adventure_line[1])
    else:
        lucky, lucky_text = terrain.luck_chance()
        if lucky:
            label_action.config(image=terrain.adventure2_lucky_img)
            label_action_text.config(text=lucky_text)
        else:
            label_action.config(image=terrain.adventure2_not_lucky_img)
            label_action_text.config(text=lucky_text)
            update_map()
            update_character_panel()

    button_action_1.config(text='Next', state='active', command=adventure3)
    button_action_2.place_forget()
    terrain.empty = True

    if terrain.icon == "P":
        player.inventory.add_item(Emerald(1))
    else:
        player.inventory.add_item(Treasure(1))


adventure_count = 0


def adventure3():
    global lucky, adventure_count

    if needed_item == "Use Torch" or needed_item == "Use Rope" or terrain.icon == "P":
        if adventure_count == 0:
            label_action.config(image=terrain.adventure3_img)
        elif adventure_count == 1:
            label_action.config(image=terrain.adventure4_img)
        else:
            label_action.config(image=terrain.adventure5_img)
        label_action_text.config(text=adventure_line[2 + adventure_count])
    else:
        if lucky:
            if adventure_count == 0:
                label_action.config(image=terrain.adventure3_lucky_img)
            elif adventure_count == 1:
                label_action.config(image=terrain.adventure4_lucky_img)
            else:
                label_action.config(image=terrain.adventure5_lucky_img)
            label_action_text.config(text=adventure_line[7 + adventure_count])
        else:
            if adventure_count == 0:
                label_action.config(image=terrain.adventure3_not_lucky_img)
            elif adventure_count == 1:
                label_action.config(image=terrain.adventure4_not_lucky_img)
            else:
                label_action.config(image=terrain.adventure5_not_lucky_img)
            label_action_text.config(text=adventure_line[12 + adventure_count])

    adventure_count += 1

    if adventure_count == 3:

        if terrain.icon == "P":
            button_action_1.config(text='Next2', state='active', command=combat)
            adventure_count = 0
            lucky = False
        else:
            button_action_1.config(text='Next2', state='active', command=call_functions)
            adventure_count = 0
            lucky = False


######################################################################################################################
# COMBAT #############################################################################################################
def create_hp_bar(enemy):
    global label_combat_enemy_hp
    if enemy.health_point > 50:
        enemy_color = 'green2'
    elif enemy.health_point > 20:
        enemy_color = 'yellow'
    else:
        enemy_color = 'red'

    label_combat_enemy_hp = tk.Label(canvas, text=str(enemy.name + ": " + enemy.health_point // 4 * u"\u25A0" +
                                                      " " + str(enemy.health_point)), bg="gray", fg=enemy_color)
    label_combat_enemy_hp.place(relx=0.2, rely=0.411, relwidth=0.35, relheight=0.02, anchor='n')

    if enemy.health_point <= 0 or not enemy.alive:
        label_combat_enemy_hp.place_forget()


def update_hp_bar(enemy):
    if enemy.health_point > 50:
        enemy_color = 'green2'
    elif enemy.health_point > 20:
        enemy_color = 'yellow'
    else:
        enemy_color = 'red'

    label_combat_enemy_hp.config(text=str(enemy.name + ": " + enemy.health_point // 4 * u"\u25A0" +
                                          " " + str(enemy.health_point)), fg=enemy_color)

    if enemy.health_point <= 0 or not enemy.alive:
        label_combat_enemy_hp.place_forget()


players_turn = True


def combat():
    enemy = terrain.attacked()

    create_hp_bar(enemy)

    create_action_ii_frame_label(dragon)
    create_action_ii_buttons()
    button_action_II_1.config(text='sword', state='active', command=lambda: attack(enemy, "sword"))
    button_action_II_2.config(text='firebolt', state='active', command=lambda: attack(enemy, "firebolt"))
    button_action_II_3.place_forget()

    clear_character_buttons()
    stop_movement()


def check_combat_outcome(enemy):
    if not player.alive or not enemy.alive or player.energy <= 0 or player.health_point <= 0:
        button_action_II_1.place_forget()
        button_action_II_2.place_forget()
        button_action_II_3.place_forget()
        destroy_secondary_action_frame()
        label_combat_enemy_hp.place_forget()
        call_functions()
        return True


def attack(enemy, attack_type):
    global players_turn

    if check_combat_outcome(enemy):
        players_turn = True
        return

    if players_turn:
        player_attack(enemy, attack_type)
    else:
        enemy_attack(enemy)
        create_action_ii_buttons()
        button_action_II_1.config(text='sword', state='active', command=lambda: attack(enemy, "sword"))
        button_action_II_2.config(text='firebolt', state='active', command=lambda: attack(enemy, "firebolt"))
        button_action_II_3.place_forget()
        update_character_panel()
        players_turn = True


def player_attack(enemy, attack_type):
    global players_turn

    if attack_type == "sword":
        if player.energy > player.weapons[0][3]:
            label_action_II.config(image=sword)
            button_action_II_1.config(text='Next', state='active', command=lambda: attack(enemy, "enemy's turn..."))
            button_action_II_2.place_forget()
            button_action_II_3.place_forget()
            players_turn = False
            player.deal_dmg(enemy, attack_type)
        else:
            messagebox.showinfo("not enough energy", "You don't have enough energy to do that")
    elif attack_type == "firebolt":
        if player.mana_point > 0:
            label_action_II.config(image=firebolt)
            button_action_II_1.config(text='Next', state='active', command=lambda: attack(enemy, "enemy's turn..."))
            button_action_II_2.place_forget()
            button_action_II_3.place_forget()
            players_turn = False
            player.deal_dmg(enemy, attack_type)
        else:
            messagebox.showinfo("not enough mana", "You don't have enough mana to do that")

    update_hp_bar(enemy)
    update_character_panel()


def enemy_attack(enemy):
    label_action_II.config(image=dragon_attack)
    enemy.deal_dmg(player)


ship_in()
root.mainloop()
