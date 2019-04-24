from tkinter import *
from tkinter import filedialog

root = Tk()

fileName = filedialog.askopenfilename()
print(fileName)

root.mainloop()

