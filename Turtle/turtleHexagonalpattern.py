from turtle import *
s= getscreen()
bgcolor('black')
colors =['green','red','pink','blue','orange','yellow']
for i in range(160):
    pencolor(colors[i%6])
    width(i/100 +1)
    fd(i)
    lt(59)
mainloop()