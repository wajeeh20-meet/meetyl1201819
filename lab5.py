
# import Tkinter as Tk
# import tkSimpleDialog  as simpledialog
# #Then when ever you want to ask the user for input use this code
# greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=Tk.Tk().withdraw())
# if greeting in ["Arrr!"]:
# 	print("Go away, pirate.")
# else:
# 	print("Greetings, hater of pirates!")

#########################################################################################################################################################################################################

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# import Tkinter as Tk
# import tkSimpleDialog as simpledialog

# year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=Tk.Tk().withdraw()))
# if year <= 1900:
#     print('Woah, thats the past!')
# if year > 1900 & year < 2020:
#     print ("That's totally the present!")
# else:
#     print ("Far out, that's the future!!")

#########################################################################################################################################################################################################
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

# class Person(object):
#   def __init__(self, first_name, last_name):
    
#   	self.first_name= first_name
#   	self.last_name = last_name
#   def speak(self):
#   	print("My name is "+  self.first_name + " " + self.last_name)

# me = Person("Brandon", "Walsh")
# you = Person("Ethan", "Reed")

# me.speak()
# you.speak()
#########################################################################################################################################################################################################
# import Tkinter as Tk
# import tkSimpleDialog  as simpledialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

# 

#########################################################################################################################################################################################################

# class Person():
#    def __init__(self, name, favorite_food,age):
#        self.name = name
#        self.fav_food = favorite_food
#        self.age = age


#    def define_color(self, color):
#        self.color = color

#    def print_info(self):
#        print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
#        print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


# a = Person("Britney", "Pizza", 16)
# a.define_color("Black")
# a.print_info()

# b = Person("Jake", "burgers", 15)
# b.define_color("Red")
# b.print_info()

#########################################################################################################################################################################################################

# class Bear():
# 	def __init__(self, name):
# 		self.name = name
# 		print("A new bear created. Its name is:" + name)
	
# 	def say_hi(self):
# 		print("Hi! I'm a bear. My name is : " + self.name)
# my_bear = Bear("Danny")
# print(my_bear.say_hi())

#########################################################################################################################################################################################################
# balloons = "5"
# name = "Ron"
# color = "Yellow"
# print("This is a tale about " + balloons + " balloons. The first kid is " + name + " who got a " + color + " balloon")

#########################################################################################################################################################################################################

class Cake():
	def __init__(self,cake_flavor):
		self.cake_flavor = flavor

	def eat(self):
		print("Yummy!!! Eating a" + self.cake_flavor + "cake")

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)

