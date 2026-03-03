from random import choice

class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步都统一始于坐标 (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        # 不断漫步，直到点数达到设定的 num_points 为止
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            # -1 为向左走，1为向右走
            x_direction = choice([1, -1])
            # 随机走 1 到 4 步或者不走(0)
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 如果横坐标和纵坐标的步长都为0（原地踏步），则拒绝将其加入结果中
            if x_step == 0 and y_step == 0:
                continue

            # 每个新位置的新 x, y 坐标都等于前一个点的坐标加上横纵增量
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 将算出来的新位置添加到列表中
            self.x_values.append(x)
            self.y_values.append(y)
