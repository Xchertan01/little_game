# -*- coding = utf-8 -*-
# @Software: Pycharm

class Settings:
    '''存储游戏 alien invasion 中所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1011
        self.screen_height = 674
        self.bg_color = (230, 230, 230)

        #飞船设置
        self.ship_speed = 0.9
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 1.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3         #使屏幕上最多只能出现3颗子弹

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 0.9
        self.bullet_speed = 1.3
        self.alien_speed = 1.0

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
