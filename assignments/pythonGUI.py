from Tkinter import *
from tkMessageBox import *

######## Main Buttons ########

class BuckysButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print message in command line", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("The most interesting text you have ever seen")

def doNothing():
    print("You may never leave")

def Open():
    showinfo("Open", "Please uninstall this program and reformat your hard drive")

def Save():
    showinfo("Save", "Press crtl+S")

def Print():
    showinfo("Print", "Press crtl+P")

def Undo():
    showerror("Undo", "You can't undo your mistakes")

def Redo():
    showwarning("Redo", "Would you like help with the internet?")

def answer():
    showinfo("The answer to life", "python the best snoodle snek")

def virus():
    showerror("Error", "Error: Not enough system RAM installed. Please download more RAM to install this program.")

########################################

root = Tk()


########################################

#Copyright
theLabel = Label(root, text="Copyright 2018 Nobody", bg="blue", fg="white")
theLabel.pack(side=BOTTOM, fill=X)

#Main Menu
menu = Menu(root)
root.config(menu=menu)

#First Dropdown
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open...", command=Open)
subMenu.add_command(label="Save As...", command=Save)
subMenu.add_command(label="Print...", command=Print)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

#Second Dropdown
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=Undo)
editMenu.add_command(label="Redo", command=Redo)

#Toolbar
toolbar = Frame(root, bg="red")

#Main Buttons
insertButt = Button(toolbar, text="Click ME TO DOWNLOAD FILE: bootsectorscripttrojanpartitioninfectorvirus.zip.bmp.exe", command=virus)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

#Secondary Buckybuttons
b = BuckysButtons(root)

#Other button
Button(text='Want to know what a python is?', command=answer).pack(side=TOP)

#Status bar
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()