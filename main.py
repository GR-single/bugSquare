import pygame
import pygame.freetype
import sys
import time
from fangkuai import Fangkuai
from zuheti import Zuheti
from random import randint
from panduan import*
zongfen=0
hui=(230,230,230)
hei=(0,0,0)
lan=(100,100,200)
pygame.init()
beijing=pygame.display.set_mode((600,600))
kedong=[]
lines=[]
hang=20
fx=0
stop=0
play=False
jishi=True
while hang>0:
    newline=[]
    lines.append(newline)
    hang=hang-1
anniu1=pygame.Rect(400,0,200,50)

zi1=pygame.freetype.Font("C:\Windows\Fonts\comic.ttf",40)

while True:
    if play:        
        if len(kedong)==0:
            kind=randint(1,5)
            newzht=Zuheti(beijing,kind,hui,lan)
            kedong.append(newzht)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    fx=2
                elif event.key==pygame.K_RIGHT:
                    fx=1
                elif event.key==pygame.K_DOWN:
                    fx=3
                elif event.key==pygame.K_SPACE:
                    kedong[0].xuanzhuan()
                elif event.key==pygame.K_q:
                    play=False
                
        if jishi:
            start=time.perf_counter()
            jishi=False
        end=time.perf_counter()
        if (end-start)>=1:
            kedong[0].yidong(3,30,lines)
            jishi=True
        kedong[0].yidong(fx,30,lines)
        fx=0
        stop=0
        for l in lines:
            if isxiabian(kedong[0].fks)==False or peng(kedong[0].fks,l)==False:
                stop=1
        if stop==1:
            for f in kedong[0].fks:
                h=int((600-f.frb.bottom)/30)
                lines[h].append(f)
            
            del kedong[0]
            lin=0
            dl=0
            while lin<20:
                if len(lines[lin])==20:
                    for l in lines[lin+1:]:
                        lineyd(l)
                    del lines[lin]
                    zongfen+=20
                    new=[]
                    lines.append(new)
                else:
                    lin+=1
        
            
        beijing.fill(hei)
        for l in lines:
            for f in l:
                f.xian()
        if stop==0:
            kedong[0].xian()
        else:
            if len(lines[19])!=0:
                l=0
                while l<20:
                    lines[l].clear()
                    l+=1
    else:
        anniu=pygame.Rect(250,250,100,100)
        pygame.draw.rect(beijing,(255,255,255),anniu)
        zi=pygame.freetype.Font("C:\Windows\Fonts\comic.ttf",30)
        zir=zi.render_to(beijing,(260,260),"PLAY",(0,100,200))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.pos[0]>anniu.left and event.pos[0]<anniu.right and event.pos[1]>anniu.top and event.pos[1]<anniu.bottom:
                    play=True
    pygame.draw.rect(beijing,(255,255,255),anniu1)
    zir1=zi1.render_to(beijing,(400,0),str(zongfen),(0,100,200))
    pygame.display.update()
