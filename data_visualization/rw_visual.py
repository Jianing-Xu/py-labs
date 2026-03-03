import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 如果这段代码没有加上 while 循环，那么将只生成一张图后退出。
print("Data Visualization - Random Walk")
print("(Close the window to stop the program)")

# 创建一个 RandomWalk 实例。可以改变里面传入的点数，比如 50_000 看效果。
rw = RandomWalk(50_000)
rw.fill_walk()

# 将所有的点绘制出来
plt.style.use('classic')

# figsize 参数可用来指定图表的尺寸和分辨率（这里的宽长比例适合大多数电脑屏幕）
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

# 像 scatter_squares 中一样，使用颜色映射 cmap 来显示每一点行走的先后顺序
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=2) # 去掉边缘颜色('none')，点更小

# 突出显示漫步最重要的两点：起点和终点，以便很容易区分
# 终点涂红加大
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=40)
# 起点涂绿加大
ax.scatter(0, 0, c='green', edgecolors='none', s=40)

# 最后，在展现这幅“抽象画”前，隐藏没必要显示出来的坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
