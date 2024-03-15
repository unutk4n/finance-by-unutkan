to calculate the profit or margin :
    I've made a quick reserach and using json might work just well.

# import explained#
    from tkinter import *
    from tkinter import ttk

so the first line means that we've imported everything from the tkinter module.
This is the standart Tkinter practice.
However, because we've imported just ttk itself, we'll need to prefix anything inside that submodule.
For example: Calling Entry() would refer to the Entry class inside the tkinter module(classic widget). We'd need ttk.Entry() to use the Entry class insde ttk (themed widget)






# FIRST PART EXPLAINED#
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized.

When we create a widget we need to specify its parent.

sticky >> this option describes how the widget should line up within the grid cell. Using compass directions.




iki klasor biri arti biri eksi 
for each line in folder
add each one 
gibi bir sey yapilabilir


















































Why do we put a frame inside the main window? Strictly speaking, we could just put the other widgets in our interface directly into the main application window without the intervening content frame. That's what you'll see in older Tk programs.

However, the main window isn't itself part of the newer "themed" widgets. Its background color doesn't match the themed widgets we will put inside it. Using a "themed" frame widget to hold the content ensures that the background is correct. This is illustrated below. 