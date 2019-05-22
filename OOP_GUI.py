import tkinter as tk
root = tk.Tk()
from tkinter import messagebox
from OOP_map_generator import game_map
from OOP_player import player
from images import *

root.title("THE PECULIAR EXPEDITION")

HEIGHT = 750
WIDTH = 1260

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#42b3f4', bd=5)
canvas.pack(side='right')

frame_map = tk.Frame(canvas, bd=5, bg='brown')
frame_map.place(relx=0.705, rely=0.005, relwidth=0.585, relheight=0.99, anchor='n')


# CREATING THE MAP: ##################################################################################################
def create_map():
    for BLOCK_INDEX, BLOCK in enumerate(game_map):  # <- with the enumerate, I can print the indexes
        for TERRAIN_OBJECT_INDEX, TERRAIN_OBJECT in enumerate(BLOCK):  # <- with the enumerate, I can print the indexes

            image = tk.PhotoImage(file=TERRAIN_OBJECT.image)
            TERRAIN_OBJECT.image = image  # <-- THIS IS NEEDED FOR SAVING THE ITEM WITH THE ATTACHED IMAGE.
            # WITHOUT THIS STEP THE IMAGES WONT BE LOADED IN THE LABELS.

            label = tk.Label(frame_map, image=TERRAIN_OBJECT.image, relief='sunken')
            label.grid(row=TERRAIN_OBJECT.coordinate[0], column=TERRAIN_OBJECT.coordinate[1])
            TERRAIN_OBJECT.label = label  # <-- SAVING THE LABEL ON THE TERRAIN OBJECT

            if BLOCK_INDEX == player.position[0] and TERRAIN_OBJECT_INDEX == player.position[1]:
                TERRAIN_OBJECT.label.config(relief='raised', bg='red')


create_map()


# CREATING THE MOVE FUNCTIONS ########################################################################################
def move_up():
    # MOVE UP IF NOT OUT OF INDEX
    if player.position[0]-1 >= 0 and game_map[player.position[0]-1][player.position[1]].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[0] -= 1
        check_if_game_over()
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        # DEBUGGING TEXT:
        display_debugging_text()
        call_functions()


def move_down():
    # MOVE DOWN IF NOT OUT OF INDEX
    if player.position[0]+1 <= 15 and game_map[player.position[0]+1][player.position[1]].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[0] += 1
        check_if_game_over()
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        # DEBUGGING TEXT:
        display_debugging_text()
        # CALLING
        call_functions()


def move_left():
    # MOVE LEFT IF NOT OUT OF INDEX
    if player.position[1]-1 >= 0 and game_map[player.position[0]][player.position[1]-1].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[1] -= 1
        check_if_game_over()
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        # DEBUGGING TEXT:
        display_debugging_text()
        call_functions()


def move_right():
    # MOVE RIGHT IF NOT OUT OF INDEX
    if player.position[1]+1 <= 15 and game_map[player.position[0]][player.position[1]+1].step:  # in range, step-able
        game_map[player.position[0]][player.position[1]].label.config(relief='sunken', bg='white')
        player.position[1] += 1
        check_if_game_over()
        game_map[player.position[0]][player.position[1]].label.config(relief='raised', bg='red')
        # DEBUGGING TEXT:
        display_debugging_text()
        call_functions()


def call_functions():
    global button_action_1, button_action_2, button_action_3

    terrain = game_map[player.position[0]][player.position[1]]
    slot_cost = 1 if len(player.inventory.contents) <= 8 else 1 + ((len(player.inventory.contents) - 8) * 0.2)
    companion_cost = 1 if len(player.companions) == 0 else 1 + (len(player.companions) * 0.25)
    player.energy -= terrain.cost * slot_cost * companion_cost
    update_character_panel()

    clear_action_buttons()

    if terrain.icon == "F":
        village_in()
        # show_action_buttons()
        # label_action.config(image=terrain.in_village())
        # button_action_1.config(text='trade', state='active')
        # button_action_2.config(text='rest', state='active')
        # button_action_3.config(text='hire', state='active')

    # if terrain.icon == "O":
    #     terrain.in_altar()
    # if terrain.icon == "S":
    #     terrain.in_sanctuary()
    # if terrain.icon == "B":
    #     terrain.in_cave()
    # if terrain.icon == "L":
    #     terrain.damage()
    # if terrain.icon == "C":
    #     terrain.in_boat()
    # if terrain.icon in "JR.":
    #     terrain.attacked()
    # if terrain.icon == "P":
    #     label_action.config(image=terrain.in_pyramid())


# CREATE DEBUGGING WINDOW ############################################################################################
frame_text = tk.Frame(canvas, bd=5, bg='brown')
frame_text.place(relx=0.2, rely=0.01, relwidth=0.15, relheight=0.15, anchor='n')

db_label_text = tk.Label(frame_text, text='Debugging Window:')
db_label_text.pack(side='top')

label_text = tk.Label(frame_text)
label_text.pack(side='bottom')


def display_debugging_text():
    slot_cost = 1 if len(player.inventory.contents) <= 8 else 1 + ((len(player.inventory.contents) - 8) * 0.2)
    companion_cost = 1 if len(player.companions) == 0 else 1 + (len(player.companions) * 0.25)
    # print("slot cost: " + str(slot_cost))
    # print("companion cost: " + str(companion_cost))
    label_text.config(text=game_map[player.position[0]][player.position[1]].name + str(player.position) +
                      "\nslot cost: " + str(slot_cost) + "\n companion cost: " + str(companion_cost))


display_debugging_text()


# CREATE CHARACTER PANEL #############################################################################################
frame_character = tk.Frame(canvas, bd=5, bg='brown')
frame_character.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.2, anchor='n')

label_character_hp_text = tk.Label(frame_character, text='health: ').grid(row=0, sticky='we')
label_character_energy_text = tk.Label(frame_character, text='energy:').grid(row=1, sticky='we')
label_character_mana_text = tk.Label(frame_character, text='mana:  ').grid(row=2, sticky='we')
label_character_gold_text = tk.Label(frame_character, text='gold:  ').grid(row=3, sticky='we')


label_character_hp = tk.Label(frame_character, text=player.health_point, bg="gray", fg='green')
label_character_hp.grid(row=0, column=1, sticky='we')
label_character_energy = tk.Label(frame_character, text=player.energy, bg="gray", fg='yellow')
label_character_energy.grid(row=1, column=1, sticky='we')
label_character_mana = tk.Label(frame_character, text=player.mana_point, bg="gray", fg='blue')
label_character_mana.grid(row=2, column=1, sticky='we')
label_character_gold = tk.Label(frame_character, text=player.gold, bg="gray", fg='yellow')
label_character_gold.grid(row=3, column=1, sticky='we')


def update_character_panel():
    label_character_hp.config(text=str(player.health_point))
    label_character_energy.config(text=str(player.energy))
    label_character_mana.config(text=str(player.mana_point))
    label_character_gold.config(text=str(player.gold))


#  CREATE ACTION WINDOW ##############################################################################################
#  ACTION WINDOW 1:
frame_action = tk.Frame(canvas, bd=5, bg='brown')
frame_action.place(relx=0.2, rely=0.43, relwidth=0.35, relheight=0.35, anchor='n')

action_image = tk.PhotoImage(file='GAME_IMAGES/landscape.png')
label_action = tk.Label(frame_action, image=action_image)
label_action.place(width=437, height=253)

button_action_1 = tk.Button(frame_action, text='action1', state='disabled')
button_action_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
button_action_2 = tk.Button(frame_action, text='action2', state='disabled')
button_action_2.place(relx=0.25, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
button_action_3 = tk.Button(frame_action, text='action3', state='disabled')
button_action_3.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')


#  ACTION WINDOW 2: (SECONDARY)
def create_action_ii_frame_label(img):
    global frame_action_II, label_action_II
    frame_action_II = tk.Frame(frame_action, border=5, bg='blue')
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
    print("create_listbox_action_ii " + buy_or_sell)
    global listbox_action_II
    listbox_action_II = tk.Listbox(label_action_II, border=2, relief='sunken')
    listbox_action_II.place(relx=0.15, rely=0, relwidth=0.3, anchor='n')

    for e in pasted_list:
        if e.pieces > 0:
            listbox_action_II.insert(tk.END, e)

    listbox_action_II.bind('<Double-1>', lambda x: village_delete_item(buy_or_sell))


def destroy_secondary_action_frame():
    frame_action_II.destroy()
    bind_movement()


def clear_action_buttons():
    button_action_1.place_forget()
    button_action_2.place_forget()
    button_action_3.place_forget()


def show_action_buttons():
    button_action_1.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_2.place(relx=0.25, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')
    button_action_3.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1, anchor='n')


# CREATING THE CONTROL PANEL AND ADDING THE MOVE FUNCTIONS ###########################################################
frame_control = tk.Frame(canvas, bd=5, bg='brown')
frame_control.place(relx=0.2, rely=0.82, relwidth=0.15, relheight=0.15, anchor='n')

up_image = tk.PhotoImage(file='GAME_IMAGES/arrow_up.png')
button_up = tk.Button(frame_control, image=up_image, command=move_up)
button_up.place(relx=0.5, rely=0.08, relwidth=0.25, relheight=0.4, anchor='n')

down_image = tk.PhotoImage(file='GAME_IMAGES/arrow_down.png')
button_down = tk.Button(frame_control, image=down_image, command=move_down)
button_down.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.4, anchor='n')

left_image = tk.PhotoImage(file='GAME_IMAGES/arrow_left.png')
button_left = tk.Button(frame_control, image=left_image, command=move_left)
button_left.place(relx=0.2, rely=0.5, relwidth=0.25, relheight=0.4, anchor='n')

right_image = tk.PhotoImage(file='GAME_IMAGES/arrow_right.png')
button_right = tk.Button(frame_control, image=right_image, command=move_right)
button_right.place(relx=0.8, rely=0.5, relwidth=0.25, relheight=0.4, anchor='n')


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


# GAME RULES #########################################################################################################
def check_if_game_over():
    if player.health_point < 0 or player.energy < 0:
        messagebox.showinfo("GAME OVER", "You Lost")
        root.destroy()


# TERRAIN FUNCTIONS ##################################################################################################
def village_in():
    show_action_buttons()
    label_action.config(image=in_village)
    button_action_1.config(text='trade', state='active', command=village_trade)
    button_action_2.config(text='rest', state='active', command=village_rest)
    button_action_3.config(text='hire', state='active')


def village_rest():
    player.energy = 100
    update_character_panel()


def village_trade():
    create_action_ii_frame_label(trade)
    create_action_ii_buttons()
    button_action_II_1.config(text='buy', state='active', command=village_buy)
    button_action_II_2.config(text='sell', state='active', command=village_sell)
    button_action_II_3.config(text='back', state='active', command=destroy_secondary_action_frame)
    stop_movement()


def village_buy():
    village = game_map[player.position[0]][player.position[1]]
    create_listbox_action_ii(village.vendor.contents, "buy")


def village_sell():
    create_listbox_action_ii(player.inventory.contents, "sell")


def village_delete_item(buy_or_sell):
    print("delete_item " + buy_or_sell)
    village = game_map[player.position[0]][player.position[1]]

    item = listbox_action_II.selection_get().split(" ")  # item name is string like: Meat 2   <- split it in 2 piece
    item_name = item[0].lower()    # get the first element of the split item name like: Meat  then make it lower case
    if buy_or_sell == "buy":
        village.buy(item_name)
        create_listbox_action_ii(village.vendor.contents, "buy")
    else:
        village.sell(item_name)
        create_listbox_action_ii(player.inventory.contents, "sell")

    update_character_panel()





root.mainloop()
