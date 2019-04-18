# This code will be the backend support for the Sci-Sub project
'''
Goals for this code are to:
1. Contain methods for serial interaction with the Arduino
 - This will include different functions based on that instruments should be activated
   as well as how long data will be collected for
2. Contain methods to write sensor data to some sort of file
 - Previous models wrote to text files and parsed data by line
3. Contain methods to graph and analize data
 - Matplotlib has functionality to modify how the data is being presented, will
   utilize this
'''
# 1-2. Import serial library
import serial

# 3. Import statements for numerical manipulation and graphing
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np

# ========================== Defining Variables ===========================
ser = serial.Serial('/dev/ttyACM1', 9600) # MAY HAVE TO CHANGE THIS VARIABLE EACH TIME
collectionTime = 0

# ========================== Defining functions ===========================
''' This set of functions will react to the user choice'''

def setCollectionTime():
    print("This function will edit the time that data will be collected for") # TODO: Need to interact with the arduino code to set a data collection time (This will be done in the while loop)
    global collectionTime
    collectionTime = int(input("Enter the time that data will be collected: "))
    

def startDataCollection():
    print("This function will start the data collection")
    print("The collection time is {} seconds.".format(collectionTime))
    if collectionTime == 0:
        print("Specify data collection time then try again...")
    else:
        while 1: # TODO: Will need to write a function that will stop the loop after one time iteration
            ser.write(b's') # This value will need to be changed with respect to the arduino code
            arduinoData = ser.readline().strip()
            print(arduinoData.decode('utf-8'))
        

def graphData():
    print("This function will graph the data")

def editGraph():
    print("This function will edit the contents of the graph")



# ========================== Main Code ===========================
''' This first section of code will preface the user with options on what data
    they would like to see collected '''

choices = {
    "1": setCollectionTime,
    "2": startDataCollection,
    "3": graphData,
    "4": editGraph,
}

while True:
    print(
        """
    Sci-Sub Menu:

    1. Set data collection time
    2. Start data collection
    3. Graph data collected
    4. Modify graph components
    """
        )
    choice = input("Enter an option: ")
    action = choices.get(choice)
    if action:
        action()
    else:
        print("{0} is not a valid choice".format(choice))

