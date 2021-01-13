import pygame
class Fangkuai():
    def __init__(self,bj,yanseb,yansen):
        self.bj=bj
        self.yanseb=yanseb
        self.yansen=yansen
        self.frb=pygame.Rect(100,100,30,30)     
    def ydxia(self,ju):
        self.frb.bottom+=ju
    def xian(self):
        pygame.draw.rect(self.bj,self.yanseb,self.frb)
        self.frn=pygame.Rect(self.frb.left+2,self.frb.top+2,26,26)
        pygame.draw.rect(self.bj,self.yansen,self.frn)

