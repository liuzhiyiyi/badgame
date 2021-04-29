import pygame.font   #文本渲染到屏幕上

class Button():
    def __init__(self, pm, screen, msg):
        self.screen=screen  #?
        self.screen_rect=screen.get_rect()

        self.width=200
        self.height=50

        self.button_color=(0, 255, 0)
        self.text_color=(255, 255, 255)
        self.front=pygame.font.SysFont(None, 48)  #使用什么字体来渲染文本
        #创建按钮的对象
        self.rect=pygame.Rect(0, 0, self.width, self.height)  #Rect(left, top, width, height) -> Rect
        self.rect.center=self.screen_rect.center  #使其居中center

        self.prep_msg(msg)


    def prep_msg(self,msg):
        #front.render将msg文本文件渲染为图像

        #.render（内容="xxx"，是否抗锯齿，字体颜色，字体背景颜色）
        self.msg_image=self.front.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)  #填充按钮颜色
        self.screen.blit(self.msg_image, self.msg_image_rect)  #绘制文本  传送
        #做出blit这个动作的人是一个Surface类的实例,这个人即将在自己身上画图,他需要两个参数:要画的图片,和画的位置,即source和dest.

