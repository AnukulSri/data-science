from turtle import *
t=Turtle()  # this means we are referring turtle to t
t.speed('fastest')
s=getscreen()
for i in range(8):
    t.fd(100)
    t.lt(360//8) # or t.lt = (360//range)means 360//8
mainloop()