import turtle
import random

colors = ["red","blue","green","purple","yellow","orange","black"]

tim = turtle.Turtle()


tim.speed(0)
tim.width(5)

def up():
	tim.setheading(90)
	tim.forward(10)

def down():
	tim.setheading(270)
	tim.forward(10)

def left():
	tim.setheading(180)
	tim.forward(10)

def right():
	tim.setheading(0)
	tim.forward(10)

def color():
	tim.color(random.choice(colors))
turtle.listen()


turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.onkey(color, "space")


turtle.mainloop()