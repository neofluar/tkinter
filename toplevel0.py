import sys
from tkinter import Label, Button, Toplevel

win1, win2 = Toplevel(), Toplevel()
Button(win1, text='Top Window Button 1', command=sys.exit).pack()
Button(win2, text='Top Window Button 2', command=sys.exit).pack()
Label(text='MAIN WINDOW').pack()
win1.mainloop()
