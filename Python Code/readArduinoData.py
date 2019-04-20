import serial

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np

ser = serial.Serial('/dev/ttyACM0', 9600)
titles = ['Time (s)', 'Temperature (°C)', 'Pressure', 'Turbidity'] # Adjust accordingly
time = []
temperature = []
pressure = []
turbidity = []

def intList():
    '''Convert all values in the time, temperature, pressure and turbidity
       lists into integers.'''
    global time, temperature, pressure, turbidity
    time = list(map(int, time))
    temperature = list(map(float, temperature))
    pressure = list(map(float, pressure))
    turbidity = list(map(float, turbidity))

while 1:
    userInput = input("Enter 's' to take data: ")

    if userInput == 's':
        for i in range(5): # Whatever is the amount of data points that you want plus the two for the titles and blank line
            ser.write(b's')
            arduinoData = ser.readline().strip()
            #print(arduinoData)
            readable = arduinoData.decode('utf-8').split('\t')
            print(readable)
            time.append(readable[0])
            temperature.append(readable[1])
            pressure.append(readable[2])
            turbidity.append(readable[3])
            
            #if i is 0:
        intList() # Convert all the list attributes to integers
        print(time)
        print(temperature)
        print(pressure)
        print(turbidity)
        plt.plot(time, temperature)
        plt.title("Temperature Change")
        plt.xlabel("Time")
        plt.ylabel("Temperature")
        plt.grid(True)
        plt.show()
    else:
        userInput = 'd'
        ser.write(b'd')
