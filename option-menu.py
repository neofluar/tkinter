from tkinter import *

master = Tk()
vals = "one", "two", "three"
variable = StringVar(master)
variable.set("one")  # default value

w = OptionMenu(master, variable, *vals)
w.config(width=5)
w.pack()

mainloop()
