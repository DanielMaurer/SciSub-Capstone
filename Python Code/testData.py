file = open("test.txt","w")
file.write("Time\tTemperature\tPressure\tTurbidity\n")
time = 0
temperature = 1
pressure = 5
turbidity = 10
for i in range (20):
    string = "{0} {1} {2} {3}\n".format(time, temperature, pressure, turbidity)
    file.write(string)
    time += 1
    temperature += 2
    pressure = pressure * 2
    turbidity = turbidity -1

file.close()
