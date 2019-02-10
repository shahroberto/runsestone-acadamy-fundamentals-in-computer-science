import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:      # repeat 4 times
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
