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
        self.prep_high_score()
        self.perp_level()


    def prep_score(self):
        #先把得分变成字符串
        rounded_score=int(round(self.data.score,-1)) #-1就是10为  2- 百位   1就是0.1位
        data_str="{:,}".format(rounded_score)  #:后面带填充的字符   格式化字符串的函数format
        #再用字符串形成‘分数图片’
        self.score_image = self.font.render(data_str, True, self.text_color, self.pm.bg_color)
        #获取‘分数图片’的各种虚拟属性
        self.score_rect=self.score_image.get_rect()
        #‘分数图片’在游戏屏幕中定位
        self.score_rect.top=self.screen_rect.top
        self.score_rect.right=self.screen_rect.right-20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)  #绘制文本  传送
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.txt_image, self.txt_rect)
        self.screen.blit(self.level_image, self.level_rect)

        level = Txt("当前等级：", self.level_rect.top ,self.level_rect.bottom,self.level_rect.left-100,self.level_rect.right-100)
        self.screen.blit( level.image,  level.rect)

        now_core=Txt("当前分数：", self.score_rect.top ,self.score_rect.bottom,self.level_rect.left-100,self.level_rect.right-100)
        self.screen.blit(now_core.image, now_core.rect)
        #做出blit这个动作的人是一个Surface类的实例,这个人即将在自己身上画图,他需要两个参数:要画的图片,和画的位置,即source和dest.



    def prep_high_score(self):
        high_score=int(round(self.data.high_score,-1))
        high_score_str="{:,}".format(high_score)

        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.pm.bg_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

        aaa = "最高分:"
        text=pygame.font.Font("C:\Windows\Fonts\STXINWEI.ttf",30)  #汉字显示  格式设置
        self.txt_image=text.render(aaa, True, self.text_color, self.pm.bg_color)  # render形成图像

        #self.txt_image = self.font.render(aaa, True, self.text_color, self.pm.bg_color)
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.centerx = self.screen_rect.centerx-86
        self.txt_rect.top = self.score_rect.top




    def perp_level(self):
        # level_score=int(round(self.data.level))
        #
        # level_score_str="{:,}".format(level_score)

        level_score_str=str(self.data.level)
        self.level_image=self.font.render(level_score_str, True, self.text_color, self.pm.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.top=self.score_rect.bottom
        self.level_rect.centerx = self.screen_rect.right-20


class Txt():
    def __init__(self,str,top,bottom,lift,right,):

        self.text_color = (30, 30, 30)
        self.text=pygame.font.Font("C:\Windows\Fonts\STXINWEI.ttf",30)
        self.image=self.text.render(str, True, self.text_color, (148,41,90))
        self.rect=self.image.get_rect()
        self.rect.top=top
        self.rect.bottom=bottom
        self.rect.left=lift
        self.rect.right=right

