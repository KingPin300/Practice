from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')

def openWindow():
	global img
	top = Toplevel()
	top.title("Coding...")
	top.iconbitmap('images/home.ico')
	img = ImageTk.PhotoImage(Image.open("images/house.jpg"))
	Label(top, image=img).pack()
	Button(top, text="close window", command=top.destroy).pack()

Button(root, text="open second window", command=openWindow, padx=20,pady=20).pack()



root.mainloop()