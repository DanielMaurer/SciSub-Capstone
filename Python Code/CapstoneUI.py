from tkinter import *
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import os


class File:
    """This class will contain methods to read a file and access to its respective arrays"""

    def __init__(self):
        self.fileName = "" # NOne
        self.file = None

        # Initialize the arrays for graphing
        self.titles = []
        self.time = []
        self.temperature = []
        self.pressure = []
        self.turbidity = []

    def selectFile(self):
        self.fileName = str(os.path.basename(filedialog.askopenfilename()))
        File.readFile(self)
        File.unpackFile(self)

    def readFile(self):
        self.file = open(self.fileName, "r")

    def unpackFile(self):
        data = self.file.readlines()

        # Fill each data array with value from the text file
        for line in data:
            val = line.split()
            self.time.append(val[0])
            self.temperature.append(val[1])
            self.pressure.append(val[2])
            self.turbidity.append(val[3])

        # Get the name of each array then remove the string from the list
        # FIND A WAY TO NOT REPEAT
        self.titles.append(self.time[0])
        self.time.pop(0)
        self.titles.append(self.temperature[0])
        self.temperature.pop(0)
        self.titles.append(self.pressure[0])
        self.pressure.pop(0)
        self.titles.append(self.turbidity[0])
        self.turbidity.pop(0)

        # Convert data lists from strings to numbers
        self.time = list(map(int, self.time))
        self.temperature = list(map(int, self.temperature))
        self.pressure = list(map(int, self.pressure))
        self.turbidity = list(map(int, self.turbidity))

class Plot(File):
    """This class will contain methods to graph various values."""

    def __init__(self):

        # Find max and min of each data set
        self.minTime = np.amin(f.time)
        self.maxTime = np.amax(f.time)
        self.minTemp = np.amin(f.temperature)
        self.maxTemp = np.amax(f.temperature)
        self.minPres = np.amin(f.pressure)
        self.maxPres = np.amax(f.pressure)
        self.minTurb = np.amin(f.turbidity)
        self.maxTurb = np.amax(f.turbidity)

    # Need to define individual functions because button commands cannot pass values into functions
    def plotTemperature(self):
        plt.plot(f.time, f.temperature)
        plt.suptitle("Time v. Temperature")
        plt.ylabel("Temperature (C)")
        plt.xlabel("Time (s)")
        plt.axis([self.minTime, self.maxTime, self.minTemp, self.maxTemp])
        plt.show()

    def plotPressure(self):
        plt.plot(f.time, f.pressure)
        plt.suptitle("Time v. Pressure")
        plt.ylabel("Pressure (unit)")
        plt.xlabel("Time (s)")
        plt.axis([self.minTime, self.maxTime, self.minPres, self.maxPres])
        plt.show()

    def plotTurbidity(self):
        plt.plot(f.time, f.turbidity)
        plt.suptitle("Time v. Turbidity")
        plt.ylabel("Turbidity (unit)")
        plt.xlabel("Time (s)")
        plt.axis([self.minTime, self.maxTime, self.minTurb, self.maxTurb])
        plt.show()


# -------------- Define parameters for the window --------------
root = Tk()
root.geometry("600x400")
root.title("DataSub")

# ---------------------- Designing the UI -------------------------
titleFrame = Frame(root)
titleFrame.pack(side=TOP)
contentFrame = Frame(root)
contentFrame.pack()

titleLabel = Label(titleFrame, text="Sci-Sub", anchor=W)
titleLabel.config(font=("TkDefaultFont", 20))
titleLabel.pack()
descriptionLabel = Label(titleFrame, text="Leading innovation in submersable research")
descriptionLabel.pack()

# ----------------- Selecting the file ------------------------


# ------------ Code for selecting and reading the a file  ---------------
f = File()  # create a file object
fileButton = Button(contentFrame, text="Select file", command=f.selectFile).grid(row=0, column=1)  # Button that will give user option to select a file
#f.readFile() # read the file
#f.unpackFile() # unpack file data into respective lists

# ------------ Code for graphing the file ---------------
p = Plot()

# ==== Add some buttons to select the info graphed ======
tempButton = Button(contentFrame, text=f.titles[1], command=p.plotTemperature).grid(row=1, column=0)
presButton = Button(contentFrame, text=f.titles[2], command=p.plotPressure).grid(row=1, column=1)
turbButton = Button(contentFrame, text=f.titles[3], command=p.plotTurbidity).grid(row=1, column=2)


root.mainloop()

