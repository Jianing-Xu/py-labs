# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
外星人入侵项目 - 配置文件
"""

class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # 浅灰色背景
        
        # 飞船设置
        self.ship_speed = 1.5 # 飞船移动速度
        self.ship_limit = 3   # 飞船命数
        
        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # 深灰色子弹
        self.bullets_allowed = 3 # 限制屏幕上同时存在的子弹数量
        
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # 外星人撞到边缘时向下移动的速度
        
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1 
