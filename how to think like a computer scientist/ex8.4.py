"""Make a turtle do things."""
import turtle
import random
import time             # timer module
from isStillIn import isInScreen          # import functions from file

start = time.time()
yurtle = turtle.Turtle()
yurtle.pensize(3)
yurtle.shape('turtle')

wn = turtle.Screen()
wn.bgcolor("lightgreen")

while isInScreen(wn, yurtle):
    coin = random.randrange(0, 2)       # random number generator 0 or 1
    if coin == 0:   # heads
        yurtle.left(90)
    else:
        yurtle.right(90)  # tails
    yurtle.forward(25)

end = time.time()
print("ALL DONE!", (end - start), "seconds for Yurtle to finish! YAY!!!")
wn.exitonclick()
