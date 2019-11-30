# modal and non-modal dialog style
from tkinter import *
makemodal = len(sys.argv) > 1


def dialog():
    win = Toplevel()
    Label(win, text='I am a popup!').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('dialog exit')


root = Tk()
Button(root, text='Create a popup', command=dialog).pack()
root.mainloop()
