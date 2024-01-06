from tkinter import mainloop
import turtle as t


t.bgcolor('gold')
def pos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Tika
pos(0,200)
t.color('red')
t.begin_fill()
t.circle(40)
t.end_fill()

# left eyebrow

pos(-30,200)
t.color('black')
t.begin_fill()
t.right(45)
for i in range(20):
    t.left(3)
    t.back(10)
for i in range(10):
    t.right(3)
    t.back(10)
t.right(18)
for i in range(13):
    t.left(3)
    t.forward(10)
for i in range(20):
    t.right(2)
    t.forward(10)
t.end_fill()

# right eyebrow

t.left(80)
pos(30,200)
t.color('black')
t.begin_fill()

for i in range(20):
    t.right(3)
    t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(10)
t.left(18)

for i in range(13):
    t.right(3)
    t.back(10)
for i in range(20):
    t.left(2)
    t.back(10)
t.end_fill()

# right eyes


pos(40,150)
#t.color('black')
t.pensize(15)
t.left(10)

for i in range(20):
   t.right(3)
   t.forward(10)
for i in range(10):
    t.left(3)
    t.forward(5)
t.right(3)
for i in range(10):
    t.left(3)
    t.back(5)
for i in range(20):
    t.right(3)
    t.back(10)
t.pensize(1)

pos(130,130)
t.begin_fill()
t.circle(40)
t.end_fill()
t.color('white')
t.begin_fill()
pos(115,175)
t.circle(10)
t.end_fill()

# left eyes

pos(-40,150)
t.color('black')
t.pensize(15)
t.right(25)

for i in range(20):
   t.left(3)
   t.back(10)

for i in range(10):
    t.right(3)
    t.back(5)
t.left(3)
for i in range(10):
    t.right(3)
    t.forward(5)
for i in range(20):
    t.left(3)
    t.forward(10)
t.pensize(1)

pos(-130,130)
t.begin_fill()
t.circle(40)
t.end_fill()
t.color('white')
t.begin_fill()

pos(-115,175)
t.circle(10)
t.end_fill()

# Nose

t.color('black')
pos(-60,10)
t.right(70)
for i in range(5,12):
    t.pensize(i)
    t.left(7)
    t.forward(10)
for i in range(12,5,-1):
    t.pensize(i)
    t.left(7)
    t.forward(10)

# nose ring
t.pensize(4)
t.color('red')
pos(90,-15)
t.circle(40) 
#t.end_fill()

''' lips

t.color('red')
pos(-130,-90)
t.right(60)

for i in range(3):
    t.left(3)
    t.forward(5)
for i in range(10):
   t.left(4)
   t.forward(6)
for i in range(10):
    t.right(10)
    t.left(7)
t.left(135)'''

t.hideturtle()
mainloop()