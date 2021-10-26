import manufacturer
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# Method when button 'Add Manufacturer' clicked
def clickedAdd():
    label = Label() # placeholder

# Method when button 'Delete Manufacturer' clicked
def clickedEdit():
    label = Label() # placeholder

# Method when button 'Display Manufacturer' clicked
def clickedDisplay():
    label = Label() # placeholder

# Method when button 'Submit' clicked
def clickedSubmit():
    ManufacturerID = int(entryManufacturerID.get())

    manufacturer.remove_manufacturer(ManufacturerID)

# Method when button 'Back' clicked
def clickedBack():
    label = Label() # placeholder (Not to implement in this Sprint)

# Create window
window = Tk()
window.attributes('-fullscreen', True)
screen_width = window.winfo_screenwidth()        
screen_height = window.winfo_screenheight()

# Color code
blue = "#344955"
white = "#ffffff"
orange = "#fb8000"

# The left navigation panel
# Frame
leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
leftFrame.grid(column=0, row=0, rowspan=10)
leftFrame.grid_propagate(0)

# Label
moduleName = Label(leftFrame, text="Manufacturer\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
moduleName.place(x=120, y=80, anchor="center")

# Show as line
lineLabel = Label(leftFrame, bg=orange)
lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)

# Button
btnAdd = Button(leftFrame, text="Add\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
btnEdit = Button(leftFrame, text="Delete\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
btnDisplay = Button(leftFrame, text="Display\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

# Title of the page
titlePadX = (( screen_width-240-252 )/2)
labelTitle = Label(window, text="Delete Manufacturer", font=('Arial', 30, BOLD), fg=blue)
labelTitle.grid(column=1, row=0, columnspan=5, padx=titlePadX)

# Back button
btnBack = Button(window, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white)
btnBack.grid(column=1, row=0, ipadx=10, ipady=2)

# Main function 
# Frame
inputFrame = Frame(window, width=1000)
inputFrame.grid(column=1, row=2, columnspan=5, rowspan=7, sticky="ns")

# Label
labelManufacturerID = Label(inputFrame, text="ID :", font=('Arial', 24), fg=blue)
labelManufacturerID.place(x=300, y=30, anchor="e")

# Entry
entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerID.place(x=310, y=30, anchor="w", width=470, height=50)

# Submit button
btnSubmit = Button(window, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white)
btnSubmit.grid(column=1, row=8, columnspan=5, ipadx=35, ipady=5)
  
window.mainloop()