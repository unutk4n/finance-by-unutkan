from tkinter import *
from tkinter import ttk
import datetime
title_string = "finance by unutkan"
class finance():

    root = Tk()
    root.title(title_string)

    first_frame = ttk.Frame(
        root,
        height=400,
        width=400
        )
    first_frame.grid(
        row=0,
        column=0
    )

    title_area = ttk.Label(
        root,
        text=title_string
    )
    title_area.grid(
        column=0,
        row=0
        
        )
    root.mainloop()



finance()
