from tkinter import *
from tkinter import ttk

def first():
    global root
    root = Tk()
    root.title("financeByUnutkan")
    #root.attributes("-zoomed", True) # you can also use fullscreen
    #root.configure(
    #    background="black") # TUM ARKA PLANIN RENGINI DEGISTIRIYOR



def second():
    global first_frame
    first_frame = ttk.Frame(
        root,
        height=400,
        width=400
        )
    
    first_frame.grid(
        row=0,
        column=0
        #sticky=(N,W,E,S)
        )

first()
second()

# CLASSLARDA ISIM DEGISIKLIGINE GITMEK DOGRU OLACAKTIR


def minimize_screen(): # burasi pek onemli degil
    root.iconify()


def options_screen():
    options_root = Tk()
    options_root.title("OPTIONS")
    #options_root.configure(background="black") # it's not working!
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

options_menu = ttk.Button(
    first_frame,
    text="Options",
    command=options_screen

)
options_menu.grid(
    column=1,
    row=1,
    #sticky=(N,W,E,S),
    padx=5,
    pady=5
)

title_area = ttk.Label(
    first_frame,
    text="FINANCE BY UNUTK4N",

)
title_area.grid(
    column=2,
    row=1,
    #sticky=(N,W,E,S)
    padx=5,
    pady=5
)

minimize_button = ttk.Button(
    first_frame,
    text="--",
    command = minimize_screen
)
minimize_button.grid(
    column=3,
    row=1,
    #sticky=(N,W,E,S),
    padx=5,
    pady=5
)

resize_button = ttk.Button(
    first_frame,
    text="resize"
)
resize_button.grid(
    column=4,
    row=1,
    #sticky=(N,W,E,S)
    padx=5,
    pady=5
)

def on_change(b):
    a = b.widget.get() # we have to use the widget word or else it won't work.
    with open("profit.txt", "a") as f:
        z = 0
        f.write(f"{a} TL\n")
    



# BELOW NAMES NEED TO BE CHANGED
        

asd = ttk.Label(
    first_frame,
    text="PROFIT BELOW"
)
asd.grid(
    column=1,
    row=2,
    padx=5,
    pady=5
)

a = StringVar()
b = ttk.Entry(
    first_frame,
    textvariable = a

    
)
b.grid(
    column=1,
    row=3,
    #sticky=(W)
    padx=5,
    pady=5
)
def clear_text():
    b.delete(0,'end')

#the reason we do this is that we need a callback to make it work
b.bind("<Return>", on_change)
#b.bind("<Return>", clear_text)


with open("profit.txt","r") as f:
    deger = 0
    for line in f:
        deger = deger + int(line)
    print(deger)



root.mainloop()

