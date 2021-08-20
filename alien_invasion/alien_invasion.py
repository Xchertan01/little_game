# -*- coding = utf-8 -*-
# @Software: Pycharm

import sys

import pygame

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()      #初始化背景设置

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        #设置背景色
        self.bg_color = (230, 230, 230)       #设置RBG值

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监视键盘和鼠标事件，为程序响应事件编写事件循环
            for event in pygame.event.get():
                # pygame.event.get()返回一个列表，包含其上一次被调用后发生的所有事件
                if event.type == pygame.QUIT:
                    sys.exit()            #退出游戏

            # 每次循环时都重新用背景色填充屏幕
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()















