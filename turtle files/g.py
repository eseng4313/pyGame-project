import turtle
bob = turtle.Turtle()
bob.speed(11)
bob.shape("turtle")


for times in range(300):
   
    
    bob.forward(times)
    bob.right(190)
    bob.forward(40)
    bob.forward(times)
    bob.circle(30)
    bob.color("green")
    bob.pencolor("yellow") 

   
   
   

