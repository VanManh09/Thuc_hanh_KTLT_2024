print("sinh viên Nguyễn Văn Mạnh")
print("MSSV 235752021610091")

from tkinter import *

def NewFile():
    print("New File!")
def OpenFile():
    print("Open File selected!")
def ExitFile():
    print("Exit File!")
def TextFile():
    print("Text File Selected!")
def PictureFile():
    print("Picture File Selected!")
def About():
    print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu= Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitFile)

insertmenu= Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=TextFile)
insertmenu.add_command(label="Picture", command=PictureFile)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
