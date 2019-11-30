# Callback coding scheme - function
from tkinter import *


def pls_quit():
    print('Go away...')
    sys.exit()


widget = Button(None,
                text='A Stupid Cat',
                command=pls_quit)
widget.pack()
widget.mainloop()
