from tkinter import *

msg = Message(None, text='Smack my bitch up')
msg.config(font=('helvetica', 18, 'normal'),
           bg='pink',
           fg='black')
msg.pack(expand=YES, fill=X)
mainloop()
