from tkinter import *
from quitter_button import Quitter


def fetch():
    print('Input =>', ent.get())
    ent.insert(END, 'X')
    ent.insert(0, 'Y')


root = Tk()
ent = Entry(root)
ent.config(show='*')
ent.insert(0, 'Type here')
ent.pack(side=TOP, fill=X)

ent.focus()
ent.bind('<Return>', (lambda event: fetch()))
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
