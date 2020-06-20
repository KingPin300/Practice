from tkinter import *

root = Tk()
root.title("Code...")
root.iconbitmap('../images/home.ico')
root.geometry("800x800+-1900+100")

def info():
	dimentioinLabel = Label(root, text=root.winfo_geometry())
	dimentioinLabel.pack(pady=20)


myButton = Button(root, text="Click Me", command=info)
myButton.pack(pady=20)

root.mainloop()