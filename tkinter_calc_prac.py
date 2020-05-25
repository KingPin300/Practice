from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def bNumber(num):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(num))

def bClear():
	e.delete(0, END)
	firstNum = 0

def bAdd():
	holder = e.get()
	if (holder == ""):
		return
	firstNum = float(holder)
	global value
	global math
	math = "+"
	value = firstNum
	e.delete(0,END)

def bEqual():
	holder = e.get()
	if (holder == ""):
		return
	nextNumber = float(holder)
	e.delete(0,END)
	if (math == "+"):
		e.insert(0, str(value + nextNumber))
	elif (math == "*"):
		e.insert(0, str(value * nextNumber))
	elif (math == "-"):
		e.insert(0, str(value - nextNumber))
	elif (math == "/"):
		if (nextNumber == 0):
			print("CAN'T DIVIDE BY 0!!")
			return
		e.insert(0, str(value / nextNumber))

def bSub():
	holder = e.get()
	if (holder == ""):
		return
	firstNum = Float(holder)
	global value
	global math
	math = "-"
	value = firstNum
	e.delete(0,END)

def bDiv():
	holder = e.get()
	if (holder == ""):
		return
	firstNum = float(holder)
	global value
	global math
	math = "/"
	value = firstNum
	e.delete(0,END)

def bMul():
	holder = e.get()
	if (holder == ""):
		return
	firstNum = float(holder)
	global value
	global math
	math = "*"
	value = firstNum
	e.delete(0,END)

# creating the buttons.
button1 = Button(root, text="1", padx=40,pady=20, command=lambda: bNumber(1))
button2 = Button(root, text="2", padx=40,pady=20, command=lambda: bNumber(2))
button3 = Button(root, text="3", padx=40,pady=20, command=lambda: bNumber(3))
button4 = Button(root, text="4", padx=40,pady=20, command=lambda: bNumber(4))
button5 = Button(root, text="5", padx=40,pady=20, command=lambda: bNumber(5))
button6 = Button(root, text="6", padx=40,pady=20, command=lambda: bNumber(6))
button7 = Button(root, text="7", padx=40,pady=20, command=lambda: bNumber(7))
button8 = Button(root, text="8", padx=40,pady=20, command=lambda: bNumber(8))
button9 = Button(root, text="9", padx=40,pady=20, command=lambda: bNumber(9))
button0 = Button(root, text="0", padx=40,pady=20, command=lambda: bNumber(0))
buttonP = Button(root, text=".", padx=41,pady=20, command=lambda: bNumber("."))

buttonAdd = Button(root, text="+", padx=39,pady=20, command=lambda: bAdd())
buttonEqual = Button(root, text="=", padx=88,pady=20, command=lambda: bEqual())
buttonClear = Button(root, text="Clear", padx=30,pady=20, command=lambda: bClear())
buttonSub = Button(root, text="-", padx=40,pady=20, command=lambda: bSub())
buttonMul = Button(root, text="*", padx=40,pady=20, command=lambda: bMul())
buttonDiv = Button(root, text="/", padx=40,pady=20, command=lambda: bDiv())

# put buttons on the screen.
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonP.grid(row=4,column=1)
buttonAdd.grid(row=5,column=0)
buttonEqual.grid(row=5,column=1, columnspan=2)
buttonClear.grid(row=4,column=2)

buttonSub.grid(row=6,column=0)
buttonMul.grid(row=6,column=1)
buttonDiv.grid(row=6,column=2)

# Making the root the main loop.
root.mainloop()