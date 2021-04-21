from math import *
import pygame,sys
from pygame.locals import *

def expression(s,sp,ep):
    s=s.split("x")
    l=len(s)
    arr=[]
    d=(ep-sp)/100
    for i in range(101):
        try:
            n=sp+(i*d)
            e="("+str(n)+")"
            ex=s[0]
            for j in range(1,l):
                ex=ex+e+s[j]
            y=eval(ex)
            arr.append(y)
        except:
            arr.append(0)
    return arr



    
    
def graph_plot(s):
    pygame.init()
    screenlenthx=800
    screenlenthy=800
    screen=pygame.display.set_mode((screenlenthx,screenlenthy))
    d=1
    running=True
    midx=0
    midy=0
    upb=10
    lwb=-10
    rtb=10
    ltb=-10
    d=1
    txw=15
    arr=expression(s,ltb,rtb)
    while running:
        screen.fill((0,0,0))
        upb=midy+(10*d)
        lwb=midy+((-10)*d)
        rtb=midx+(10*d)
        ltb=midx+((-10)*d)

        p=int(rtb-ltb/100)
        r=700/(upb-lwb)
        r1=700/(rtb-ltb)
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    running=False
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        running=False
                    elif event.key==K_SPACE:
                        d+=1
                        txw-=3
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)
                        arr=expression(s,ltb,rtb)

                    elif event.key==K_BACKSPACE:
                        if(d>0):
                            if(d>1):
                                d-=1
                                txw+=3
                            else:
                                d-=0.01
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)  
                        arr=expression(s,ltb,rtb)
                    elif event.key==K_LEFT:
                        midx+=1
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)
                        arr=expression(s,ltb,rtb)
                    elif event.key==K_RIGHT:
                        midx-=1
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)
                        arr=expression(s,ltb,rtb)
                    elif event.key==K_UP:
                        midy-=1
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)
                        arr=expression(s,ltb,rtb)
                    elif event.key==K_DOWN:
                        midy+=1
                        upb=midy+(10*d)
                        lwb=midy+((-10)*d)
                        rtb=midx+(10*d)
                        ltb=midx+((-10)*d)
                        arr=expression(s,ltb,rtb)
                        
                    
                        
        for i in range(int(lwb),int(upb)):
            if(i==0):
                lw=2;c=(0,255,0)
            else:
                lw=1;c=(0,255,255)
            pygame.draw.line(screen,c,(50,50+int((upb-i)*r)),(750,50+int((upb-i)*r)),lw)              
        for i in range(int(ltb),int(rtb)):
            if(i==0):
                lw=2;c=(0,255,0)
            else:
                lw=1;c=(0,255,255)
            pygame.draw.line(screen,c,(50+int((i-ltb)*r1),50),(50+int((i-ltb)*r1),750),lw) 
        

        #print(d)
        for i in range(99):
            pygame.draw.line(screen,(255,255,0),(50+int((i)*7),50+int((upb-arr[i])*r)),(50+int((i+1)*7),50+int((upb-arr[i+1])*r)),3)              
        
        
        pygame.draw.rect(screen,(255,255,255),(0,0,800,50))
        pygame.draw.rect(screen,(255,255,255),(0,50,50,800))
        pygame.draw.rect(screen,(255,255,255),(750,50,50,800))
        pygame.draw.rect(screen,(255,255,255),(0,750,800,50))
        
        for i in range(int(lwb),int(upb)+1):
            fonts2=pygame.font.Font('freesansbold.ttf',txw)
            bits=fonts2.render(str(i),True,(0,0,0))
            screen.blit(bits,(755,50+int((upb-i)*r)))
        for i in range(int(ltb),int(rtb)+1):
            fonts2=pygame.font.Font('freesansbold.ttf',txw)
            bits=fonts2.render(str(i),True,(0,0,0))
            screen.blit(bits,(50+int((i-ltb)*r1),35))
  
        
        pygame.display.update()

s=input("Enter a equation:\ny=")
graph_plot(s)