from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("Learning to Code")
root.iconbitmap('images/home.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askyesno("Popup", "Do you like cheese?")
	Label(root, text=response).pack()

Button(root, text="popup", command=popup).pack()

root.mainloop()