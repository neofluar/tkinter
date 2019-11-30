# Callback coding scheme - lambda
from tkinter import *


def sum_it(num1, num2):
    print(num1 + num2)


X = 5
Y = 3
root = Tk()
widget = Button(
    root,
    text='A Good Dog',
    command=(lambda: sum_it(X, Y)))
widget.pack(expand=YES, fill=NONE)
widget1 = Button(
    root,
    text='press me',
    command=(lambda: print('BY!') or sys.exit()))
widget1.pack()
widget.mainloop()
