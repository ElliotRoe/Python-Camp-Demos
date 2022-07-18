from turtle import *


def square():
    j = 0
    while j < 4:
        forward(100)
        left(90)
        j = j + 1


# Square 1
square()
# move to the right
forward(200)
# Square 2
square()
# move to the right
forward(200)
# Square 3
square()

