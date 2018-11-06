import tkinter as tk
from tkinter import ttk


def statusSelected():
    radSel = maritalStatusVar.get()
    if (radSel == 1):
        print('Single')
    elif (radSel == 2):
        print('Married')
    else:
        print('Divorced')


win = tk.Tk()
win.geometry('400x200')
win.title('Basic radio button example')

maritalStatusVar = tk.IntVar()

singleRb = ttk.Radiobutton(
    win, text="Single", variable=maritalStatusVar, value=1, command=statusSelected)
singleRb.grid(column=0, row=0, sticky=tk.W)

marriedRb = ttk.Radiobutton(
    win, text="Married", variable=maritalStatusVar, value=2, command=statusSelected)
marriedRb.grid(column=0, row=1, sticky=tk.W)

divorcedRb = ttk.Radiobutton(
    win, text="Divorced", variable=maritalStatusVar, value=3, command=statusSelected)
divorcedRb.grid(column=0, row=2, sticky=tk.W)

win.mainloop()
