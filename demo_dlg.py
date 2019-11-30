from tkinter import *
from dialog_table import demos
from quitter_button import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent=None, **options)
        self.pack()
        Label(self, text='Basic Demo').pack()
        for key, value in demos.items():
            Button(self, text=key, command=value).pack(side=TOP,
                                                       fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    Demo().mainloop()
