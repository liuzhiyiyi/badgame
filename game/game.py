import pygame, sys
from settings import Setting
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group
from aline import Aline
from random import randint
from game_data import Game_data
from button import Button
from score_board import Scoreboard
from high_energy_bullet import Highbullet



def run_game():  #实验机记录
    pygame.init()
    pm=Setting()  #参数实例  设置的屏幕参数导进来
    screen=pygame.display.set_mode((pm.screen_width,pm.screen_height)) #整个游戏窗口 也是一个surface

    pygame.display.set_caption("Alien Invasion")
    play_button=Button(pm,screen,"Play")

    ship=Ship(screen,pm)# 飞船实例
    # bg_color=(122,211,44)  # 范围0-255
    bullets=Group()#创建一个存储子弹的编组  管理所有的子弹
    alines = Group()
    print(alines)

    data=Game_data(pm)
    sb=Scoreboard(pm,screen,data)
    gf.creat_fleet(pm, screen, ship, alines) #创建外星人群

    super_bullers=Group()

    gf.creat_superbullers(pm, screen,super_bullers)





    while True:
        gf.check_events(ship,screen,bullets,data, play_button,pm,alines,sb)
        # ship.update()
        # bullets.update()

        gf.update_screen(pm, screen, data, ship, bullets, alines, play_button,sb,super_bullers)

        if data.game_active:


                # ship.update()
                #
                # bullets.update()   #自动对每个精灵(属于bullet)调用bullet.update
                ship.update()
                bullets.update()
                super_bullers.update()

                # gf.delete(bullets)

                gf.update_bullets(pm,screen,ship,alines,bullets,data,sb,super_bullers)
                gf.update_alines(pm,data,ship,screen,alines,bullets,sb)
                gf.update_superbullet(super_bullers, pm)
               # gf.update_screen(pm, screen,data, ship, bullets, alines,play_button)
        # else:
        #    pygame.display.set_caption("Game over")

           #break




run_game()


