from tkinter import messagebox as mBox
from tkinter import Tk

root = Tk()
root.withdraw()

mBox.showinfo('info message', 'some dummy text for info message...')
mBox.showwarning('warning message', 'some text for warning...')
mBox.showerror('error message', 'some text for error message..')
