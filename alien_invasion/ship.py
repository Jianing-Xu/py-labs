import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船及其起始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 书中原本应该是加载一张飞船的bmp图像，鉴于没有附件素材，我们用蓝色矩形代替
        # self.image = pygame.image.load('images/ship.bmp')
        
        # 替代方案：在屏幕底部绘制一个蓝色的飞船（一个方块）
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255)) # 蓝色
        
        self.rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 因为 pygame.Rect 只支持整数，所以建立另外一个变量，存储小数值以便更平滑地移动
        self.x = float(self.rect.x)

        # 移动标志（按键按下为 True，松开为 False）
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 只有在标志为真，且没有到达屏幕右边缘时才移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 只有在标志为真，且没有到达屏幕左边缘时才移动
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
         """让飞船在屏幕底端居中"""
         self.rect.midbottom = self.screen_rect.midbottom
         self.x = float(self.rect.x)
