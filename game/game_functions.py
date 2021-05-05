import pygame , sys
from bullet import Bullet
from aline import  Aline
#from random import randint
from time import sleep
from high_energy_bullet import Highbullet
#from pygame.sprite import Sprite
import random
from threading import Timer
import _thread





def update_screen(duixiang,screen,data,ship,bullets,alines,play_button,sb,change_buller,super_bullers):
    screen.fill(duixiang.bg_color)  #颜色
    ship.blitme()  # 传送图像  船图以及获取的位置
    sb.show_score()
    super_bullers.draw(screen)
    #ship.blitme() 传一个
    alines.draw(screen)  #传一编组 draw  自动绘制编组alines里面的每一个元素 到 screen

    change_buller.blitme()
    change_buller.change_speed()

    if data.game_active == True:
        for bullet in bullets.sprites():
            bullet.draw_bullet()

    if  data.game_active==False:

        play_button.draw_button()
    pygame.display.flip()   #更新整个待显示的Surface对象到屏幕上

def check_events(ship,screen,bullets,data, play_button,pm,alines,sb):  #点击键盘

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                 check_keydown_enent(event,ship,screen,bullets,data,alines,pm,sb)
            elif event.type==pygame.KEYUP:
                 check_keyup_enent(event, ship)
            elif event.type==pygame.MOUSEBUTTONDOWN :
                mouse_x,mouse_y=pygame.mouse.get_pos()  #get_pos()  返回 x,y
                check_play_button(data, play_button, mouse_x, mouse_y,pm,screen,ship,alines,bullets,sb)

def check_play_button(data, play_button, mouse_x, mouse_y,pm,screen,ship,alines,bullets,sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and  data.game_active==False: #如果按钮的区域与鼠标点击的点冲突（重合）的话就：
         # print("data.score=", data.score, "data.high_score=", data.high_score)
          #check_high_score(data,sb)
          #sb.show_score()
          new_play(pm, data, sb, alines, bullets, ship)







def new_play(pm,data,sb,alines,bullets,ship):
        pm.initialize_dynamic_setting()  # 重置速度
        data.score = 0
        pm.score_scale=2
        pm.aline_points=5
        sb.prep_score()# 先准备者，后面图像会更新
       # sb.show_score()

        pygame.mouse.set_visible(False)  # 隐藏鼠标
        data.reset_data()
        data.game_active = True
        # 重置游戏
        alines.empty()
        bullets.empty()

        data.ship_limit = 3
        sb.prep_ships()

        data.level=1

        # creat_fleet(pm,screen,ship,alines)
        ship.center_ship()

def check_keydown_enent(event,ship,screen,bullets,data,alines,pm,sb):
    if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
        ship.moving_right = True
        # ship.rect.centerx+=10

    if event.key == pygame.K_LEFT or event.key ==pygame.K_a:
        ship.moving_left = True
        # ship.rect.centerx-=10

    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True

        # ship.rect.centerx+=10

    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down= True
        # ship.rect.centerx-=10
    if  event.key == pygame.K_ESCAPE:
        sys.exit()



    if event.key ==pygame.K_SPACE: #空格
      if len(bullets)<pm.bullet_allowed:#限制子弹数量
        new_bullet=Bullet(pm,screen,ship)  #创建子弹，
        bullets.add(new_bullet)  #把子弹加入编组bullets
        #print(" 造出子弹了")
      if data.game_active == False:

          new_play(pm, data, sb, alines, bullets, ship)


def check_keyup_enent(event,ship):
    if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key ==pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False

    # if event.key==pygame.K_LEFT:
    #     ship.rect.centerx-=10



#---------------------------------------




def count_alines(pm,aline_width):  #一行放几个外星人

    available_space_x = pm.screen_width - 2 * aline_width
    return int(available_space_x/(2*aline_width))




def creat_aline(pm,screen,alines,aline_number,row_number):  #造出一个某位置的外星人


              aline = Aline(pm, screen)
              aline_width=aline.rect.width
              aline.xx=aline_width+2*aline_width*aline_number #  只是代表位置信息   #区别只有图像的长宽和坐标的位置
              #print("aline.x=",aline.xx)
              aline.rect.x=aline.xx    #这个才是定点
              aline.rect.y=aline.rect.height+50+2*aline.rect.height*row_number

              #aline.speed=randint(-1,1)    #随机移动
              aline.speed =pm.alien_speed

            #  aline.speed =pm.alien_speed     #整体移动
             # aline.speed_1=randint(-1,1)

              alines.add(aline)

def creat_superbullers(pm, screen,super_bullers):
    xx=100
    while xx<3001:
        bullet = Highbullet(pm, screen)
        bullet.rect.x=bullet.screen.get_rect().left+random.randint(1,1100)
        bullet.yy=bullet.screen.get_rect().top-xx
        bullet.rect.y=bullet.screen.get_rect().top-xx
        super_bullers.add(bullet)

        xx=xx+1000

# def creat_three_superbullers(pm, screen,super_bullers):
#
#
#         for xx in range(5):
#              creat_superbullers(pm, screen, super_bullers, xx+100)







def get_number_rows(pm,ship_height,aline_height):
    available_space_y=(pm.screen_height-(3*aline_height)-ship_height)
    number_rows=available_space_y//(2*aline_height)  #而在python3中， ‘整数/整数 = 浮点数’， ‘整数//整数 =  整数’
    return number_rows



def creat_fleet(pm,screen,ship,alines,):
    #创建外星人群
    aline = Aline(pm, screen)

    number_alines_x=count_alines(pm,aline.rect.width)  #一行能有几个外星人（附带间隔距离）
    number_rows=get_number_rows(pm,ship.rect.height,aline.rect.height)
    for row_number in range(number_rows):  #几行
        for aline_number in range(number_alines_x):
             creat_aline(pm, screen, alines, aline_number,row_number)






# def change_fleet_direction(pm,alines):
#     for aline in alines.sprites():      #sprites 精灵
#         aline.rect.y+=pm.fleet_drop_speed
#     pm.fleet_direction*=-1

# def check_fleet_edges(pm,alines):
#     for aline in alines.sprites():
#         if aline.check_edges():
#             change_fleet_direction(pm,alines)
#             break

def check_fleet_edges(pm,alines):
    for aline in alines.sprites():
        if aline.check_edges():
            aline.rect.y += pm.fleet_drop_speed

            aline.direction*= -1




def update_alines(pm,data,ship,screen,alines,bullets,sb):
    check_fleet_edges(pm,alines)
    alines.update()
    if pygame.sprite.spritecollideany(ship,alines):   #判断 某个精灵 和 指定精灵组 中的精灵的碰撞
        print("Ship hit")
        ship_hit(pm,data,screen,ship,alines,bullets,sb)
    check_aliens_bottom(pm,data,screen,ship,alines,bullets,sb)

def update_high_buller(change_buller,data):

    change_buller.update()
    # print(change_buller.rect.y)
    # print(change_buller.screen.get_rect().bottom)
    #if change_buller.rect.y>change_buller.screen.get_rect().bottom:

        #如何删除单个对象？

def check_eat_high_buller(ship,change_buller,pm,data):
    collisions=pygame.sprite.collide_rect(ship, change_buller)
    if collisions :
        pm.bullet_width = 200
        change_buller.stop()
        try:
            _thread.start_new_thread(recover_bullet,(pm,5))
        except:
            print("bad")


def recover_bullet(pm,delay):


   sleep(delay)
   pm.bullet_width = 20










def check_bullet_alien_collisions(pm,screen,ship,alines,bullets,data,sb):   #返回字典，并且添加重叠的键值对
    collisions=pygame.sprite.groupcollide(bullets,alines,True,True)  #判断 精灵组 和 精灵组 的碰撞
    if len(alines)==0:
       # print("len(alines)=",len(alines))
        bullets.empty()  #清空子弹
        pm.increase_speed()# 提升游戏难度
        sb.perp_level()  # 必须把变化的数字变成图片，每次变化都要传到图片那里一次
        data.up_level()

        creat_fleet(pm,screen,ship,alines)




    if collisions:
        for alines in collisions.values():  #看一个子弹对应的列表有几个外星人（alines）
            data.score += pm.aline_points*len(alines)
            sb.prep_score()
        check_high_score(data, sb)
        #check_high_score(data, sb)

    # if len(alines)==0:
    #     bullets.empty()  #清空子弹
    #     pm.increase_speed()# 提升游戏难度
    #     creat_fleet(pm,screen,ship,alines)

def update_bullets(pm,screen,ship,alines,bullets,data,sb,change_buller):   #函数二合一
    for ii in bullets.copy():   #让子弹消失

            if ii.rect.bottom < 100:
                # ii.y += 100
                # # print(self.y)
                #
                # ii.rect.y = ii.y
                bullets.remove(ii)
        # print(len(bullets)) 验证结果
    check_bullet_alien_collisions(pm, screen, ship, alines, bullets,data,sb)
    check_eat_high_buller(ship, change_buller, pm,data)

def ship_hit(pm,data,screen,ship,alines,bullets,sb):
   if data.ships_left>1:
        data.ships_left-=1
        sb.prep_ships()#更新记分牌
        ship.center_ship()
        sleep(0.5)

        #清空外星人和子弹列表
        alines.empty()
        bullets.empty()

        #创建新的外星人，并且把飞船放在屏幕中间
        creat_fleet(pm,screen,ship,alines)
        #ship.center_ship()

   else:

       pygame.mouse.set_visible(True)
       data.game_active=False



def check_aliens_bottom(pm,data,screen,ship,alines,bullets,sb):
    screen_rect=screen.get_rect()
    for aline in alines.sprites():
        if aline.rect.bottom>=screen_rect.bottom:
            ship_hit(pm,data,screen,ship,alines,bullets,sb)

def check_high_score(data,sb):
    if data.score>data.high_score:
        data.high_score=data.score
        #print("data.score=",data.score,"data.high_score=",data.high_score)
        sb.prep_high_score()   #多方准备，然后聚集一处 show_score   blit


