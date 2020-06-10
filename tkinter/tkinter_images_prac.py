from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning to Code")
root.iconbitmap('images/home.ico')

myImage = ImageTk.PhotoImage(Image.open("images/house.jpg"))

myLabel = Label(image=myImage)
myLabel.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()