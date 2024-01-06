import pgzrun



HEIGHT = 400 # setting height of the screen
WIDTH = 400

box1 = Rect((120,50),(40,40)) # creating a rectangle
box2 = Rect((180,50),(40,40))
box3 = Rect((240,50),(40,40))
plat2 =Rect((150,50),(150,15))
plat = Rect((WIDTH/2-250/2,HEIGHT-50),(250,25))

ivy = 3
ivy2 = 3
ivy3 = 3

def item_motion_control(obj,plt,oy):

    obj.y+=oy
    if obj.y>HEIGHT:
        obj.y=0
    if obj.y<0:
        obj.y=0
        oy = -oy
    if obj.colliderect(plt):
        oy=-oy
    return oy
    

        
def draw():
    screen.fill('black')
    screen.draw.rect(box1,'red')
    screen.draw.rect(box2,'green')
    screen.draw.rect(box3,'blue')
    screen.draw.filled_rect(plat,'brown')
    screen.draw.rect(plat2,'white')

def update():
    #item_motion_control()
    global ivy
    global ivy2
    global ivy3

    ivy = item_motion_control(box1,plat,ivy)
    ivy2 = item_motion_control(box2,plat,ivy2)
    ivy3 = item_motion_control(box3,plat,ivy3)
    if keyboard.left:
        plat.x-=3
    elif keyboard.right:
        plat.x+=3
        
pgzrun.go()

