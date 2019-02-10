import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # creates instance tess with attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()      # create alex

tess.forward(80)            # let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)             # turn tess around
tess.forward(80)            # move her away from origin

alex.forward(50)            # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
