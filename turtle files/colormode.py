# create a triangular spiral thet becomes increasingly red
#name
import turtle
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(11)

bob.pensize(3)
turtle.bgcolor('black')
#variables
s = 9
d = 200
a = 360/s

#for loop
for n in range(255):#n is the loop variables
    print(n)
    c = (190,n,n)
    bob.color(c)
    bob.forward(d)
    bob.right(169)
    bob.circle(90)
    
for n in range(255):#n is the loop variables
    print(n)
    c = (n,199,n)
    bob.color(c)
    bob.forward(d)
    bob.right(169)
    bob.circle(60)
    
        
        

    
