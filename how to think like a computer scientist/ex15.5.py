import turtle
import random

count = 0
count2 = 0
count3 = 0

def branchType(branchLen,t):
    if branchLen <= 90:
        t.pensize(5)
        t.color("brown")
    if branchLen <= 70:
        t.pensize(4)
        t.color("brown")
    if branchLen <= 50:
        t.pensize(3)
        t.color("brown")
    if branchLen <= 35:
        t.pensize(2)
        t.color("brown")
    if branchLen <= 20:
        t.pensize(1)
        t.color("brown")

def tree(branchLen,t):
    global count
    global count2
    global count3
    count += 1
    if branchLen < 3:
        t.color("green")
        t.stamp()
    else:
        count2 += 1
        branchType(branchLen,t)
        t.forward(branchLen)
        angle = random.randint(15, 45)
        t.right(angle)
        tree(branchLen-random.randint(10, 20),t)
        t.left(2*angle)
        tree(branchLen-random.randint(5, 15),t)
        t.right(angle)
        branchType(branchLen,t)
        t.backward(branchLen)
        count3 += 1

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.pensize(6)
    t.shape("triangle")
    t.shapesize(0.5,0.5,0.5)
    t.color("brown")
    t.speed(0)
    tree(100,t)
    print "Program recursed (%d, %d, %d) times" %(count, count2, count3)
    myWin.exitonclick()

main()
