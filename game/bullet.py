import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)#为子弹创建一个矩形，提供左上角XY坐标+宽+高
        self.rect.centerx=ship.rect.centerx   #飞船坐标赋予
        self.rect.top=ship.rect.top           #飞船坐标赋予   子弹的矩形上方与飞船上方重叠
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed

    def update(self):

        self.y -= self.speed_factor
        #print(self.y)

        self.rect.y = self.y
        # if self.rect.bottom<500:
        #     print(self.rect.bottom)
        #     self.remove()    ##?为什么不能在类里面直接删除这个对象



    def draw_bullet(self):  # 在屏幕上绘制子弹

        pygame.draw.rect(self.screen,self.color,self.rect)  #在screen上绘制矩形

