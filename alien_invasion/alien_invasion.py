import sys
from time import sleep # 用于在游戏重新开始前停顿

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的总体类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        
        # 初始化pygame模块以便运行
        pygame.init()
        # 初始化设置实例
        self.settings = Settings()

        # 创建显示窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵项目 (Python编程：从入门到实践)")

        # 创建一艘飞船对象
        self.ship = Ship(self)
        # 用群组(Group)存储由 Sprite 创造的对象，也就是多个子弹和外星人
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # 创建外星人群
        self._create_fleet()
        
        # 游戏状态标志位
        self.game_active = True

    def run_game(self):
        """开始游戏的主循环（事件循环）"""
        while True:
            # 始终侦听键盘或鼠标动作
            self._check_events()
            
            # 只有在活跃状态才更新逻辑，这样挂掉后就等于暂停
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            # 每次循环时都重绘屏幕并在最后刷新显示
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            # 玩家点击了窗口的关闭按钮 'X'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 玩家按下了某个键
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 玩家松开了某个键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key == pygame.K_RIGHT:          # 右箭头
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:         # 左箭头
            self.ship.moving_left = True
        elif event.key == pygame.K_q:            # 第 12 章最后：按 'q' 快速退出游戏
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:        # 空格发射子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应按键松开事件"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组 bullets 中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新所有被发射子弹的位置，并消除消失的子弹"""
        # 对编组使用 update() 将会自动调用其中每个元素的 update() 方法
        self.bullets.update()

        # 删除已消失的子弹（已经飞出屏幕顶端）以免消耗内存
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)
                 
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人的碰撞"""
        # pygame.sprite.groupcollide 检查是否有子弹和外星人重叠（发生碰撞）。第三、四个布尔参数决定是否从屏幕上移除这两个精灵
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        # 如果编组空了表明全部消灭，此时应清空子弹并生成一群新外星人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """检查是否有外星人到达边缘，并更新整群外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人是否跟飞船撞上了 (spritecollideany 返回碰撞到的第一个精灵实例，没撞上返回 None)
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 除了飞船，还要检查他们是否到达了屏幕底端
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 按照连飞船被撞到一起处理：损失一命
                self._ship_hit()
                break

    def _ship_hit(self):
        """响应飞船被外星人撞击或者外星人到底部"""
        if self.settings.ship_limit > 0:
            # 生命数减 1
            self.settings.ship_limit -= 1

            # 清空屏幕上残余的子弹和外星人
            self.aliens.empty()
            self.bullets.empty()

            # 重新创建外星人群，并将新飞船放在屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()

            # 短暂暂停以便玩家反应
            sleep(0.5)
        else:
            # 并没有更多命了，结束游戏状态
            self.game_active = False

    def _create_fleet(self):
        """创建外星人群。书中算法根据屏幕宽度和高度算出能装下多少行和列"""
        # 1. 创建一个外星人，计算并存储它需要的空间
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 两个外星人之间的水平间距设为外星人自身的宽度
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # 2. 计算可以容纳多少行
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # 3. 按行创建外星人
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行中"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # 设置他在 x 轴的位置
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        
        # 设置他在 y 轴的位置
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        
        # 最后，千万不要忘了把他加入精灵编组
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """如果有外星人到达边缘时的反馈动作"""
        for alien in self.aliens.sprites():
            # 只要有一个调用 check_edges() 为真了，说明这群大军撞墙了，应该转变方向
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """将整群外星人下移一片距离，然后并改变整体横向移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # -1 和 1 来回跳切
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新并绘制屏幕上的内容"""
        # 1. 每次重绘先敷上指定的背景色
        self.screen.fill(self.settings.bg_color)
        
        # 2. 把飞船绘制上去
        self.ship.blitme()
        
        # 3. 遍历编组里的所有子弹实例，因为子弹没有 image 对象，它是一个自画的 rect 矩形
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
             
        # 4. 这个内置方法不仅遍历编组成员，还把它里面每个成员各自的 image 画到他们相应的 rect 范围里
        self.aliens.draw(self.screen)

        # 5. 最后这一步非常关键：让最近绘制的整个屏幕可见（即把显存中的画面切到显示器上来）
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
