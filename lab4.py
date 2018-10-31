class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_color = favourite_color
	def  eat(self,food):
		print("Yummy!! " + self.name + " is eating "+ food )
	def discription(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favourite_color)
	def make_sound(self):
		for i in range (3):
			print(self.sound)

lion = Animal("roar","wael","5","black")
lion.eat("meat")
lion.discription()
lion.make_sound()

#problem 3: 
class person(object):
	def __init__(self,name,age, city, gender)
	self.name = name
	self.age = age
	self.city = city
	self.gender = gender
	

		