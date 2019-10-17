import serial

import matplotlib
matplotlib.use("TkAgg") # The backend for matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import *
from tkinter import ttk

# ========================== Defining Variables ===========================
ser = serial.Serial('/dev/ttyACM0', 9600) # MAY HAVE TO CHANGE THIS VARIABLE EACH TIME
collectionTime = 0
titles = ['Time (s)', 'Temperature (°C)', 'Pressure', 'Turbidity'] # Adjust accordingly
time = []
temperature = []
pressure = []
turbidity = []

LARGE_FONT = ("Verdana", 12)
TITLE_FONT = ("Verdana", 24)
SUBTITLE_FONT = ("Verdana", 16)


# ========================== Sci-Sub Class ===========================
class SciSubCap(tk.Tk): # tk will be inherited
    """This class will hold the main functions for data collection and graphing
        as well as how to move from window to window."""

    def __init__(self, *args, **kwargs): # args shows that we can pass anything in, kwargs represents passing dictionaries

        tk.Tk.__init__(self, *args, **kwargs) # Lets initialize Tkinter too

        tk.Tk.wm_title(self, "Sci-Sub")
        
        container = tk.Frame(self) # creating a window
        container.pack(side="top", fill="both", expand=True) #Fill will fill the entire space, expand will go until there is no space
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # Frames will represent the windows of the application

        # ADD NEW FRAMES TO THIS LIST!
        for F in (StartPage, PageGraph):
            frame = F(container, self) # This is defining the start page and giving access to the containter
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # sticky says which directions that you want to stretch to

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """ Selects which frame is currently showing """
        frame = self.frames[cont] # cont is the key for what frame is being raised
        frame.tkraise()

    def retrieve_input(self, time_entry, status_label, view):
        """ Takes the input from the text box and updates the status label """
        global collectionTime
        if collectionTime is not -1: # If this is the first time
            textInput = time_entry.get("1.0", "end-1c")
            if textInput is '':
                status_label['text'] = "Input a collection time first..."
                view.update()
            else:
                try:
                    collectionTime = int(textInput)
                    print(collectionTime)
                    status_label['text'] = "Ready to start collection..."
                    view.update()
                except ValueError:
                    status_label['text'] = "Input a number and try again..."
                    view.update()
        else: # If data was already collected
            status_label['text'] = "No more data to be collected..."
            view.update()

    def intList(self):
        '''Convert all values in the time, temperature, pressure and turbidity
        lists into integers.'''
        global time, temperature, pressure, turbidity
        time = list(map(int, time))
        temperature = list(map(float, temperature))
        pressure = list(map(float, pressure))
        turbidity = list(map(float, turbidity))

    def start_data_collection(self, status_label, controller, view):
        """ Collects data for amount of time specified by the user. This method interacts with the Arduino,
            both starting and stopping its data collection. """
        global collectionTime
        print("This function will start the data collection")
        if collectionTime == 0: # If no data collection time was specified
            status_label['text'] = "Enter collection time then try again..."
            view.update()
        elif collectionTime == -1: # If data was already collected
            status_label['text'] = "No more data will be collected for this trial..."
            view.update()
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
                # Update the status bar
                percentage = (int(readable[0])/collectionTime)*100
                percentage = round(percentage, 2)
                status_label['text'] = "Collection {}% complete".format(percentage)
                view.update()
            
            controller.intList() # Convert all the list attributes to integers
            ser.write('end'.encode()) # Serial.end() command on the arduino
            collectionTime = -1
            status_label['text'] = "Data collection complete..."
            view.update()

    def graphData(self, status_label, view, data):
        """ Graph data based on user choice. """
        global titles, time, temperature, pressure, turbidity
        if data is 1:
            plt.plot(time, temperature)
        elif data is 2:
            plt.plot(time, pressure)
        elif data is 3:
            plt.plot(time, turbidity)
        plt.title("{} Change".format(titles[data]))
        plt.xlabel(titles[0])
        plt.ylabel(titles[data])
        plt.grid(True)
        plt.show()


class StartPage(tk.Frame):
    """ This class is the main menu of the application. Collection time is specified, data collection begins,
        and navigation to other frames is initiated. """


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        title_label = tk.Label(self, text="Sci-Sub", font=TITLE_FONT)
        title_label.pack()

        subtitle_label = tk.Label(self, text="Leading innovation in submersable research", font=SUBTITLE_FONT)
        subtitle_label.pack(pady=5)

        #space_label = tk.Label(self, text="              ", font=SUBTITLE_FONT)
        #space_label.pack()

        time_label = tk.Label(self, text="Enter the collection time:", font=LARGE_FONT)
        time_label.pack()

        time_entry = tk.Text(self, height=1, width=10)
        time_entry.pack()

        button_time_enter = ttk.Button(self, text="Enter", command=lambda: controller.retrieve_input(time_entry,status_label, self))
        button_time_enter.pack()

        button_start_data = ttk.Button(self, text="Start Collection", command=lambda: controller.start_data_collection(status_label, controller, self))
        button_start_data.pack()


        button_view_graph = ttk.Button(self, text="View Data", command=lambda: controller.show_frame(PageGraph))
        button_view_graph.pack()

        status_label = tk.Label(self, text="Insert a collection time (in seconds) and press enter...", bd=1, relief=SUNKEN, anchor=W)
        status_label.pack(side=BOTTOM, fill=X)


        '''
        button3 = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(PageThree))
        button3.pack()'''





class PageGraph(tk.Frame): # This frame will display the graph
    """ This class is the menu for which data should be graphed. """

    def __init__(self, parent, controller):
        global titles, time, temperature, pressure, turbidity
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button_temp = ttk.Button(self, text="Time v. Temperature", command=lambda: controller.graphData(status_label, self, 1))
        button_temp.pack()

        button_pressure = ttk.Button(self, text="Time v.z Pressure", command=lambda: controller.graphData(status_label, self, 2))
        button_pressure.pack()

        button_turbidity = ttk.Button(self, text="Time v. Turbidity", command=lambda: controller.graphData(status_label, self, 3))
        button_turbidity.pack()

        status_label = tk.Label(self, text="Select a datatype to graph", bd=1, relief=SUNKEN, anchor=W)
        status_label.pack(side=BOTTOM, fill=X)
        
        """
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        #a.plot(time, temperature)
        #a.plot

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #toolbar = NavigationToolbar2Tk(canvas, self)
        #toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        """




app = SciSubCap()
app.mainloop()

"""
Extra page classes for expansion

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",command=lambda: controller.show_frame(PageOne))
        button2.pack()
        """
