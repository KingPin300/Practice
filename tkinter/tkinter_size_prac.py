from tkinter import *

root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')
root.geometry("600x400")

def resize():
	w = widthEntry.get()
	h = heightEntry.get()
	root.geometry(f"{w}x{h}")


widthLabel = Label(root, text="Width:")
widthLabel.pack(pady=10)
widthEntry = Entry(root)
widthEntry.pack(pady=5)

heightLabel = Label(root, text="Height:")
heightLabel.pack(pady=10)
heightEntry = Entry(root)
heightEntry.pack(pady=5)

myButton = Button(root, text="resize", command=resize)
myButton.pack(pady=20)

root.mainloop()