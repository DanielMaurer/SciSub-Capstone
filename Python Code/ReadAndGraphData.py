import matplotlib.pyplot as plt

#Open the file and copy the information
file = open("test.txt", "r")
data = file.readlines()
print(data)

#Create an array for each data type
titles = []
time = []
temperature = []
pressure = []
turbidity = []

# Fill each data array with value from the text file
for line in data:
    val = line.split()
    time.append(val[0])
    temperature.append(val[1])
    pressure.append(val[2])
    turbidity.append(val[3])

# Get the name of each array then remove the string from the list
titles.append(time[0])
time.pop(0)
titles.append(temperature[0])
temperature.pop(0)
titles.append(pressure[0])
pressure.pop(0)
titles.append(turbidity[0])
turbidity.pop(0)

# Define a plot
# In this case, I will be plotting the temperature v. time
plt.plot(time, temperature)
plt.title("Temperature Change")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()

file.close()
