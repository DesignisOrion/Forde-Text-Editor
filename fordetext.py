# Creating my very first text editor. Enjoy!
# importing the tkinter and the file dialog features
from tkinter import *
from tkinter import filedialog

# To start a new file


def new_file():
    text.delete(0.0, END)

# To open a new file


def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0, END)
    text.insert(0.0, data)

# To save a file


def save_file():
    filename = "Untiled.txt"
    data = txt.get(0.0, END)
    file1 = open(filename, 'w')
    file1.write(data)

# I Hope you understand the code. No cheating Sir / Maam.
# Created by DesignIsOrion

# To save as


def save_as():
    file1 = filedialog.asksaveasfile(mode-'w')
    data = text.get(0.0, END)
    file1.write(data)


# This is the code for the graphic user interface. Pretty straight forward
gui = Tk()
gui.title("Forde Text Editor")
gui.geometry("600x500")
text = Text(gui)
text.pack()

# This is how I created the menu
mymenu = Menu()
list1 = Menu()
list1.add_command(label="New file", command=new_file)
list1.add_command(label="Open file", command=open_file)
list1.add_command(label="Save", command=save_file)
list1.add_command(label="New file", command=save_as)
list1.add_command(label="Exit", command=gui.quit)
# Created by DesignIsOrion

mymenu.add_cascade(label="File", menu=list1)
gui.config(menu=mymenu)
gui.mainloop()
