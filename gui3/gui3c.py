# Callback coding scheme - class method
from tkinter import *


class HiRacoonClass:
    def __init__(self):
        widget = Button(None,
                        text='OMG!',
                        command=self.please_quit)
        widget.pack()

    def please_quit(self):
        print('Goodbye, the ugly cruel world!')
        sys.exit()


HiRacoonClass()
mainloop()
