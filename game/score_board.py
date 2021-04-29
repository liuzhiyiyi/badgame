import pygame.font

class Scoreboard():
    def __init__(self,pm,screen,data):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.pm=pm
        self.data=data
        #显示得分字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)#实例化一个字体对象

        self.prep_score()

    def prep_score(self):
        #先把得分变成字符串
        data_str=str(self.data.score)
        #再用字符串形成‘分数图片’
        self.score_image = self.font.render(data_str, True, self.text_color, self.pm.bg_color)
        #获取‘分数图片’的各种虚拟属性
        self.rect=self.score_image.get_rect()
        #‘分数图片’在游戏屏幕中定位
        self.rect.top=self.screen_rect.top
        self.rect.right=self.screen_rect.right-20

    def show_score(self):
        self.screen.blit(self.score_image, self.rect)  #绘制文本  传送
        #做出blit这个动作的人是一个Surface类的实例,这个人即将在自己身上画图,他需要两个参数:要画的图片,和画的位置,即source和dest.