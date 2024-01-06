# Concentric square shape means the shape like good night coil 

from turtle import *
s= getscreen()
speed('slow') # this function is to slow down the speed of output
pensize(2)
pencolor('red')
for i in range(0,52): 
    fd(i*2)
    lt(90)
mainloop()

# printing concentric square in 3 quadrant

"""from turtle import *
s= getscreen()
pensize(3)
penup()
goto(-200,-120)
pendown()
for i in range(0,52):
    fd(i*3+5)
    lt(90)
mainloop()
"""