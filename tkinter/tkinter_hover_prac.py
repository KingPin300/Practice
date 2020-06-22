from tkinter import *

root = Tk()
root.title("Code...")
root.iconbitmap('../images/home.ico')
root.geometry("600x400")

def buttonHover(event):
	myButton["bg"] = "white"
	myLabel.config(text="I'm hovering over the button.")

def buttonLeave(event):
	myButton["bg"] = "SystemButtonFace"
	myLabel.config(text="")

myButton = Button(root, text="click me", font=("Helvetica", 28))
myButton.pack(pady=50)

myLabel = Label(root, text="", bd=1, relief=SUNKEN, anchor=E)
myLabel.pack(fill=X, side=BOTTOM, ipady=2)

myButton.bind("<Enter>", buttonHover)
myButton.bind("<Leave>", buttonLeave)

root.mainloop()