import pygame
from fangkuai import Fangkuai
from panduan import*
class Zuheti():
    def __init__(self,bj,kind,yanseb,yansen):
        self.kind=kind
        self.bj=bj
        self.yanseb=yanseb
        self.yansen=yansen
        self.cishu=0
        self.zt=0
        self.fks=[]
        a=4
        while a>0:
            newfk=Fangkuai(self.bj,self.yanseb,self.yansen)
            self.fks.append(newfk)
            a=a-1
        if self.kind==1:
            self.fks[0].frb.left=0
            self.fks[0].frb.top=0
            self.fks[1].frb.left=self.fks[0].frb.right
            self.fks[1].frb.top=self.fks[0].frb.top
            self.fks[2].frb.left=self.fks[0].frb.left
            self.fks[2].frb.top=self.fks[0].frb.bottom
            self.fks[3].frb.left=self.fks[0].frb.right
            self.fks[3].frb.top=self.fks[0].frb.bottom
        elif self.kind==2:
            self.fks[0].frb.left=0
            self.fks[0].frb.top=30
            self.fks[2].frb.bottom=self.fks[0].frb.top
            self.fks[2].frb.left=self.fks[0].frb.right
            self.fks[1].frb.top=self.fks[0].frb.top
            self.fks[1].frb.left=self.fks[0].frb.right
            self.fks[3].frb.top=self.fks[1].frb.top
            self.fks[3].frb.left=self.fks[1].frb.right
        elif self.kind==3:
            self.fks[0].frb.top=0
            self.fks[0].frb.left=0
            self.fks[1].frb.top=self.fks[0].frb.bottom
            self.fks[1].frb.left=self.fks[0].frb.left
            self.fks[2].frb.top=self.fks[1].frb.bottom
            self.fks[2].frb.left=self.fks[0].frb.left
            self.fks[3].frb.top=self.fks[2].frb.bottom
            self.fks[3].frb.left=self.fks[0].frb.left
        elif self.kind==4:
            self.fks[0].frb.top=0
            self.fks[0].frb.left=0
            self.fks[1].frb.top=self.fks[0].frb.bottom
            self.fks[1].frb.left=self.fks[0].frb.left
            self.fks[2].frb.top=self.fks[0].frb.bottom
            self.fks[2].frb.left=self.fks[1].frb.right
            self.fks[3].frb.top=self.fks[0].frb.bottom
            self.fks[3].frb.left=self.fks[2].frb.right
        elif self.kind==5:
            self.fks[0].frb.top=30
            self.fks[0].frb.left=0
            self.fks[1].frb.top=self.fks[0].frb.top
            self.fks[1].frb.left=self.fks[0].frb.right
            self.fks[2].frb.top=self.fks[0].frb.top
            self.fks[2].frb.left=self.fks[1].frb.right
            self.fks[3].frb.top=0
            self.fks[3].frb.left=self.fks[2].frb.left
    def yidong(self,fangxiang,juli,lines):
        self.juli=juli
        self.lines=lines
        if fangxiang==1 and isyoubian(self.fks) and youpeng(self.fks,self.lines):
            for fk in self.fks:
                fk.frb.right+=self.juli
        if fangxiang==2 and iszuobian(self.fks) and zuopeng(self.fks,self.lines):
            for fk in self.fks:
                fk.frb.left-=self.juli
        if fangxiang==3 and isxiabian(self.fks):
            for fk in self.fks:
                fk.frb.bottom+=self.juli
    def xuanzhuan(self):
        if self.kind==2:
            self.zt=self.cishu%4+1
            if self.zt==1:
                self.fks[0].frb.left=self.fks[1].frb.left
                self.fks[0].frb.top=self.fks[1].frb.bottom
            elif self.zt==2:
                self.fks[2].frb.bottom=self.fks[1].frb.bottom
                self.fks[2].frb.right=self.fks[1].frb.left
            elif self.zt==3:
                self.fks[3].frb.left=self.fks[1].frb.left
                self.fks[3].frb.bottom=self.fks[1].frb.top
            elif self.zt==4:
                self.fks[3].frb.top=self.fks[1].frb.top
                self.fks[3].frb.left=self.fks[1].frb.right
                self.fks[2].frb.bottom=self.fks[1].frb.top
                self.fks[2].frb.left=self.fks[1].frb.left
                self.fks[0].frb.right=self.fks[1].frb.left
                self.fks[0].frb.top=self.fks[1].frb.top
        if self.kind==3:
            self.zt=self.cishu%2+1
            if self.zt==1:
                x=0
                while x<=2:
                    self.fks[x].frb.top+=(3-x)*30
                    self.fks[x].frb.left+=(3-x)*30
                    x+=1
            if self.zt==2:
                x=0
                while x<=2:
                    self.fks[x].frb.top-=(3-x)*30
                    self.fks[x].frb.left-=(3-x)*30
                    x+=1
        if self.kind==4:
            self.zt=self.cishu%4+1
            if self.zt==1:
                x=0
                while x<=3:
                    if x==0:
                        self.fks[0].frb.left+=30
                        self.fks[0].frb.top+=30
                    elif x!=1:
                        self.fks[x].frb.top+=(x-1)*30
                        self.fks[x].frb.left-=(x-1)*30
                    x+=1
            elif self.zt==2:
                x=0
                while x<=3:
                    if x==0:
                        self.fks[0].frb.left-=30
                        self.fks[0].frb.top+=30
                    elif x!=1:
                        self.fks[x].frb.top-=(x-1)*30
                        self.fks[x].frb.left-=(x-1)*30
                    x+=1
            elif self.zt==3:
                x=0
                while x<=3:
                    if x==0:
                        self.fks[0].frb.left-=30
                        self.fks[0].frb.top-=30
                    elif x!=1:
                        self.fks[x].frb.top-=(x-1)*30
                        self.fks[x].frb.left+=(x-1)*30
                    x+=1
            elif self.zt==4:
                x=0
                while x<=3:
                    if x==0:
                        self.fks[0].frb.left+=30
                        self.fks[0].frb.top-=30
                    elif x!=1:
                        self.fks[x].frb.top+=(x-1)*30
                        self.fks[x].frb.left+=(x-1)*30
                    x+=1
        if self.kind==5:
            self.zt=self.cishu%4+1
            if self.zt==1:
                x=0
                while x<=3:
                    if x==3:
                        self.fks[3].frb.left+=30
                        self.fks[3].frb.top+=30
                    elif x!=2:
                        self.fks[x].frb.left+=(2-x)*30
                        self.fks[x].frb.top-=(2-x)*30
                    x+=1
            elif self.zt==2:
                x=0
                while x<=3:
                    if x==3:
                        self.fks[3].frb.left-=30
                        self.fks[3].frb.top+=30
                    elif x!=2:
                        self.fks[x].frb.left+=(2-x)*30
                        self.fks[x].frb.top+=(2-x)*30
                    x+=1
            elif self.zt==3:
                x=0
                while x<=3:
                    if x==3:
                        self.fks[3].frb.left-=30
                        self.fks[3].frb.top-=30
                    elif x!=2:
                        self.fks[x].frb.left-=(2-x)*30
                        self.fks[x].frb.top+=(2-x)*30
                    x+=1
            elif self.zt==4:
                x=0
                while x<=3:
                    if x==3:
                        self.fks[3].frb.left+=30
                        self.fks[3].frb.top-=30
                    elif x!=2:
                        self.fks[x].frb.left-=(2-x)*30
                        self.fks[x].frb.top-=(2-x)*30
                    x+=1

        if self.kind!=1:
            self.cishu+=1


    def xian(self):
        for fk in self.fks:
            fk.xian()
        

