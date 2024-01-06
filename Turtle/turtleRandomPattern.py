# Creating Random flower pattern

import random # import random library
from turtle import *
s= Screen()
colors=['orange','pink']
for i in range (50):
    x= random.randint(-200,200) # it means to pick a random value b/w -200 to 200 for x
    y= random.randint(-200,200) # it means to pick a random value b/w -200 to 200 for y
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(1,2)) # this is to select random value for pensize
    pencolor(colors[random.randint(0,1)]) # this is to select random color from initialize list
    radius= random.randint(5,20)
    fillcolor('red')
    begin_fill()
    for i in range(6): # creating 6 sided flower
        circle(radius)
        lt(60)
    end_fill()
mainloop()