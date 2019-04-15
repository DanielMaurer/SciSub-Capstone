from tkinter import *

root = Tk()

# Define some functions
def printName():
    print("Hello my name is Danny")

def printDay(event):
    print("Today is Wednesday")

# Declare the widget
button1 = Button(root, text = "Print Name", command = printName)
button2 = Button(root, text = "Print Day")
button2.bind("<Button-1>", printDay) # Left mouse button

# place on screen
button1.pack()
button2.pack()

root.mainloop()
