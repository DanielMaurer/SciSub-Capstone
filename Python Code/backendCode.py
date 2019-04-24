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
ser = serial.Serial('/dev/ttyACM0', 9600) # MAY HAVE TO CHANGE THIS VARIABLE EACH TIME
collectionTime = 0
titles = ['Time (s)', 'Temperature (°C)', 'Pressure', 'Turbidity'] # Adjust accordingly
time = []
temperature = []
pressure = []
turbidity = []

# ========================== Defining functions ===========================
''' This set of functions will allow the user to graph data '''

def timeTemperature():
    global titles, time, temperature
    # if time or temperature is empty, send back to main menu
    print("This function will graph Time v. Temperature")
    plt.plot(time, temperature)
    plt.title("Temperature Change")
    plt.xlabel(titles[0])
    plt.ylabel(titles[1])
    plt.grid(True)
    plt.show()

def timePressure():
    global titles, time, pressure
    # if time or pressure is empty, send back to main menu
    print("This function will graph Time v. Pressure")
    plt.plot(time, pressure)
    plt.title("Pressure Change")
    plt.xlabel(titles[0])
    plt.ylabel(titles[2])
    plt.grid(True)
    plt.show()

def timeTurbidity():
    global titles, time, turbidity
    # if time or turbidity is empty, send back to main menu
    print("This function will graph Time v. Turbidity")
    plt.plot(time, turbidity)
    plt.title("Turbidity Change")
    plt.xlabel(titles[0])
    plt.ylabel(titles[3])
    plt.grid(True)
    plt.show()

def intList():
    '''Convert all values in the time, temperature, pressure and turbidity
       lists into integers.'''
    global time, temperature, pressure, turbidity
    time = list(map(int, time))
    temperature = list(map(float, temperature))
    pressure = list(map(float, pressure))
    turbidity = list(map(float, turbidity))


''' This set of functions will react to the user choice'''

def setCollectionTime():
    print("This function will edit the time that data will be collected for") # TODO: Need to interact with the arduino code to set a data collection time (This will be done in the while loop)
    global collectionTime
    if collectionTime is not -1: # If this is the first time
        collectionTime = int(input("Enter the time that data will be collected: "))
    else: # If data was already collected
        print("No more data will be collected for this trial...")

def startDataCollection():
    global collectionTime
    print("This function will start the data collection")
    if collectionTime == 0: # If no data collection time was specified
        print("Specify data collection time then try again...")
    elif collectionTime == -1: # If data was already collected
        print("No more data will be collected for this trial...")
    else: # If this is the first time to collect data
        print("The collection time is {} seconds.".format(collectionTime))
        for i in range(collectionTime): # Take data for the given amount of time
            ser.write(('sta'+str(collectionTime)).encode()) # write the start command with time to the serial monitor
            arduinoData = ser.readline().strip() # Take the data line by line
            readable = arduinoData.decode('utf-8').split('\t') # Convert it to readable data
            print(readable)
            # Append values to their given list
            time.append(readable[0])
            temperature.append(readable[1])
            pressure.append(readable[2])
            turbidity.append(readable[3])
            
        intList() # Convert all the list attributes to integers
        ser.write('end'.encode()) # Serial.end() command on the arduino
        collectionTime = -1

            # TODO: Add a progress bar for the data collection
           

def graphData():
    print("This function will graph the data")
    global time
    if time:
        graphs = {
            "1": timeTemperature,
            "2": timePressure,
            "3": timeTurbidity,
    }
        print("""
        Select what you would like to graph:

        1. Time v. Temperature
        2. Time v. Pressure
        3. Time v. Turbidity
        """
              )
        option = input("Enter an option: ")
        action = graphs.get(option)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))

    else:
        print("Collect data then try again...")

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

