import turtle 
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(110)
from myFunctionfile import*
turtle.bgcolor('yellow')

for times in range(8):
    star(bob)
