from tkinter import *

root = Tk()

#Declare the widgets
label1 = Label(root, text = "Name")
label2 = Label(root, text = "Password")
entry1 = Entry(root)
entry2 = Entry(root)
checkBox = Checkbutton(root, text = "Stay logged in")

#Insert into the screen
label1.grid(row = 0, column = 0, sticky = E) # E is for east
label2.grid(row = 1, column = 0, sticky = E)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

checkBox.grid(row = 2, columnspan = 2)


root.mainloop()
