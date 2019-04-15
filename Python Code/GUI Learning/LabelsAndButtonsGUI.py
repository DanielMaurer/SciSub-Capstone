from tkinter import *

root = Tk() # this will create a blank window using tkinter constructor

#Create the frames
topFrame = Frame(root) # Make a container in the root window
topFrame.pack() # puts the frame in to the root window, default goes in the window
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM) # Place on the bottom of the other frame

# Parameters for a button are...(frame, text on the button, color of button)
button1 = Button(topFrame, text = "Button 1")
button2 = Button(topFrame, text = "Button 2")
button3 = Button(topFrame, text = "Button 3")
button4 = Button(bottomFrame, text = "Button 4")
label1 = Label(root, text = "One", bg = "red", fg = "white")
label2 = Label(root, text = "Two", bg = "blue", fg = "orange")


button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM, fill = X)
label1.pack(fill=X) # automatically in the topFrame
label2.pack(side = LEFT, fill = Y) # automatically in the bottomFrame

root.mainloop()

