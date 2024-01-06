# The screen is divided into four quadrants. The point where the turtle is initially positioned at beginning
# to move turtleto any other area on the screen, use goto() and enter coordinates like:
# goto(100,100)or goto(-10,10)or goto(-10,-10)or goto(10,-10)

from turtle import *
import turtle
turtle.bgcolor('black') # it is used to change the background color of output screen
turtle.pensize(5) # it is used to change the size of pen
turtle.pencolor('red')  # it is used to change the color of pen
s= getscreen()
penup() 
goto(150,100)
pendown()
for i in range(4):
    fd(100)
    lt(90)
mainloop()
 