
import pgzrun  # here we are importing a file to create a function OR we can say it work as turtle 
# here we can create a output screen likes in turtle and print the output
from turtle import Screen

HEIGHT = 400 # setting height of the screen
WIDTH = 500 # setting width of screen
box1_vx = 1  # global variable
box2_vy = 1 # global variable

box1 = Rect((100,250),(50,40)) # creating a rectangle
box2 = Rect((50,50),(60,20))

def draw(): # function used to show the data on the screen
    screen.fill('black') # it will change the color of screen to black
    screen.draw.text("hello world", (20,30), color="white")  # IT will print the text on the screen with the margin of 20 at x-axis and 30 at y-axis
    screen.draw.rect(box1,'red') # it will draw the rectangle on the screen
    screen.draw.filled_rect(box2,'blue') 
def update():# it will update function in milliseconds OR to move the object
    global box1_vx
    global box2_vy


    box1.x+=box1_vx # changing the movement of first rectangle
    if box1.x>WIDTH:
        box1.x=0
    if box1.x<0:
        box1.x=WIDTH

 
    box2.y+=box2_vy # changing the movement of second rectangle
    if box2.y>HEIGHT:
     box2.y=0
    if box2.y<0:
        box2.y=HEIGHT

    if box1.colliderect(box2):
        box1_vx=-box1_vx
        box2_vy=-box2_vy

   
pgzrun.go()
