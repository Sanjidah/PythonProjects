#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(20)
  a = random.randrange(0,360,5)
  trey.right(a)
