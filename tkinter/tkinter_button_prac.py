from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Button was clicked!")
	myLabel.pack()


myButton1 = Button(root,text="Don't Click Me!", state=DISABLED, padx=10, pady=10, bg="red")
myButton2 = Button(root,text="Click Me!", padx=10, pady=10, command=myClick, fg="blue")

myButton1.pack()
myButton2.pack()


# Making the root the main loop.
root.mainloop()