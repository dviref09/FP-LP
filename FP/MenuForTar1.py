#
#  Example program for Targil 1
#
import math
from myboolfuncs import *
#
# Area calculation program  
def rectangleArea(w, h):
	return w*h
#
def circleArea(r):
	return math.pi * r**2


def triangleArea(base, height):
	return base * height / 2

def squareArea(side):
	return side ** 2

def sphereVolume(radius):
	return (4/3) * math.pi * (radius ** 3)

def squarePyramidVolume(base, height):
	return (1/3) * (base ** 2) * height

def coneVolume(radius, height):
	return (1/3) * math.pi * (radius ** 2) * height
	
#
# printing the menu options
def prtMenu(shapes):
	for i in range(len(shapes)):
		print (i+1, shapes[i])
	return
#
# main program
#
def question2():
	print ("Welcome to the Area / Volume calculation program")
	print ("---------------------------------------\n")  
	# Print out the menu
	shapes = ("Rectangle", "Circle", "Triangle", "Square", "Sphere", "Square Pyramid", "Cone")
	while True:
		print ("\nPlease select a shape (press 0 to quit):")
		prtMenu(shapes) 
		# Get the user's choice: 
		shape = input("> ")
		# Calculate the area: 
		if shape == "1":
			height = getNumber("Please enter the height: ")    
			width  = getNumber("Please enter the width: ")
			area = rectangleArea(width, height)
			print ("The area is", area)
			continue
		elif shape == "2":
			radius = getNumber("Please enter the radius: ")
			area   = circleArea(radius)
			print ("The area is", area)
			continue
		elif shape == "3":
			base = getNumber("Please enter the base: ")
			height = getNumber("Please enter the height: ")
			area = triangleArea(base, height)
			print ("The area is", area)
			continue
		elif shape == "4":
			side = getNumber("Please enter the length of the side: ")
			area = squareArea(side)
			print ("The area is", area)
			continue
		elif shape == "5":
			radius = getNumber("Please enter the radius: ")
			volume = sphereVolume(radius)
			print ("The volume is", volume)
			continue
		elif shape == "6":
			base = getNumber("Please enter the length of the side of the base: ")
			height = getNumber("Please enter the height: ")
			volume = squarePyramidVolume(base, height)
			print ("The volume is", volume)
			continue
		elif shape == "7":
			radius = getNumber("Please enter the radius: ")
			height = getNumber("Please enter the height: ")
			volume = coneVolume(radius, height)
			print ("The volume is", volume)
			continue
		elif shape == "0":
			print ("Bye!")  
			break
		else:     
			print ("Invalid shape")
