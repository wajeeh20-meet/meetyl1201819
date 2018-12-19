from turtle import *
import turtle
import math
import random
turtle.tracer(0)
class Ball(Turtle):
	def __init__(self, radius, color, speed,dx,dy,x,y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.penup()
		self.speed(0)
		self.dx = dx/10
		self.dy = dy/10
		self.goto(x,y)
		self.speed(speed)
	def move(self):
		oy = self.ycor()
		ox = self.xcor()
		ny = oy + self.dy
		nx = ox + self.dx
		self.goto(nx,ny)
		if(nx>400 or nx <-400):
			self.dx = self.dx*-1
		if(ny>400 or ny <-400):
			self.dy = self.dy*-1

ball1 = Ball(70,"red",50,9,9,100,100)
ball2 = Ball(70,"blue",50,9,9,-100,-100)






def check_collision(ball1, ball2):
	

	radius_len = ball1.radius + ball2.radius

	D = math.sqrt((ball1.xcor()-ball2.xcor())**2 + (ball1.ycor() - ball2.ycor())**2)
	if (radius_len >D):
		return True
	return False
while True:
	if(check_collision(ball1,ball2)):

		tempx = ball1.dx
		tempy = ball1.dx
		ball1.dx = ball2.dx
		ball1.dy = ball2.dy
		ball1.dx = tempx
		ball1.dy = tempy
	ball1.move()
	turtle.update()
	ball2.move()
	turtle.update()

turtle.mainloop()




