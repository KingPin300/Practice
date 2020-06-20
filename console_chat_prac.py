import threading
from tkinter import *
import time

root = Tk()
root.title("CHAT ROOM")
root.iconbitmap('images/home.ico')
root.geometry("600x450")

text = Text(root, exportselection = 1)
text.pack()

def readChat():
	msg = textEntry.get()
	textEntry.delete(0, len(msg))
	sendChat(msg)

def sendChat(msg):
	if msg:
		text.insert(INSERT, f"{msg}\n")

textEntry = Entry(root)
enterButton = Button(root, text = "Enter", command = readChat)
textEntry.pack()
enterButton.pack()

root.mainloop()