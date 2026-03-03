import matplotlib.pyplot as plt

# 生成更大的数据集，使用循环自动计算 1000 个点的平方值
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# ax.scatter() 专门用来绘制散点图
# c 参数使用颜色映射 cmap (Colormap)。这里 'Blues' 表示根据 y_values 的值，颜色由浅蓝过渡到深蓝。
# s 参数设置点的大小
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("Scatter Plot (Squares)", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

plt.show()
