from tkinter import *

root = Tk()

# Creating a label.
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Damion.")
myLabel3 = Label(root, text="Nice to meet you!")

# Putting it on the screen.
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=1,column=1)

# Making the root the main loop.
root.mainloop()