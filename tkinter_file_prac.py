from tkinter import *
from PIL import ImageTk, Image
from tkinter import  filedialog

root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')

def locationImg():
	global myImage
	root.filename = filedialog.askopenfilename(initialdir="C:\code\Practice", title="Select a File", filetypes=(("jpg","*.jpg"),("txt","*.txt")))
	myImage = ImageTk.PhotoImage(Image.open(root.filename))
	labelImg = Label(image=myImage).pack()

Button(root, text="click to add image", command=locationImg).pack()
root.mainloop()