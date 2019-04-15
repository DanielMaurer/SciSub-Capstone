from tkinter import *

root = Tk()

# Make the functions
def leftClick(event):
    print("left")

def middleClick(event):
    print("middle")

def rightClick(event):
    print("right")

# Declare the widgets
frame = Frame(root, width = 300, height = 250)

# Bind the events
frame.bind("<Button-1>", leftClick) # if you left click, it will call the function
frame.bind("<Button-3>", middleClick)
frame.bind("<Button-2>", rightClick)

# Pack to the screen
frame.pack()


root.mainloop()
