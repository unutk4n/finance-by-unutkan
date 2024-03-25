from tkinter import *
from tkinter import ttk
import datetime


current_date = datetime.date.today()
recurrent_date = current_date.strftime("%d-%m-%Y")





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
class Definitions():
    def to_do():
        todo_root = Tk()
        todo_root.title("To Be Done")
        todo_frame = ttk.Frame(
            todo_root,
            height=500,
            width=300
        )
        todo_frame.grid(
            column=0,
            row=0,
            sticky=(N,W,E,S)
        )        
    def options_screen():# option window 
        options_root = Tk()
        options_root.title("OPTIONS")
        options_frame = ttk.Frame(
            options_root,
            height=500,
            width=800
        )
    
        options_frame.grid(
            column=0,
            row=0,
            sticky=(N,W,E,S)
        )

        options_root.mainloop()

    def on_change(b):
        a = b.widget.get() # we have to use the widget word or else it won't work.
        with open("profit.txt", "a") as f:
            z = 0
            f.write(f"{a} \n") # buranin sonuna tl koymustum ancak asagida bir fonskyon cagirdigimda int olarak almak gerekiyor.
   
    def show_sum_profit_def():
        with open("profit.txt") as f:
            try:
                toplama = 0
                for line in f:
                    toplama = toplama + int(line)
                    print(toplama)
            except ValueError:
                pass 
    
    def to_be_sent_def():
        sent_def = Tk()
        sent_def.title("NEREYE NE GIDECEK")

        sent_def_frame = ttk.Frame(
            sent_def,
            height=500,
            width=550
        )
        sent_def_frame.grid(
            column=0,
            row=0,
           sticky=(N,W,E,S)

        )
        nereye = ttk.Label(
            sent_def_frame,
            text= "NEREYE GIDIYOR"
        
        )
        nereye.grid(
            column=0,
            row=0,
            padx=5,
            pady=5
        )
        a = StringVar()
        b = ttk.Combobox(
            sent_def_frame,
            textvariable= a
        )
        b['values'] = ('ZIRAAT', 'GARANTI', 'VAKIF')

        b.grid(
            column=0,
            row=1,
            padx=5,
            pady=5
        )
        b.state(["readonly"])

        c = ttk.Label(
            sent_def_frame,
            text= "NE GIDECEK"
        )
        c.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        d = StringVar()
        e = ttk.Combobox(
            sent_def_frame,
            textvariable= d
        )
        e.grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )
        e['values'] = ('SU', 'EKMEK', 'PATATES')
        e.state(["readonly"])

        f = ttk.Label(
            sent_def_frame,
            text="KAC ADET/MIKTAR"
        )
        f.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        g = StringVar()
        h = ttk.Combobox(
            sent_def_frame,
            textvariable=g
        )
        h.grid(
            column=3,
            row=1,
            padx=5,
            pady=5
        )
        h['values'] = ('1','2','3')
        h.state(["readonly"])



        sent_def.mainloop()

class Buttons():

    options_button_00 = ttk.Button(
        Rootly.first_frame,
        text="Setings",
        command=Definitions.options_screen
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
        command= Definitions.show_sum_profit_def
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
        command=Definitions.to_do
        )
    todo_button.grid(
        column=2,
        row=1,
        padx=5,
        pady=5
        )
    where_is_going_what = ttk.Button(
        Rootly.first_frame,
        text="NEREYE NE GIDECEK",
        command=Definitions.to_be_sent_def
    )

    where_is_going_what.grid(
        column=1,
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
    date_label = ttk.Label(
        Rootly.first_frame,
        text=recurrent_date
    )
    date_label.grid(
        row=0,
        column=2,
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

def ready_go():
    Entries()
    Labels()
    Buttons() # I WAS EXPECTING AN ERROR SINCE THE ROOTLY CLASS IS SUPPOSED TO WORK IN THE FIRST PLACE
    Rootly.root.mainloop()
    
ready_go()
