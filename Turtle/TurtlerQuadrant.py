# creating square in all 4 quadrant..

from turtle import *
s = getscreen()
pensize(4)
color=['blue','red','green','black']

pencolor(color[0]) # 1 quadrant (+x,+y)
penup()
goto(200,150)
pendown()
for i in range(4):
    fd(50)
    lt(360//4)

pencolor(color[1]) # 2 quadrant (-x,+y)
penup()
goto(-200,150)
pendown()
for i in range(4):
    fd(50)
    lt(360//4)

pencolor(color[2]) # 3quadrant (-x,-y)
penup()
goto(-200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(360//4)

pencolor(color[3]) # 4 quadrant (+x,-y)
penup()
goto(200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(360//4)

mainloop()