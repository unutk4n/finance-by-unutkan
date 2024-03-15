from tkinter import *
from tkinter import ttk

class mainFrame():
    def __init__(self):
        global root 
        self.root = Tk()
        self.root.title("Finance_by_Unutkan")

        global first_frame
        self.first_frame = ttk.Frame(
            self.root,
            height=500,
            width=750
        )
        self.first_frame.grid(
            column=0,
            row=0,
            #sticky=(N,W,E,S)
        )
        self.options_button = ttk.Button(
        self.first_frame,
        text= "OPTIONS",
        )
        self.options_button.grid(
            column = 1,
            row = 1,
            padx = 5,
            pady = 5
        )


        self.root.mainloop()
     

mainFrame()