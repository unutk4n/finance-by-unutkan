from tkinter import *
from tkinter import ttk
import datetime

#
#
#

"""TO DO BUTTON KISMINDA KALDIK"""
class Rootly():
    root = Tk()
    root.title("financeByUnutkan")
    first_frame = ttk.Frame(
        root,
        height=400,
        width=400
        )
    first_frame.grid(
        column=0,
        row=0,
        sticky=(N,W,E,S)
    )

class Buttons():

    options_button_00 = ttk.Button(
        Rootly.first_frame,
        text="Setings",
        #command=
    )
    options_button_00.grid(
    column=0,
    row=0,
    padx=5,
    pady=5
    )

    show_sum_profit = ttk.Button(
    Rootly.first_frame,
    text="SHOW SUM PROFIT",
    #command= show_sum_profit_def
)
    show_sum_profit.grid(
    column=2,
    row=3,
    padx=5,
    pady=5
)
todo_button = ttk.Button(
    Rootly.first_frame,
    text="TO DO",
    #command=to_do

)
todo_button.grid(
    column=2,
    row=1,
    padx=5,
    pady=5
)
class Labels():

    main_header = ttk.Label(
    Rootly.first_frame,
    text="FINANCE BY UNUTK4N",
    )

    main_header.grid(
    column=1,
    row=0,
    #sticky=(N,W,E,S)
    padx=5,
    pady=5
    )

    profit_header = ttk.Label(
        Rootly.first_frame,
        text="Profit Below"
    )

    profit_header.grid(
        column=0,
        row=2,
        padx=5,
        pady=5
    )

class Entries():

    profitString = StringVar()
    profit_Entry = ttk.Entry(
        Rootly.first_frame,
        textvariable= profitString
    )
    # B.BIND EKLEMESINI EN SON YAPACAGIZ
    profit_Entry.grid(
        column=0,
        row=3,
        padx=5,
        pady=5
    )






class Definitions():
    pass

Entries()
Labels()
Buttons() # I WAS EXPECTING AN ERROR SINCE THE ROOTLY CLASS IS SUPPOSED TO WORK IN THE FIRST PLACE
Rootly.root.mainloop()