import tkinter as tk
from tkinter import ttk


def changeButtonText():
    btn.configure(text="Hello "+name.get())


# define window
win = tk.Tk()
win.title("Simple Textbox example")


# define label
label = ttk.Label(win, text="Enter Your Name:")
label.grid(column=0, row=0)

# define value holder(binding variable) for textbox
name = tk.StringVar()
# define textbox
textBox = ttk.Entry(win, textvariable=name)
textBox.grid(column=0, row=1)
textBox.focus()

# define a button
btn = ttk.Button(win, text="Click Me", command=changeButtonText)
btn.grid(column=1, row=1)

# actually runs the window
win.mainloop()
