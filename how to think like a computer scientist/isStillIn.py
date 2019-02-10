def isInScreen(wn, t):           # determine if the turtle is in the screen
    leftBound = -(wn.window_width()/2)
    rightBound = wn.window_width()/2
    topBound = wn.window_height()/2
    bottomBound = -(wn.window_height()/2)

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn
