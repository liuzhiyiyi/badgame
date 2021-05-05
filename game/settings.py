
class Setting:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(148,41,90)
        self.ship_speed=10
        self.bullet_speed=5
        self.bullet_width=20
        self.bullet_height=15
        self.bullet_color=211,211,211
        self.bullet_allowed=20
        self.alien_speed=5
        self.fleet_drop_speed=50  #下落速度
        self.fleet_direction=-1  #控制方向，-1就为反方向
        self.ship_limit=3
        self.speedup_scale=2
        self.initialize_dynamic_setting()
        self.aline_points=5
        self.score_scale=2
        #特效子弹补给包的速度
        self.super_bullet_speed_out=1
        self.super_bullet_speed_in=10

    def initialize_dynamic_setting(self):  #check_play_button
        self.ship_speed=5
        self.bullet_speed=5
        self.alien_speed=1
        self.fleet_direction=1

    def increase_speed(self):  #check_bullet_alien_collisions
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.aline_points=int(self.aline_points*self.score_scale)

