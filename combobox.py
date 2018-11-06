import tkinter as tk
from tkinter import ttk


def numSelected(n):
    statusLabel.configure(text="You selected:" + num.get())


# define window
win = tk.Tk()
win.title("Basic Combobox")
# set the intial dimensions of window
win.geometry("500x300")

# define label
label = ttk.Label(win, text="Select Number:")
label.grid(column=0, row=0)

# define value holder(binding value) for combobox
num = tk.StringVar()
# define combobox
combo = ttk.Combobox(win, textvariable=num)
combo.grid(column=0, row=1)
# bind event to combobox when selected
combo.bind('<<ComboboxSelected>>', numSelected)
# provide datasource for combobox
combo['values'] = list(x for x in range(1, 100) if x % 2 == 0)
# choose current item
combo.current(0)


# status label
statusLabel = ttk.Label(win, text="Status: ")
statusLabel.grid(column=0, row=5)

win.mainloop()
