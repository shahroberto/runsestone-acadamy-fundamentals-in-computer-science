import turtle

def drawSquare(t,sz):
    """Make turtle t draw a square with size sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()      # create alex
drawSquare(alex,50)         # call fxn to draw square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)

wn.exitonclick()
