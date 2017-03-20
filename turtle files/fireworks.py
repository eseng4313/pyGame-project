import turtle
from myFunctionfile import*
bob=turtle.Turtle()
bob.speed(11)
turtle.bgcolor('black')
bob.pencolor('sky blue')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)

jump(bob,200,-200)

bob.pencolor('orange')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)


jump(bob,-200,-200)

bob.pencolor('red')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)
    

jump(bob,200,200)

bob.pencolor('green')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)
    
jump(bob,-200,200)


bob.pencolor('yellow')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)

jump(bob,400,0)

bob.pencolor('white')
for times in range(110):
    bob.forward(100)
    bob.right(135)
    bob.forward(times)
    bob.circle(times)



