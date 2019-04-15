from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo('Window Title', 'This is a fun fact')
answer = tkinter.messagebox.askquestion('Questions 1', 'Are you cool')
if answer == 'yes':
    print("Im sure you are")

root.mainloop()
