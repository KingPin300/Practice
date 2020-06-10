from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')
root.geometry("400x400")

option = ["Monday",
		 "Tuesday",
		 "Wednesday",
		 "Thursday",
		 "Friday",
		 "Saturday",
		 "Sunday"]

def show(var):
	Label(root, text=var.get()).pack()

var = StringVar()
var.set(option[0])

drop = OptionMenu(root, var, *option)
drop.pack()

Button(root, text="show selection", command=lambda: show(var)).pack()

root.mainloop()