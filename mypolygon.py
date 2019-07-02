import turtle
import math
bob = turtle.Turtle()
#print(bob)
#for i in range(4):
#    bob.fd(100)
#    bob.lt(90)
#turtle.mainloop()

def square(t, length):
    print(bob)
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.mainloop()
#square(bob, 150)

def polygon(t, length, n):
    print(bob)
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    t.mainloop()
#polygon(bob, 100, 5)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 60
    length = circumference/ n
    polygon(t, length, n)
#circle(bob, 100)

def arc(t, r, angle):
    circumference = 2 * math.pi * r 
    arclength = circumference * (angle/360)
    n = 60
    length = arclength/ n
    turnang = angle/n
    for i in range(n):
        t.fd(length)
        t.lt(turnang)
#arc(bob, 100, 360)


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()