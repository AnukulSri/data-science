# here we are creating circle at the edges or sides of pentagon 
from turtle import *
t= Turtle()
s= getscreen()
for i in range (5):
    t.fd(100)
    t.lt(360//5)
    t.circle(20) # it means to create circle with the size of 20

mainloop() # this function is used to hold output screen

# to create dot in place of circle...

"""
from turtle import *
t= Turtle() # this means we are referring turtle to t
s= getscreen()
for i in range (5):
    t.fd(100)
    t.lt(360//5)
    t.dot(20)
mainloop()
"""