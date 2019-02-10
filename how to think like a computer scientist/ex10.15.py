import turtle

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'F[-X]+X'     # Rule 1
    elif ch == 'F':
        newstr = 'FF'
    else:
        newstr = ch    # no rules apply so keep the character
    return newstr

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def createLsystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            # print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def main():
    inst = createLsystem(8,"X")     # create the string
    # print(inst)
    t = turtle.Turtle()             # create the turtle
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    t.color("blue")
    t.pensize(1)
    t.setposition(0, -200)
    t.left(90)
    t.speed(9)
    drawLsystem(t, inst, 30, 2)     # draw the picturre
                                    # angle 60, segment length 5
    wn.exitonclick()

main()
