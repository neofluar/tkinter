# Using bind method (more general approach)
from tkinter import *


def hello(event):
    print('Double-click to exit')


def goodbye(event):
    print('Exiting...')
    sys.exit()


widget = Button(None,
                text='Event! What event?')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', goodbye)
widget.mainloop()
