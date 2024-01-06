from turtle import *
s= getscreen()

fillcolor('blue') # this function is used to fill color in a shapes
begin_fill()  # this function shows the beginning of filling a color
for i in range(5):
    fd(100)
    lt(360//5)
end_fill() # this function shows the ending of- filling color 
fillcolor('yellow')
begin_fill()
circle(50) 
end_fill()
mainloop()