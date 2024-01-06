from turtle import *
s= getscreen()
pencolor('red')
fillcolor('red')
for i in range(5):
    lt(360//5)
    penup()
    fd(20)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    bk(20) # this is to move turtle back to center
    pendown()
    

mainloop()