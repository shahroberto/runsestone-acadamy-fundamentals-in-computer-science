import turtle

def drawMulticolorSquare(t,sz):
    """Make turtle t draw a multicolor square with size sz."""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()        # set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()      # create tess
tess.pensize(3)

size = 20
for i in range(15):
    drawMulticolorSquare(tess,size)
    size = size + 10
    tess.forward(10)
    tess.right(18)

wn.exitonclick()
