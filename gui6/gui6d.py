from tkinter import *
from gui6.gui6a import Hello


class HelloExtended(Hello):
    def make_widgets(self):
        Hello.make_widgets(self)
        Button(self,
               text='EXTEND',
               command=self.quit).pack(side=RIGHT)

    def print_message(self):
        print('Hello', self.data)


if __name__ == '__main__':
    HelloExtended().mainloop()
