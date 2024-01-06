from genericpath import getsize
from turtle import *
s = getscreen()
color=['blue','black']
pencolor('red')
pensize('15')
for i in range (6,0,-1):
    penup() #this is o move penup from screen
    setpos(0,-20*i) # move to a position on y-axis
    pendown()
    fillcolor(color[i%2])
    begin_fill()
    circle(20*i) # creating circle with diff. radius because i changes in every turn of loop
    end_fill()
mainloop()