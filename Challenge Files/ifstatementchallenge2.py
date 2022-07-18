import random
from turtle import *
# Write a program that draws a square (or whatever shape you want) if random_number is equal to 1,
#   or a triangle if random_number is equal to 2.
# The code to draw a triangle is already given to you.

# This line of code generates a random number between 1 and 2.
random_number = random.randint(1, 2)


# Code to draw a triangle
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)

