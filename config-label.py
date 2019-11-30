from tkinter import *
root = Tk()
labelfont = ('times',  # courier, helvetica
             20,
             'bold underline')   # combination of normal, roman, italic, overstrike
widget = Label(root, text='COFIGURED LABEL')
widget.config(bg='black',
              fg='yellow',
              font=labelfont,
              height=3,
              width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
