from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning to Code")
root.iconbitmap('images/home.ico')

r = IntVar()


Radiobutton(root, text="option 1", variable=r, value=1).pack()
Radiobutton(root, text="option 2", variable=r, value=2).pack()
Radiobutton(root, text="option 3", variable=r, value=3).pack()



root.mainloop()