import turtle
def drawRectangle(t,w,h):       # general function to draw rectangle
    """Get turtle t to draw a recatngle of width w and height h"""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawSquare(tx,sz):          # draw a square
    drawRectangle(tx,sz,sz)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
drawSquare(tess,50)
wn.exitonclick()
