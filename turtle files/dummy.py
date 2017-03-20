import turtle
from myFunctionfile import*
bob=turtle.Turtle()
bob.speed(11)
bob.pensize(10)

bob.pencolor('black')
for times in range(999):
    bob.forward(times)
    bob.right(194)
    bob.forward(50)

jump(bob,0,0)

bob.pensize(1)
bob.pencolor('blue')


for times in range(99):
    bob.forward(times)
    bob.right(194)
    bob.forward(50)
