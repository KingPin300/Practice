from tkinter import *
import time


root = Tk()
root.title("Code...")
root.iconbitmap('images/home.ico')
root.geometry("600x400")

def clock():
	hour = time.strftime("%I")
	minute = time.strftime("%M")
	second = time.strftime("%S")
	am_pm = time.strftime("%p")
	day = time.strftime("%A")
	timezone = time.strftime("%Z")

	myLabel.config(text=hour+":"+minute+":"+second+" "+am_pm)
	myLabel.after(1000,clock)

	myLabel2.config(text=day+" "+timezone)


myLabel = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
myLabel.pack(pady=20)

myLabel2 = Label(root, text="", font=("Helvetica", 14))
myLabel2.pack(pady=10)
clock()

root.mainloop()