import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('Tabbed panel basics')

tabControl = ttk.Notebook(win)

tab1 = ttk.Labelframe(tabControl, text="This is Tab 1")
tabControl.add(tab1, text="Tab 1")

tab2 = ttk.Labelframe(tabControl, text="This is Tab 2")
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

win.geometry('200x200')
win.mainloop()
