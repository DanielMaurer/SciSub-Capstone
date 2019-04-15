import serial

arduinoData = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    myData = arduinoData.readline()
    print(myData)
