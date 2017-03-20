# create a triangular spiral thet becomes increasingly red
#name
import turtle 
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(110)
from myFunctionfile import*
turtle.bgcolor('yellow')

for times in range(255):
    cool(bob)
    bob.forward(50)
    bob.left(49)
    bob.fillcolor('black')
    bob.begin_fill()
    bob.circle(50)
    bob.end_fill()
