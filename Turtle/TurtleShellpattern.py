from turtle import *
s= getscreen()
pencolor('black')
pensize(3)
fillcolor('pink')
for i in range (10,1,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()  