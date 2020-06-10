from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning to Code")
root.iconbitmap('images/home.ico')

frame = LabelFrame(root, text="This is my frame.", padx=10, pady=10)
frame.pack(padx=10,pady=10)

b = Button(frame,text="click me")
b.pack()
root.mainloop()