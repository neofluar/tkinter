from tkinter import *
widget = Button(text='CONFIGURED BUTTON',
                padx=10,
                pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby',   # coursor: watch, pencil, cross, and hand2
              bd=8,             # border width
              relief=RAISED,    # border style: FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE
              bg='dark green',
              fg='white',
              font=('helvetica', 20, 'italic bold'))
widget.mainloop()
