import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()

win1, win2 = Tk(), Tk()
Button(win1, text='111', command=win1.destroy).pack()
Button(win2, text='222', command=win2.destroy).pack()
win1.mainloop()
