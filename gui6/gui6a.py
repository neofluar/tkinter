from tkinter import *


class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 10
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self,
                        text='A Frame Button',
                        command=self.print_message)
        widget.pack(side=LEFT)

    def print_message(self):
        self.data += 1
        print('Look what I can:', self.data)


if __name__ == '__main__':
    Hello().mainloop()
