# Callback coding scheme - callable class
from tkinter import *


class CallableRacoon:
    def __init__(self):
        self.message = 'I am not!'

    def __call__(self):
        print(self.message)
        sys.exit()


widget = Button(None,
                text='Am I hot?',
                command=CallableRacoon())
widget.pack()
widget.mainloop()
