# -*- coding = utf-8 -*-
# @Software: Pycharm

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()      #初始化背景设置
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1011, 674))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监视键盘和鼠标事件，为程序响应事件编写事件循环
            for event in pygame.event.get():
                # pygame.event.get()返回一个列表，包含其上一次被调用后发生的所有事件
                if event.type == pygame.QUIT:
                    sys.exit()            #退出游戏

            # 每次循环时都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()















