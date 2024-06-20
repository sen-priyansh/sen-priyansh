from tkinter import *
gui= Tk()
#width x hight
gui.geometry('600x600')

text = Label(text='hello this is my gui from python')
text.pack()
photo = PhotoImage(file="diya.PNG")
photo_lable = Label(photo)
photo_lable.pack


gui.mainloop()

