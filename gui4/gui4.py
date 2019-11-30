from tkinter import *


def greeting():
    print('Hello Panda!')


win = Frame()
win.pack()
Label(win,
      text='Greet the Panda The Great!').pack(side=TOP,
                                              expand=YES)
Button(win,
       text='Say hello',
       command=greeting).pack(side=LEFT)
Button(win,
       text='Quit',
       command=win.quit).pack(side=RIGHT)
win.mainloop()
