import  pygame

from pygame.sprite import Sprite


class Highbullet(Sprite):
    def __init__(self, ai_settings, screen):
        # 初始化外星人并设置其起始位置
        super(Highbullet, self).__init__()
        self.screen = screen
        self.ai_setting=ai_settings
        self.image = pygame.image.load('h1.bmp')
        self.rect = self.image.get_rect()
        self.rect.x=self.screen.get_rect().centerx
        #self.rect.y=self.screen.get_rect().top-100  # 特效子弹起始位置
        self.yy=float(self.rect.y)
        self.speed=ai_settings.super_bullet_speed
        self.number=0



    def update(self):

            self.yy+= self.speed  #单纯的数字加

            self.rect.y = self.yy    #让坐标的值等于数字


    def stop(self):
        pygame.sprite.Sprite.kill(self)




    def blitme(self):
        self.screen.blit(self.image,self.rect)  #blit 块传送   把这个图像传到 self.rect制定的位置






