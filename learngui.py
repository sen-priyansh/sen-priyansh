from tkinter import *

if __name__ == '__main__':
    root=Tk()
    root.title('learngui')

    root.wm_iconbitmap("logo.png")

    root.geometry('644x744')

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    menubar= Menu(root)
    filemenu= Menu(menubar, tearoff=0)

    filemenu.add_command(label= 'new' , command=newfile)

    #To Open already existing file
    filemenu.add_command(label="Open", command = openFile)

    # To save the current file

    filemenu.add_command(label = "Save", command = saveFile)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = quitApp)
    menubar.add_cascade(label = "File", menu=FileMenu)

    # Edit Menu Starts
    EditMenu = Menu(menubar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    menubar.add_cascade(label="Edit", menu = EditMenu)

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    
    

    root.mainloop()