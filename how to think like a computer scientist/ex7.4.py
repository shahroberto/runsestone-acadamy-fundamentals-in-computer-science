import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.tracer(1000) # speed up process for lots of darts

fred.up()

numdarts = 10000
insideCount = 0.0  # number of dots in a circle
for i in range(numdarts):
    randx = random.random()
    randy = random.random()
    x = (-2)*randx+1
    y = (-2)*randy+1
    fred.setx(x)
    fred.sety(y)
    circleDist = fred.distance(0,0)
    if circleDist <= 1:
        fred.dot("red")
        insideCount += 1
    else:
        fred.dot("blue")

# approximate pi
piApprox = 4.0*(insideCount/numdarts)
print("pi is approximated as %f") % (piApprox)

wn.exitonclick()
