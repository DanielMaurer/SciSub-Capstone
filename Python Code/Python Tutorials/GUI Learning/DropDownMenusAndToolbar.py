from tkinter import *

# ALL MENU ITEMS ARE IN THE MAIN MENU BAR, NOT IN THE WINDOW

def doNothing():
    print("Menu item was pressed")

root = Tk()
root.geometry("500x300")

# ----------- MENU BAR ------------
menu = Menu(root) # Menu item for the root
root.config(menu = menu) # Configuring the menu with the object menu

fileMenu = Menu(menu, tearoff = 0) # Menu item within the menu
fileMenu.add_command(label = "New Project...", command = doNothing)
fileMenu.add_command(label = "New...", command = doNothing)

fileMenu.add_separator()

fileMenu.add_command(label = "Exit", command = doNothing)
menu.add_cascade(label = "File", menu = fileMenu)

editMenu = Menu(menu, tearoff = 0)
editMenu.add_command(label = "Redo", command = doNothing)
menu.add_cascade(label = "Edit", menu = editMenu)

# ------------ TOOL BAR --------------
toolbar = Frame(root, bg = "blue")
insertButton = Button(toolbar, text = "Insert", command = doNothing)
insertButton.pack(side = LEFT, padx = 2, pady = 2)
printButton = Button(toolbar, text = "Print", command = doNothing)
printButton.pack(side = LEFT, padx = 4, pady = 4)

toolbar.pack(side = TOP, fill = X) # Be sure to fill in the X direction

# ------------- Status Bar -----------------
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()

