from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')
root.geometry("400x400")

def extOpen():
	program = filedialog.askopenfilename()
	os.system('"%s"'%program)

Button(root, text="open program", command=extOpen).pack(padx=15, pady=15)

root.mainloop()