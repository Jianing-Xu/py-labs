# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第四章：操作列表
"""

# 4-1 比萨 (Pizzas)
# 想出至少三种喜欢的比萨，将其名称存储在一个列表中，再使用 for 循环将每种比萨打印出来。
pizzas = ["pepperoni", "margherita", "hawaiian"]
for pizza in pizzas:
    # 打印包含比萨名称的完整句子
    print(f"I like {pizza} pizza.")
# for 循环结束后（没有缩进的代码）
print("I really love pizza!\n")

# 4-2 动物 (Animals)
# 找出至少三种有共同特征的动物，将它们存入列表中，再用 for 循环打印每个动物的名字。
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# 4-3 数到20 (Counting to Twenty)
# 使用一个 for 循环打印数 1 到 20。
# range(1, 21) 生成从 1 开始到 20 结束的数字（不包含 21）
print("4-3 Counting to 20:")
for num in range(1, 21):
    print(num, end=" ")  # 使用 end=" " 避免每次打印换行
print("\n")

# 4-4 一百万 (One Million)
# 创建一个包含数 1 到 1000000 的列表。
# numbers = list(range(1, 1000001)) # 出于演示简洁暂不打印

# 4-5 一百万求和 (Summing a Million)
# 使用 min() 和 max() 检查列表是否确实包含 1 到 1000000，再调用 sum() 函数。
numbers = list(range(1, 1000001))
print("4-5 Min, Max, and Sum:")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")  # 快速求和
print()

# 4-6 奇数 (Odd Numbers)
# 通过给 range() 的第三个参数指定步长为 2，创建一个包含 1 到 20 所有奇数的列表。
print("4-6 Odd Numbers:")
odd_numbers = list(range(1, 21, 2))
for num in odd_numbers:
    print(num, end=" ")
print("\n")

# 4-7 3的倍数 (Threes)
# 创建一个列表，其中包含 3 到 30 内能被 3 整除的数，再打印。
print("4-7 Threes:")
threes = list(range(3, 31, 3))
for num in threes:
    print(num, end=" ")
print("\n")

# 4-8 立方 (Cubes)
# 创建一个列表，包含 1 到 10 的立方（即该数的 3 次方），并打印出来。
# （此处使用传统 for 循环和 append）
print("4-8 Cubes:")
cubes = []
for value in range(1, 11):
    cube = value ** 3  # ** 是Python中的乘方运算符
    cubes.append(cube)
for cube in cubes:
    print(cube, end=" ")
print("\n")

# 4-9 立方解析 (Cube Comprehension)
# 使用列表解析 (List Comprehension) 生成 1 到 10 的立方。
# 语法结构：[表达式 for 变量 in 可迭代对象]
print("4-9 Cube Comprehension:")
cubes_short = [value**3 for value in range(1, 11)]
print(cubes_short)
print()

# 4-10 切片 (Slices)
# 打印列表的切片。
# 切片语法：list[起始索引:结束索引]，同样是不包含结束索引。
print("4-10 Slices:")
items = ["apple", "banana", "cherry", "date", "elderberry"]
print("The first three items in the list are:")
print(items[:3])  # 从头开始切片，到索引 3 之前

print("Three items from the middle of the list are:")
print(items[1:4]) # 从索引 1 开始，到索引 4 之前

print("The last three items in the list are:")
print(items[-3:]) # -3 表示倒数第三个元素，一直切片到末尾
print()

# 4-11 你的比萨和我的比萨 (My Pizzas, Your Pizzas)
# 复制列表，并证明是两个独立的列表。
print("4-11 My Pizzas, Your Pizzas:")
my_pizzas = ["pepperoni", "margherita", "hawaiian"]
# [:] 用于创建列表的副本。如果直接 friend_pizzas = my_pizzas，两个变量将指向同一个列表。
friend_pizzas = my_pizzas[:] 

my_pizzas.append("meat lover")     # 在我的比萨列表末尾添加
friend_pizzas.append("vegetarian") # 在朋友的比萨列表末尾添加

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza, end=" ")
print()

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza, end=" ")
print("\n")

# 4-13 自助餐 (Buffet)
# 使用元组 (Tuple) 而不是列表来存储不能修改的系列。
print("4-13 Buffet:")
# 元组使用圆括号 ()，列表使用方括号 []
foods = ("steak", "salad", "pizza", "sushi", "soup")
print("Original menu:")
for food in foods:
    print(food)

# 尝试修改元组元素会报错： TypeError: 'tuple' object does not support item assignment
# foods[0] = "burger"

# 覆盖整个元组变量是允许的
print("\nModified menu:")
foods = ("burger", "salad", "pizza", "ice cream", "soup")
for food in foods:
    print(food)
