import turtle

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'     # Rule 1
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

def drawLsystem(aTurtle,instructions,angle,distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLsystem(4,"F")     # create the string
    print(inst)
    t = turtle.Turtle()             # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 60, 5)     # draw the picturre
                                    # angle 60, segment length 5

    wn.exitonclick()

main()
