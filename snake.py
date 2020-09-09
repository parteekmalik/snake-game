import pygame
import random
from pygame import *
pygame.init()
pygame.display.set_caption("Snake")
win = pygame.display.set_mode((1280,640))
pos=[32,32]
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(x):
    screen_text = font.render(x, True, (255,0,0))
    win.blit(screen_text,(0,0))
    
def plot_snake():
    for x,y in snk_list:
        pygame.draw.rect(win, (255,255,255), [x, y,32 ,32])
    pygame.draw.rect(win, (0,0,0), [snk_list[len(snk_list)-1][0],snk_list[len(snk_list)-1][1] ,32 ,32])
    if list[4] is True:
          pygame.draw.rect(win,(255,255,255),(pos[0],pos[1],32,32))
          pygame.draw.circle(win,(0,0,0),(pos[0]+26,pos[1]+8),2)
          pygame.draw.circle(win,(0,0,0),(pos[0]+26,pos[1]+24),2)
          pygame.draw.rect(win,(255,0,0),(pos[0]+32,pos[1]+12,6,8))
    if list[1] is True:
          pygame.draw.rect(win,(255,255,255),(pos[0],pos[1],32,32))
          pygame.draw.circle(win,(0,0,0),(pos[0]+8,pos[1]+8),2)
          pygame.draw.circle(win,(0,0,0),(pos[0]+8,pos[1]+24),2)
          pygame.draw.rect(win,(255,0,0),(pos[0],pos[1]+12,-4,8))
    if list[2] is True:
          pygame.draw.rect(win,(255,255,255),(pos[0],pos[1],32,32))
          pygame.draw.circle(win,(0,0,0),(pos[0]+8,pos[1]+8),2)
          pygame.draw.circle(win,(0,0,0),(pos[0]+24,pos[1]+8),2)
          pygame.draw.rect(win,(255,0,0),(pos[0]+12,pos[1]-6,8,8))
    if list[3] is True:
          pygame.draw.rect(win,(255,255,255),(pos[0],pos[1],32,32))
          pygame.draw.circle(win,(0,0,0),(pos[0]+8,pos[1]+26),2)
          pygame.draw.circle(win,(0,0,0),(pos[0]+24,pos[1]+26),2)
          pygame.draw.rect(win,(255,0,0),(pos[0]+12,pos[1]+32,8,8))
snk_list = []
fpos=[224,224]
list=[True,False,False,False,True,False,4,0,10]
#     run,left  ,up   ,down,right,eaten,speed,list[7]
def dead():
            pygame.display.set_caption("Snake-You Loose")
            list[0]=False
def draw():
    
       pygame.draw.rect(win,(0,0,0),(0,0,1280,640))
       pygame.draw.rect(win,(255,0,0),(fpos[0],fpos[1],32,32))

def move():
    if list[2]: 
        pos[1]-=list[6]
        if [pos[0],pos[1]-32] in snk_list[:-1] :
            dead()
    if list[3]:
        pos[1]+=list[6]
        if [pos[0]+32,pos[1]+32] in snk_list[:-1] :
            dead()
    if list[1]:
        pos[0]-=list[6]
        if [pos[0]-32,pos[1]] in snk_list[:-1] :
            dead()
    if list[4]:
        pos[0]+=list[6]
        if [pos[0]+32,pos[1]] in snk_list[:-1] :
            dead()
    return pos[0],pos[1]

def fruit():
    if pos[0]==fpos[0] :
        if list[3] is True and pos[1]==fpos[1]:
            
            list[5]=True
        if list[2] is True and pos[1]==fpos[1]:
            list[5]=True
    if  pos[1]==fpos[1]:
        if list[4] is True and pos[0]==fpos[0]:
            
            list[5] =True
        if list[1] is True and pos[0]==fpos[0]:
            list[5]=True
    if list[5]:
      list[8]+=12
     
      while list[5]:
         fpos[1]=random.randint(0,640)
         fpos[0]=random.randint(0,1280)
         if fpos[0]%32==0 and fpos[1]%32==0 and fpos[0]!=1280 and fpos[1]!=640 and [fpos[0],fpos[1]] not in snk_list:
             list[5]=False
      list[7]+=10

      
def action():
    keys = pygame.key.get_pressed()
    pos[0],pos[1]=move()
    if keys [pygame.K_UP]:
     if list[3] is False :
       if list[1] is True or list[4] is True:
        list[2]=True
        if pos[0]%32!=0:
            pos[0]=int(pos[0]/32)
            if list[4] is True:
               pos[0]=(pos[0]+1)*32
            if list[1] is True:
               pos[0]=(pos[0])*32
        list[4]=list[1]=False
    elif keys [pygame.K_DOWN]:
     if list[2] is False :
       if list[1] is True or list[4] is True:
        list[3]=True
        if pos[0]%32!=0:
            pos[0]=int(pos[0]/32)
            if list[4]:
               pos[0]=(pos[0]+1)*32
            else:
                pos[0]=(pos[0])*32
        list[1]=list[4]=False
    elif keys[pygame.K_RIGHT]:
     if list[1] is False :
       if list[2] is True or list[3] is True:
        list[4]=True
        if pos[1]%32!=0:
            pos[1]=int(pos[1]/32)
            if list[3]:
               pos[1]=(pos[1]+1)*32
            else:
                pos[1]=(pos[1])*32
        list[2]=list[3]=False
    elif keys[pygame.K_LEFT]:
     if list[4] is False :
       if list[2] is True or list[3] is True:
        list[1]=True
        if pos[1]%32!=0:
            pos[1]=int(pos[1]/32)
            if list[3]:
                
               pos[1]=(pos[1]+1)*32
            else:
                pos[1]=(pos[1])*32
        list[3]=list[2]=list[4]=False
    if pos[0]>1248 or pos[1]>608 or pos[0]<0 or pos[1]<0:
        dead()

        
while list[0]:
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            list[0] = False
    fruit()
    action()
    draw()
    snk_list.append([pos[0],pos[1]])
    if len(snk_list)>list[8]:
       del snk_list[0]
    plot_snake()
    text_screen("Score: " + str(list[7]))

pygame.quit()

