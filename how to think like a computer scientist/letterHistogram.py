from countingLetters import countAll
import turtle

def drawBar(t, height, letter):
    """Get Turtle t to draw one bar, of height."""
    t.pendown()
    t.begin_fill()              # start filling this shape
    t.left(90)
    t.forward(height)

    t.penup()
    if height < 0:
        t.fd(-20)
    t.write('  ' + str(letter) + "=" + str(height), font=("Arial", 16, "normal"))
    if height < 0:
        t.fd(20)
    t.pendown()

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                # stop filling this shape

countedLetters = countAll(raw_input('please input a phrase to count:\n>'))
countedList = countedLetters.items()
countedList.sort(key=lambda x: x[0])

maxheight = max(item[1] for item in countedList)
print(maxheight)
numbars = len(countedList)
print(numbars)
border = 10

wn = turtle.Screen()            # Set up window and its attributes
wn.title("Counting Letters")
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()          # create Tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)

for char in countedList:
    drawBar(tess, char[1], char[0])

wn.exitonclick()
