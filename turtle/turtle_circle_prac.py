import turtle
import random
import time

colors = ["red","blue","green","purple","yellow","orange","black"]

tim = turtle.Turtle()

tim.color(colors[0],colors[1])

tim.hideturtle()
tim.width(5)
tim.speed(0)

for x in range(5):
	numx = random.randrange(-300,300)
	numy = random.randrange(-300,300)
	tim.penup()
	tim.setpos(numx,numy)
	tim.pendown()
	tim.color(colors[random.randrange(0,len(colors)-1)])
	tim.begin_fill()
	tim.circle(random.randrange(10,80))
	tim.end_fill()

time.sleep(2)