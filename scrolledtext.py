import tkinter as tk
from tkinter import scrolledtext, ttk

# when user types something


def textChanged(x):
    mirrorText.set(mirrorText.get()+x.char)
    print(mirrorText.get())


win = tk.Tk()
win.title('Write your message')
win.geometry('300x300')
win.resizable(0, 0)

label = ttk.Label(win, text="Message:")
label.grid(column=0, row=0)

mirrorText = tk.StringVar()
mirrorLabel = ttk.Label(win, text="", textvariable=mirrorText)
mirrorLabel.grid(column=0, columnspan=3, row=2)


# provide scroll width and scroll height
# note: these are magic numbers they are best practice to use them
scrolW = 30
scrolH = 3

scrVar = tk.StringVar()
# create scrolledtext widget
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,
                                wrap=tk.WORD  # word will wrap other than break
                                )

scr.grid(column=0, row=1, columnspan=5)

scr.bind('<KeyRelease>', textChanged)


win.mainloop()
