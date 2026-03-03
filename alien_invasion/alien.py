import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 这里原本应该加载一张外星人图片，为了保证您的机器上不用配置图片也能运行，我们用一个绿色矩形代替
        # self.image = pygame.image.load('images/alien.bmp')
        
        # 替代方案：绘制一个绿色的正方形作为外星人
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0)) # 绿色
        
        # 获取外星人的包围矩形 rect 属性
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回 True"""
        screen_rect = self.screen.get_rect()
        # 右侧超出或者左侧小于等于0
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        # 利用 settings 的方向乘以速度，更新外星人的 x 坐标
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
