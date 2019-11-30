from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno(title='Verify',
                message='Do yu really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been canceled')


errmsg = 'Sorry, no spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam',
       command=(lambda: showerror('Spam',
                                  errmsg))).pack(fill=X)
mainloop()
