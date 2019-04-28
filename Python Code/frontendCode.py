import matplotlib
matplotlib.use("TkAgg") # The backend for matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

# Declaring font constants
LARGE_FONT = ("Verdana", 12)
TITLE_FONT = ("Verdana", 24)
SUBTITLE_FONT = ("Verdana", 16)


class SciSubCap(tk.Tk): # tk will be inherited

    def __init__(self, *args, **kwargs): # args shows that we can pass anything in, kwargs represents passing dictionaries

        tk.Tk.__init__(self, *args, **kwargs) # Lets initialize Tkinter too

        tk.Tk.wm_title(self, "Sci-Sub")
        
        container = tk.Frame(self) # creating a window
        container.pack(side="top", fill="both", expand=True) #Fill will fill the entire space, expand will go until there is no space
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # Frames will represent the windows of the application

        # ADD NEW FRAMES TO THIS LIST!
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self) # This is defining the start page and giving access to the containter
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # sticky says which directions that you want to stretch to

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont] # cont is the key for what frame is being raised
        frame.tkraise()

    def start_data_collection(self):
        print("This function will start the data collection")



class StartPage(tk.Frame):

    def retrieve_input(self, time_entry):
        self.collectionTime = int(time_entry.get("1.0", "end-1c"))
        print(self.collectionTime)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.collectionTime = 0
        
        title_label = tk.Label(self, text="Sci-Sub", font=TITLE_FONT)
        title_label.grid(row=0, column=1)

        subtitle_label = tk.Label(self, text="Leading innovation in submersable research", font=SUBTITLE_FONT)
        subtitle_label.grid(row=1, column=1)

        space_label = tk.Label(self, text="              ", font=SUBTITLE_FONT)
        space_label.grid(row=2, column=1)
        space_label.grid(row=2, column=0)
        space_label.grid(row=6, column=1)
        space_label.grid(row=7,column=1)

        time_label = tk.Label(self, text="Enter the collection time:", font=LARGE_FONT)
        time_label.grid(row=3, column=1)

        time_entry = tk.Text(self, height=1, width=10)
        time_entry.grid(row=4, column=1)

        button_time_enter = ttk.Button(self, text="Enter", command=lambda: self.retrieve_input(time_entry))
        button_time_enter.grid(row=4, column=2)

        button_start_data = ttk.Button(self, text="Start Collection", command=lambda: controller.start_data_collection())
        button_start_data.grid(row=5, column=1)

        button_view_graph = ttk.Button(self, text="View Data", command=lambda: controller.show_frame(PageThree))
        button_view_graph.grid(row=8, column=1)

        '''
        button3 = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(PageThree))
        button3.pack()'''


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


class PageThree(tk.Frame): # This frame will display the graph

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [8,7,6,5,4,3,2,1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




app = SciSubCap()
app.mainloop()
