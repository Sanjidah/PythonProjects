#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import turtle            # set up tess
wn = turtle.Screen()
tess = turtle.Turtle()

for i in range(150):        # repeat 150 times
    tess.forward(0.5*i)     # move forward
    tess.penup()            # lift pen up
    tess.forward(0.5*i)     # move forward
    tess.pendown()          # put pen down
    tess.left(110)          # turn left 110 degrees


wn.exitonclick()

