from tkinter import *


def func1():
    print("in func1")


def func2():
    print("in func2")


def selection():
    dictionary[listbox.selection_get()]()
    print(listbox.selection_get())


root = Tk()

frame = Frame(root)
frame.pack()

dictionary = {"1": func1, "2": func2}

items = StringVar(value=tuple(sorted(dictionary.keys())))

listbox = Listbox(frame, listvariable=items, width=15, height=5)
listbox.grid(column=0, row=2, rowspan=6, sticky=("n", "w", "e", "s"))

selectButton = Button(frame, command=selection)
listbox.bind('<Double-1>', lambda x: selectButton.invoke())

root.mainloop()
