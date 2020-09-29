#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import turtle
stamps = int(input("Please enter the number of turtle stamps: "))

tess = turtle.Turtle()
tess.shape('turtle')
tess.penup()               
steps = 20

for i in range(stamps):
    tess.stamp()              
    steps = steps + 2
    tess.forward(steps)
    tess.right(24)          
