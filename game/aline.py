import  pygame
from pygame.sprite import Sprite


class Aline(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化外星人并设置其起始位置
        super(Aline, self).__init__()
        self.screen=screen                 #Surface
       # print("Aline.screen=",self.screen)
        self.ai_setting=ai_settings  #?
        #载入图片
        self.image=pygame.image.load('sun.bmp')
        #print("Aline.image=", self.image)   #Surface
        self.rect=self.image.get_rect()
       # print("Aline.erct=", self.rect)
        #最初左上角位置
        self.rect.x=self.rect.width       #self.rect.x  是左上角顶点的坐标(在背景上)
        self.rect.y=self.rect.height    #self.rect.height  是图形的高
        #存精准位置
        self.xx = float(self.rect.x)
        self.yy = float(self.rect.y)
        self.speed=1
        self.speed_1=1
        self.direction=1


    def blitme(self):  #在（背景上）指定位置处绘制外星人
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.xx+=(self.ai_setting.alien_speed*self.direction)

        self.rect.x=self.xx
        # self.yy+=self.speed_1
        #
        # self.rect.y=self.yy

    def check_edges(self):
        if self.rect.right>=self.screen.get_rect().right or self.rect.left<=0:
            return True

        # elif self.rect.left<=0:
        #     return True