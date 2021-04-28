import pygame

class Ship():   #绘制一副飞船在屏幕上的画
    def __init__(self,screen,speed):  #screen 表示飞船要绘制在哪
        self.screen=screen  #初始化飞船设置其位置
       # print("Ship.screen=",self.screen)
        self.image=pygame.image.load('huiji.bmp')  #返回表示飞船的surface（是屏幕的一部分）  抓图像
       # print("Ship.image=",self.image)
        self.rect=self.image.get_rect()  #rect 矩形   右边是表示图片的‘矩形‘    图像位置赋予对象
        #print(self.rect)  #像素
        self.screen_rect=screen.get_rect()  #右边是表示屏幕的’矩形‘           屏幕位置赋予对象
        #print(self.screen_rect.top)
        #get_rect( )是pygame模块的一个方法
        self.rect.centerx=self.screen_rect.centerx  #将飞船中心X坐标和窗口的X坐标重合

        self.rect.bottom=self.screen_rect.bottom   #将飞船低部与窗口低部重合
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.speed=speed
    def blitme(self):
        self.screen.blit(self.image,self.rect)  #blit 块传送   把这个图像传到 self.rect制定的位置

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=self.speed

        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=self.speed

        if self.moving_up and self.rect.top>0:
            self.rect.centery -= self.speed

        if self.moving_down and self.rect.bottom<=self.screen_rect.bottom :
            self.rect.centery += self.speed

    def center_ship(self):
       # self.center=self.screen_rect.centerx
        self.rect.centerx = self.screen_rect.centerx

        self.rect.centery = self.screen_rect.bottom