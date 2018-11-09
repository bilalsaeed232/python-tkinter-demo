import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Using label Frame")
win.geometry('300x300')


text = ttk.Entry(win, text="Enter")
text.grid(column=0, row=0)


# TODO: use LabelFrame widget to arrange all related labels together
labelFrame = ttk.LabelFrame(win, text="List of Todos")
# can modify the whole frame separately
labelFrame.grid(column=1, row=1,
                # padx & pady is used to provide horizontal and vertical padding, note: it will also affect the same elements in the current row (so choose different row)
                padx=20, pady=50
                )


label1 = ttk.Label(labelFrame, text="Todo 1")
label1.grid(column=0, row=0)
label2 = ttk.Label(labelFrame, text="Todo 2")
label2.grid(column=0, row=1)
label3 = ttk.Label(labelFrame, text="Todo 3")
label3.grid(column=0, row=2)
label4 = ttk.Label(labelFrame, text="Todo 4")
label4.grid(column=0, row=3)


win.mainloop()
