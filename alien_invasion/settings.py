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
        self.ship_speed = 1

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
