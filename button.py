import tkinter as tk
from tkinter import ttk


# event for button click
def changeColor():
    label.configure(text="blue label")


win = tk.Tk()
win.size = (200, 200)

label = ttk.Label(win, text="Red label")
label.grid(column=0, row=0)

button = ttk.Button(win, text="Change color",
                    command=changeColor)
button.grid(column=1, row=0)


win.mainloop()
