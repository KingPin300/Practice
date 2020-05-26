from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')
root.geometry("400x400")

var = StringVar()

def show():
	myLabel = Label(root, text=var.get()).pack()

c = Checkbutton(root, text="Check the box!", variable=var, command=show, onvalue="on", offvalue="off")
c.deselect()
c.pack()

Button(root, text="press to select", command=show).pack()

myLabel = Label(root, text=var.get()).pack()
root.mainloop()