from sys import exit
from tkinter import *
from gui6.gui6a import Hello

parent = Frame(None)
parent.pack()
Hello(parent).pack(side=RIGHT)
Button(parent, text='ATTACH', command=exit).pack(side=LEFT)
parent.mainloop()
