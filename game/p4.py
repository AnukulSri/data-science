import pgzrun

HEIGHT = 500
WIDTH = 500

box1 = Rect((220,150),(40,40))
box2 = Rect((220,200),(40,40))
box3 = Rect((220,250),(40,40))
platform = Rect((50,150),(10,150))
platform2 = Rect((450,150),(10,150))


ivy = 3
ivy2 = 3
ivy3 = 3
sp= 3     
def motion_changes(item,plat,s,plt): # here item is to denote boxex and s is to denote speed, plat is used for platfrom
    
    item.x += s
    if item.x>WIDTH:
        item.x=0
    elif item.x<0:
        item.x =0
        s = -s
    elif item.colliderect(plat):
         s= -s
    elif item.colliderect(plt):
        s= -s
    return s

def plat_form_control(p1,p2,sp):# this function is to control platforms


    if p1.y>HEIGHT: # its means if platform 1 goes above the screen height then,
        p1.y=0 # stop it
    elif p1.y<0: # its means if platform 1 goes below the screen height then,
        p1.y=0 # stop it
        sp = -sp # it means the speed will be zero
    elif p2.y>HEIGHT:
        p2.y=0
    elif p2.y<0:
        p2.y=0
        sp=-sp
    return sp

def platform_control(): # this function is for movement of platform upward and downward
    if keyboard.up:
           platform.y -=3 
           platform2.y += 3
    elif keyboard.down:
        platform.y +=3
        platform2.y -=3
    


def draw (): # draw function is used to draw the shapes,text etc.
    screen.fill('Black')
    screen.draw.rect(box1,'red')
    screen.draw.rect(box2,'green')
    screen.draw.rect(box3,'blue')
    screen.draw.filled_rect(platform,'brown')
    screen.draw.filled_rect(platform2,'brown')

def update():
   
        global ivy
        global ivy2
        global ivy3
        global sp

        ivy = motion_changes(box1,platform2,ivy,platform)
        ivy2 = motion_changes(box2,platform2,ivy2,platform)
        ivy3 = motion_changes(box3,platform2,ivy3,platform)
        sp= plat_form_control(platform,platform2,sp)
        platform_control()

pgzrun.go()