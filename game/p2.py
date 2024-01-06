import pgzrun



HEIGHT = 400 # setting height of the screen
WIDTH = 400

box1 = Rect((120,50),(40,40)) # creating a rectangle
box2 = Rect((180,50),(40,40))
box3 = Rect((240,50),(40,40))
plat2 =Rect((150,50),(150,15))
plat = Rect((WIDTH/2-250/2,HEIGHT-50),(250,25))

ivy =3

def item_motion_control():
    global ivy
    box1.y+=ivy
    if box1.y>HEIGHT:
        box1.y=0
    if box1.y<0:
        box1.y=0
        ivy = -ivy
    if box1.colliderect(plat):
        ivy=-ivy
    
def it_mo_co():
    global ivy
    box2.y+=ivy
    if box2.y>HEIGHT:
        box2.y=0
    if box2.y<0:
        box2.y=0
        ivy = -ivy
    if box2.colliderect(plat):
        ivy=-ivy

def i_m_c():
    global ivy
    box3.y+=ivy
    if box3.y>HEIGHT:
        box3.y=0
    if box3.y<0:
        box3.y=0
        ivy = -ivy
    if box3.colliderect(plat):
        ivy=-ivy
        
def draw():
    screen.fill('black')
    screen.draw.rect(box1,'red')
    screen.draw.rect(box2,'green')
    screen.draw.rect(box3,'blue')
    screen.draw.filled_rect(plat,'brown')
    screen.draw.rect(plat2,'white')

def update():
    item_motion_control()
    it_mo_co()
    i_m_c()

    if keyboard.left:
        plat.x-=3
    elif keyboard.right:
        plat.x+=3
        
pgzrun.go()