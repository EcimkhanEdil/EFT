import pygame
from random import randint
from time import time
import webbrowser
pygame.init()
pygame.display.set_caption('TrueProger and FalseProger')

#zastavka=input('хотите посмотреть заставку?(да/нет)')
#if zastavka=='да':
#    webbrowser.open('https://www.youtube.com/watch?v=AqM-N4h3ViI')

class Chvk():
    def __init__(self,png,x,y,width,heigth,hp):
        self.rect=pygame.Rect(x, y, width, heigth)
        self.png=pygame.image.load(png)
        self.hp=hp
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
    def fill(self):
        pygame.draw.rect(linox,self.fire)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Bullet():
    def __init__(self,bul,damage,x_b, y_b, width_b, heigth_b):
        self.bal=pygame.image.load(bul)
        self.damage=damage
        self.fire_2=pygame.Rect(x_b, y_b+10, width_b, heigth_b)
        self.coor_x=x_b
        self.coor_y=y_b
    def draw_fire(self):
        linox.blit(self.bal,(self.coor_x,self.coor_y))
    def draw_fire_2(self):
        linox.blit(self.bal,(self.fire_2.x,self.fire_2.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Bang():
    def __init__(self,bang,x,y):
        self.bang=pygame.image.load(bang)
        self.x=x
        self.y=y
    def bangg(self):
        linox.blit(self.bang,(self.x,self.y))
        

f_x=250
f_y=250

kill=0

x=0
y=0

bg=pygame.image.load('5.png')
pl=Chvk('pl.png',250,250,50,100,100)
en=Chvk('en.png',100,250,50,100,50)

bull=10

#bullett=0

temp=0

bullett=Bullet('bullet.png',50,600,600,25,10)#
bang=Bang('bang!.png',600,600)
bung=0

move_left=False
move_right=False

linox=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
run=True
#linox.fill((41, 227, 184))
#font=pygame.font.Font(None,30).render('TrueProger_and_FalseProger',True,(227, 68, 248 ))
while run:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button ==1:
            bullett=Bullet('bullet.png',25,pl.rect.x-48,pl.rect.y+3,25,10)
            bullett.draw_fire()
            bullett.draw_fire_2()
            bang=Bang('bang!.png',pl.rect.x-60,pl.rect.y-5)
            bull=160
            bung=80
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                move_left=True
            elif event.key==pygame.K_d:
                move_right=True
            
            elif event.key==pygame.K_w:
                pl.rect.y-=30
                temp=160
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                move_left=False
            elif event.key==pygame.K_d:
                move_right=False
                
    if move_left==True:
        pl.rect.x-=1
    if move_right==True:
        pl.rect.x+=1
        
    
    
    linox.blit(bg,(0,0))
    pl.drawd()
    en.drawd()
    
    if pl.rect.y<=220 and temp<=0:
        pl.rect.y=250
    if temp<=160:
        temp-=15

    if bull<=1000 and bull>0:
        bullett.fire_2.x-=2
        bullett.draw_fire_2()
        bull-=1
    if bung<=1000 and bung>0:
        bang.bangg()
        bung-=1
        
    if bullett.fire_2.x<=en.rect.x+40 and bullett.fire_2.y>=en.rect.y:
        en.hp-=bullett.damage
        bullett.fire_2.x=-100
    if en.hp<=0 and kill:
        en.x=-100
        en.y=0
        kill=100
    if kill<=1000 and kill>0:
        en.rect.y+=2
        kill-=1
    if en.rect.y>=250:
        kill=0
        en.rect.y=250
