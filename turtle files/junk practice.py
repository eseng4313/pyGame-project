import turtle
from myFunctionfile import*
bob=turtle.Turtle()
ed=turtle.Turtle()
trump=turtle.Turtle()
jack=turtle.Turtle()

bob.shape('turtle')
trump.shape('turtle')
jack.shape('turtle')
ed.shape('turtle')

bob.speed(0)
jack.speed(0)
trump.speed(0)
ed.speed(0)

for times in range(255):
    jump(ed,200,200)
    ed.circle(300- times*2)
    ed.forward(30)

    jump(bob,200,-200)
    bob.circle(300- times*2)
    bob.forward(30)
    
    jump(jack,-200,200)
    jack.circle(300- times*2)
    jack.forward(30)

    jump(trump,-200,-200)
    trump.circle(300- times*2)
   


    
   
    



    

