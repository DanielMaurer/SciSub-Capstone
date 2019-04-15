from tkinter import *


root = Tk()

# Need to create a canvas in order to draw
canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

blackLine = canvas.create_line(0,0,50,50) # Starting from the top left
redLine = canvas.create_line(50,50, 100, 150, fill = "red")

greenBox = canvas.create_rectangle(25, 25, 60, 100, fill = "green") #starting location, width then height

'''canvas.delete(redLine)
canvas.delete(ALL)'''

root.mainloop()
