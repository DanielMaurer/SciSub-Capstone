import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    userInput = input("Enter 's' to take data: ")

    if userInput == 's':
        ser.write(b's')
        arduinoData = ser.readline()
        print(arduinoData)
