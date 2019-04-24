from tkinter import *


class DannysButtons:

    def __init__(self, master): # constructor for the DannysButtons class, master is the root or main window 
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "Quit Button", command = master.quit) # already in tkinter library
        self.quitButton.pack(side = LEFT)

    def printMessage(self): #have to throw in the self object
            print("This is so dang cool")

root = Tk()

b = DannysButtons(root)

root.mainloop()
