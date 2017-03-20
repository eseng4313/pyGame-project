#Create a polygon function that accepts a turtle, sides, and distance.
#function file

def polygon(t, sides, distance):
    angle = 360/sides#angle variable is inside the function
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.right(angle)
    t.end_fill()

def cool(t,d):
    t.color('black')
    polygon(t,4,d)
    t.color('orange')
    polygon(t,3,d)

def coolSquared(t,d):
    for times in range(4):
        cool(t,d)
        t.right(90)


def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def star(t,d,c):

    t.begin_fill()
    for times in range(8):
        t.color(c)
        t.forward(d)
        t.left(135)

    t.end_fill()



def funky(t,d,c1,c2):
    t.color(c1)
    polygon(t,3,d)
    t.color(c2)
    polygon(t,3,d/2)























    
    












        

        
