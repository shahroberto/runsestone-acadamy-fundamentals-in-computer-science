import turtle

def drawSquare(t,sz):          # draw a square
    """Make turtle t draw a square of size sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
 
def drawTriangle(t,sz):         # draw a tirangle
    """Make turtle t draw a trianlge of size sz."""
    for i in range(3):
        t.forward(sz)
        t.left(120)

def drawOctogon(t,sz):          # draw an octogon
    """Make turtle t draw an octogon of size sz."""
    for i in range(8):
        t.forward(sz)
        t.left(45)

def drawPoylgon(t,sz,n):         # draw a polygon
    """Make turtle t draw a polygon of size sz with n vertices."""
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
numVertices = int(raw_input("enter the number of vertices \n>"))
#drawSquare(tess,50)
#drawTriangle(tess,75)
#drawOctogon(tess,100)
drawPoylgon(tess,2,numVertices)
wn.exitonclick()
