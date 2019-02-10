import turtle               # allows us to access the turtle library
wn = turtle.Screen()        # creates a graphic window
# prompt for user input color
winColor = raw_input("Choose a window color: \n>")
wn.bgcolor(winColor)        # sets the window background color

alex = turtle.Turtle()      # creates a turtle named alex
alexColor = raw_input("Choose a turtle color: \n>")
alex.color(alexColor)       # make alex blue

# convert input to integer value otherwise will be considered as string
alexSize = int(input("Choose a pen size: \n>"))
alex.pensize(alexSize)      # set the width of his pen

alex.forward(150)           # moves forward by 50 units
alex.left(90)               # rotates left by 90 deg
alex.forward(75)
alex.left(90)
alex.forward(300)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(150)

wn.exitonclick()            # wait for a user to click to exit
