import sys
from tkinter import *
sys.path.append('/home/saksama/Desktop') \\ add the folder path here.
from Controller import Controller

root = Tk()
Controller = Controller.Controller()

Heading = Label(root, text="Welcome to HeartBeat!!")
Heading.pack(anchor=CENTER)


# DirButton selects and returns the Excel file to extract the information from
getFileButton = Button(root, text="File Selector", command=Controller.getFileName)
getFileButton.pack(anchor=CENTER)

#Dir Chooser will be the folder where all the folders are created.
DirChooserLabel = Label(root, text="Select the folder where you want the new files")
DirChooserLabel.pack(anchor=CENTER)

getDirButton = Button(root, text="Directory Selector", command= lambda: Controller.getDirName())
getDirButton.pack(anchor=CENTER)

# ---------------- col starts ----------------------------------- #
colLabel = Label(root, text="Enter the column number[s] from the excel file.\n  \
Please use comma[s] to seperate the column numbers")
colLabel.pack(anchor=CENTER)

# This entry will contain the number of columns from which info needs to be extracted.
Col = Entry(root)
Col.pack()
# ---------------- col ends ----------------------------------- #

Finish = Button(root, text="Make Folders", command= lambda: Controller.Process(Col.get()))
Finish.pack()

root.geometry('{}x{}'.format(500, 250))
root.mainloop()
