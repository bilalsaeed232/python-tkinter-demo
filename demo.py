import tkinter as tk
from tkinter import ttk, scrolledtext, Menu


def clickMe():
    print('You clicked the button')


win = tk.Tk()
win.title('Python GUI')

# create a LabelFrame to contain all the widgets
mainFrame = ttk.Labelframe(win, text="Monty Python")
mainFrame.grid(column=0, row=0, columnspan=4, sticky=(tk.W))


labelName = ttk.Label(mainFrame, text="Enter a name:")
labelName.grid(column=0, row=0, sticky=tk.W)
nameVar = tk.StringVar()
nameText = ttk.Entry(mainFrame, width=12, textvariable=nameVar)
nameText.grid(column=0, row=1, sticky=tk.W)


labelNumber = ttk.Label(mainFrame, text="Choose a number:")
labelNumber.grid(column=1, row=0, sticky=tk.W, columnspan=3)
numberVar = tk.StringVar()
numberCombo = ttk.Combobox(mainFrame, width=12, textvariable=numberVar)
numberCombo.grid(column=1, row=1)
numberCombo['values'] = list(t for t in range(1, 100))
numberCombo.current(0)
clickBtn = ttk.Button(mainFrame, text="Click ME!", command=clickMe)
clickBtn.grid(column=2, row=1)


# checkboxes
disabledVar = tk.IntVar()
disabledCB = ttk.Checkbutton(
    mainFrame, text="Disabled", variable=disabledVar, state="disabled")
disabledCB.grid(column=0, row=2, sticky=tk.W)

uncheckedVar = tk.IntVar()
uncheckedCB = ttk.Checkbutton(
    mainFrame, text="Unchecked", variable=uncheckedVar)
uncheckedCB.grid(column=1, row=2)

toggleVar = tk.IntVar()
toggleCb = ttk.Checkbutton(mainFrame, text="Toggle", variable=toggleVar)
toggleCb.grid(column=2, row=2)


# Scrolledtext
scrollText = scrolledtext.ScrolledText(
    mainFrame, width=30, height=3, wrap=tk.WORD)
scrollText.grid(column=0, row=3, sticky="WE", columnspan=3)


# radio buttons
colorRadioVar = tk.IntVar()

blueRb = ttk.Radiobutton(mainFrame, text="Blue",
                         variable=colorRadioVar, value=1)
blueRb.grid(column=0, row=4, sticky=tk.W)
goldRb = ttk.Radiobutton(mainFrame, text="Gold",
                         variable=colorRadioVar, value=2)
goldRb.grid(column=1, row=4)
redRb = ttk.Radiobutton(mainFrame, text="Red", variable=colorRadioVar, value=3)
redRb.grid(column=2, row=4)


# inner labelframe
labelFrame = ttk.Labelframe(mainFrame, text="Labels in a frame")
labelFrame.grid(column=0, row=5, padx=10, pady=30)

label1 = ttk.Label(labelFrame, text="label1")
label1.grid(column=0, row=0)
label2 = ttk.Label(labelFrame, text="label2")
label2.grid(column=0, row=1)
label3 = ttk.Label(labelFrame, text="label3")
label3.grid(column=0, row=2)


# TODO: create menu bar with menu items
def _quite():
    win.quit()
    win.destroy()
    # exit()


menuBar = Menu(win)

# file menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quite)
menuBar.add_cascade(label="File", menu=fileMenu)

# help menu items
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# add the menubar to our main window
win.config(menu=menuBar)

# change the size of our window
win.geometry('350x300')

# actually run the window
win.mainloop()
