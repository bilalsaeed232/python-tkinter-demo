import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox


win = tk.Tk()
win.title("Messagebox example")


def _exitApp():
    win.quit()
    win.destroy()


def _showNewInfo():
    mBox.showinfo('Info message box', 'You selected new document menu option')


def _showHelpWarning():
    mBox.showwarning('warning messagebox',
                     'you have selected help menu option')


def _showConfigError():
    mBox.showerror('error messagebox',
                   'you have selected configuration menu option')


def _confirmMessageBox():
    result = mBox.askyesno('Confirm Message box',
                           'Do you really want to save this document?')
    print('You have selected yes? "{0}"'.format(result))


menuBar = Menu(win)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=_showNewInfo)
fileMenu.add_command(label="Save", command=_confirmMessageBox)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_exitApp)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Config", command=_showConfigError)


menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Edit", menu=editMenu)


win.config(menu=menuBar)

win.geometry('250x250')
win.mainloop()
