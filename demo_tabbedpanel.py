import tkinter as tk
from tkinter import ttk, scrolledtext, Menu


def clickMe():
    print('You clicked the button')


win = tk.Tk()
win.title('Python GUI')
# change the icon of main window
win.iconbitmap('./pyt.ico')


# create tabbed panel control
tabControls = ttk.Notebook(win)

# create a LabelFrame to contain all the widgets
step1Tab = ttk.Labelframe(tabControls, text="Monty Python")
step1Tab.grid(column=0, row=0, sticky=(tk.W))

step2Tab = ttk.Labelframe(tabControls, text="Click on any radiobutton")

labelName = ttk.Label(step1Tab, text="Enter a name:")
labelName.grid(column=0, row=0, sticky=tk.W)
nameVar = tk.StringVar()
nameText = ttk.Entry(step1Tab, width=12, textvariable=nameVar)
nameText.grid(column=0, row=1, sticky=tk.W)


labelNumber = ttk.Label(step1Tab, text="Choose a number:")
labelNumber.grid(column=1, row=0, sticky=tk.W, columnspan=3)
numberVar = tk.StringVar()
numberCombo = ttk.Combobox(step1Tab, width=12, textvariable=numberVar)
numberCombo.grid(column=1, row=1)
numberCombo['values'] = list(t for t in range(1, 100))
numberCombo.current(0)
clickBtn = ttk.Button(step1Tab, text="Click ME!", command=clickMe)
clickBtn.grid(column=2, row=1)


# checkboxes
disabledVar = tk.IntVar()
disabledCB = ttk.Checkbutton(
    step2Tab, text="Disabled", variable=disabledVar, state="disabled")
disabledCB.grid(column=0, row=2, sticky=tk.W)

uncheckedVar = tk.IntVar()
uncheckedCB = ttk.Checkbutton(
    step2Tab, text="Unchecked", variable=uncheckedVar)
uncheckedCB.grid(column=1, row=2)

toggleVar = tk.IntVar()
toggleCb = ttk.Checkbutton(step2Tab, text="Toggle", variable=toggleVar)
toggleCb.grid(column=2, row=2)


# Scrolledtext
scrollText = scrolledtext.ScrolledText(
    step1Tab, width=30, height=3, wrap=tk.WORD)
scrollText.grid(column=0, row=3, sticky="WE", columnspan=3)


# radio buttons
def radioClicked():
    radVal = colorRadioVar.get()
    if radVal == 1:
        step2Tab.configure(text="Blue")
    elif radVal == 2:
        step2Tab.configure(text="Gold")
    else:
        step2Tab.configure(text="Red")


colorRadioVar = tk.IntVar()

blueRb = ttk.Radiobutton(step2Tab, text="Blue",
                         variable=colorRadioVar, value=1, command=radioClicked)
blueRb.grid(column=0, row=4, sticky=tk.W)
goldRb = ttk.Radiobutton(step2Tab, text="Gold",
                         variable=colorRadioVar, value=2, command=radioClicked)
goldRb.grid(column=1, row=4)
redRb = ttk.Radiobutton(step2Tab, text="Red",
                        variable=colorRadioVar, value=3, command=radioClicked)
redRb.grid(column=2, row=4)


# inner labelframe
labelFrame = ttk.Labelframe(step1Tab, text="Labels in a frame")
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


# Add tabs to TabControl
tabControls.add(step1Tab, text="Step 1")
tabControls.add(step2Tab, text="Step 2")
tabControls.pack(expand=1, fill="both")


# change the size of our window
win.geometry('350x300')

# actually run the window
win.mainloop()
