from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning to Code")
root.iconbitmap('images/home.ico')

myImage1 = ImageTk.PhotoImage(Image.open("images/house.jpg"))
myImage2 = ImageTk.PhotoImage(Image.open("images/house2.jpg"))
myImage3 = ImageTk.PhotoImage(Image.open("images/house3.jpg"))
myImage4 = ImageTk.PhotoImage(Image.open("images/house4.jpg"))

imageList = [myImage1,myImage2,myImage3,myImage4]

status = Label(root, text=f"1 of {len(imageList)}", bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myImage1)
myLabel.grid(row=0,column=0,columnspan=3)

def forward(place):
	global myLabel
	global buttonForward
	global buttonBack
	global status

	myLabel.grid_forget()
	myLabel = Label(image=imageList[place])

	
	buttonBack = Button(root, text="<<", command=lambda: back(place-1), bg="black",fg="white")
	
	if (place == len(imageList)-1):
		buttonForward = Button(root, text=">>", state=DISABLED, bg="black",fg="white")
	else:
		buttonForward = Button(root, text=">>", command=lambda: forward(place+1), bg="black",fg="white")

	status = Label(root, text=f"{place + 1} of {len(imageList)}", bd=1, relief=SUNKEN, anchor=E)

	myLabel.grid(row=0,column=0,columnspan=3)
	buttonBack.grid(row=1,column=0)
	buttonForward.grid(row=1,column=2)
	status.grid(row=2, column=0,columnspan=3, sticky=W+E)

def back(place):
	global myLabel
	global buttonForward
	global buttonBack
	global status

	myLabel.grid_forget()
	myLabel = Label(image=imageList[place])
	
	buttonForward = Button(root, text=">>", command=lambda: forward(place+1), bg="black",fg="white")
	if (place == 0):
		buttonBack = Button(root, text="<<", state=DISABLED, bg="black",fg="white")
	else:
		buttonBack = Button(root, text="<<", command=lambda: back(place-1), bg="black",fg="white")

	status = Label(root, text=f"{place + 1} of {len(imageList)}", bd=1, relief=SUNKEN, anchor=E)

	myLabel.grid(row=0,column=0,columnspan=3)
	buttonBack.grid(row=1,column=0)
	buttonForward.grid(row=1,column=2)
	status.grid(row=2, column=0,columnspan=3, sticky=W+E)

buttonBack = Button(root, text="<<", state=DISABLED, bg="black",fg="white")
buttonExit = Button(root, text="X", command=root.quit, bg="black",fg="red")
buttonForward = Button(root, text=">>", command=lambda: forward(1), bg="black",fg="white")

buttonBack.grid(row=1,column=0)
buttonExit.grid(row=1,column=1)
buttonForward.grid(row=1,column=2, pady=10)
status.grid(row=2, column=0,columnspan=3, sticky=W+E)
root.mainloop()