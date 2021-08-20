# -*- coding = utf-8 -*-
# @Software: Pycharm

import sys

import pygame

from settings import Settings

class Ship:
    '''管理飞船的类'''

    def __init__(self, ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放置在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()      #初始化背景设置
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监视键盘和鼠标事件，为程序响应事件编写事件循环
            for event in pygame.event.get():
                # pygame.event.get()返回一个列表，包含其上一次被调用后发生的所有事件
                if event.type == pygame.QUIT:
                    sys.exit()            #退出游戏

            # 每次循环时都重新用背景色填充屏幕
            self.screen.fill(self.settings.bg_color)

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()















