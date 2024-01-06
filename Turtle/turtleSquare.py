"""from turtle import *

#speed(0)
forward (100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
mainloop()
"""
# lt is decided by breaking 360 degree into equal side. 
from turtle import *
t= Turtle()
s= getscreen()
for i in range(4):
    t.fd(100)
    t.lt(90)
mainloop()