from tkinter import *

root = Tk()

e = Entry(root, width=30, bg="green", fg="white", borderwidth=5)
e.pack()
e.insert(0,"\t")
def myClick():
	myLabel = Label(root, text=e.get(), fg="green")
	myLabel.pack()


myButton2 = Button(root,text="Enter!", padx=10, pady=10, command=myClick, fg="blue")

myButton2.pack()


# Making the root the main loop.
root.mainloop()