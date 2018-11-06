import tkinter as tk
from tkinter import ttk


def updateStatus():
    st = 'You selected: [ '
    st += ' "' + musicCb.cget('text') + '"' if cbVarMusic.get() else ''
    st += ' "' + gamesCb.cget('text') + '"' if cbVarGames.get() else ''
    st += ' "' + sportsCb.cget('text') + '"' if cbVarSports.get() else ''

    st += ' ]'

    status.set(st)
    print(st)


win = tk.Tk()
win.title('Select your interests')
win.geometry('500x300')
win.resizable(0, 0)

label = ttk.Label(win, text="Select your inteerest:")
label.grid(column=0, row=0, sticky=tk.W)

# create checkboxes
cbVarMusic = tk.IntVar()
musicCb = tk.Checkbutton(
    win, text="Music", variable=cbVarMusic, command=updateStatus)
musicCb.grid(column=0, row=1, sticky=tk.W)

cbVarGames = tk.IntVar()
gamesCb = tk.Checkbutton(win, text="Video Games",
                         variable=cbVarGames, command=updateStatus)
gamesCb.grid(column=0, row=2, sticky=tk.W)

cbVarSports = tk.IntVar()
sportsCb = tk.Checkbutton(
    win, text="Sports", variable=cbVarSports, state='disabled', command=updateStatus)
sportsCb.grid(column=0, row=3, sticky=tk.W)


# status label
status = tk.StringVar()
statusLabel = ttk.Label(win, text="Your selection: ", textvariable=status)
statusLabel.grid(column=1, row=5, sticky=tk.S)

win.mainloop()
