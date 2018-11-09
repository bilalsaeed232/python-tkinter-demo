import tkinter as tk
from tkinter import Spinbox


win = tk.Tk()
win.title('Spinbox example')
win.geometry('250x250')

mainFrame = tk.LabelFrame(win, text="Main")
mainFrame.grid(column=0, row=0, sticky='NESW')


def _spinned():
    print('Value: ', spin1.get() + '\n')


spin1 = Spinbox(mainFrame,
                from_=0, to=20,
                width=8,  # defaults to 20
                relief=tk.GROOVE,  # defaults to GROOVE
                bd=5,  # border size
                command=_spinned
                )
spin1.grid(column=0, row=0, padx=20, pady=20)

spin2 = Spinbox(mainFrame,
                from_=0, to=10,
                width=8,
                relief=tk.RAISED,
                bd=5
                )
spin2.grid(column=0, row=1)


win.mainloop()
