#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import turtle
tess = turtle.Turtle()

turns = int(input("Enter number of turns: "))
for i in range(0,turns,2):
    print (i)
    tess.forward(i)
    tess.right(45)
