import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Basic label')

# will automatically consumes the space needed to fix the text
ttk.Label(win, text="Basic label text").grid(column=0, row=10)

win.mainloop()
