import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 60, 2)))
tess.up()                       # lifts the pen for tess
for size in range(5, 60, 2):
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)
    tess.right(24)

wn.exitonclick()
