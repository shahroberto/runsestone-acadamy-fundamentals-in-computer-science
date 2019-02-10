import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(4):      # repeat 4 times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()

print(list(range(4)))    # range fxn [0 1 2 3]
print(list(range(1,5)))  # [1 2 3 4]
print(list(range(10,21)))

for i in range(10):
    print i,

for i in range(0,19,2):
    print i,
