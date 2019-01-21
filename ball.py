from turtle import *
import turtle 
import random
import math
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.shape("circle") 
		self.shapesize(r/10) 
		self.r = r
		self.color(color)
		self.penup()
		self.dx = dx
		self.dy = dy 
		self.goto(x,y)
	def move (self, screen_widht, screen_height):	
		oldx = self.xcor()
		oldy = self.ycor()
		newx  = oldx + self.dx
		newy  = oldy + self.dy
		right_side = newx + self.r
		left_side = newx - self.r
		top_side = newy + self.r
		bottom_side = newy - self.r

		self.goto(newx, newy)
		if right_side > screen_widht or left_side < -screen_widht:
			self.dx *= -1
		if top_side > screen_height or bottom_side < -screen_height:
			self.dy *= -1