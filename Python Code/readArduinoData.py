import serial

ser = serial.Serial('/dev/ttyACM1', 9600)

while 1:
    userInput = input("Enter 's' to take data: ")

    while userInput == 's':
        ser.write(b's')
        arduinoData = ser.readline().strip()
        print(arduinoData.decode('utf-8'))
