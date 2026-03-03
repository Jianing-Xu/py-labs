import matplotlib.pyplot as plt

# 准备想要可视化的数据
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 使用内置样式
# 可以通过 plt.style.available 查看所有可用样式
plt.style.use('seaborn-v0_8') 

# plt.subplots() 是一个可在同一张图中生成一张或多张图表的函数
# fig 表示整张图片，ax 表示图片中的各个图表
fig, ax = plt.subplots()

# .plot() 会尝试根据给定的数据绘制出有意义的折线图
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Squares of Numbers (Matplotlib)", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 使用 plt.show() 打开查看器并显示绘制的图表
plt.show()

# ---
# 或者，如果您想要直接保存为文件而不是弹窗，可以使用：
# plt.savefig('squares_plot.png', bbox_inches='tight')
