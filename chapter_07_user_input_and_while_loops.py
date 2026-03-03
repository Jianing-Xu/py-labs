# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第七章：用户输入和 while 循环
"""

# 7-1 汽车租赁 (Rental Car)
# 询问用户要租赁什么样的汽车，然后打印一条消息，如 "Let me see if I can find you a Subaru"。
print("7-1 Rental Car:")
# input() 函数会暂停程序运行，等待用户输入一些文本。获取的值都是字符串 (str)
car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car.title()}.\n")

# 7-2 餐馆订位 (Restaurant Seating)
# 询问用户有多少人用餐。如果人数超过 8，就打印一条消息，指出没有空桌；否则告诉用户有空桌。
print("7-2 Restaurant Seating:")
party_size = input("How many people are in your dinner party? ")
# 使用 int() 函数将用户输入的字符串表示转换为数值以便进行数值比较
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
print()

# 7-3 10的整数倍 (Multiples of Ten)
# 让用户输入一个数字，然后使用求模运算符 (%) 判断它是否是 10 的整数倍。
print("7-3 Multiples of Ten:")
number = input("Give me a number, please: ")
number = int(number)

# % 是一个求余运算，如果余数为 0 表示能被整除
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
print()

# 7-4 比萨配料 (Pizza Toppings)
# 编写一个循环，提示用户输入要求的比萨配料，直输入 'quit' 为止。
print("7-4 Pizza Toppings:")
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.) "

# 使用 while 循环让程序不断运行，直到遭遇 break 语句
while True:
    topping = input(prompt)
    if topping == 'quit':
        # 输入 quit，则执行 break 退出所在的 while 循环 (如果是嵌套的，只退出这一层循环)
        break
    else:
        print(f"  I'll add {topping} to your pizza.")

# 7-5 电影票 (Movie Tickets)
# 根据不同的年龄收取不同的票价：3 岁以下免费；3~12岁 10 美元；12岁（不含）以上 15 美元。
print("\n7-5 Movie Tickets:")
prompt = "How old are you?"
prompt += "\n(Enter 'quit' when you are finished.) "

# 这是另一种控制 while 循环的方法：使用标志 (flag) 变量 active
active = True
while active:
    age = input(prompt)
    # 首先检查是否输入了 quit
    if age == 'quit':
        active = False
    else:
        # 如果不是 quit，将其转换为整数再判断票价级别
        age = int(age)
        
        if age < 3:
            print("  Your ticket is free!")
        elif age <= 12: # age >= 3 这一条件已经被包含，不需要重复写
            print("  Your ticket is $10.")
        else:
            print("  Your ticket is $15.")

# 7-7 无限循环 (Infinity)
# 这是一个经典的无限循环，如果运行了该程序，用户需要按 Ctrl-C 退出。
# 为了避免整个程序卡死，此处使用注释将其取消激活。
# print("\n7-7 Infinity:")
# while True:
#     print("This loop will never end!")

# 7-8 熟食店 (Deli)
# 创建一个代表各种三明治的列表 sandwiches_orders，和一个名为 finished_sandwiches 的空列表。
print("\n7-8 Deli:")
sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I made your tuna sandwich")

# 7-9 五香烟熏牛肉卖完了 (No Pastrami)
# 使用 7-8 里的列表并使用 while 循环将所有的 'pastrami' 删除。
print("\n7-9 No Pastrami:")
print("Sorry, we're all out of pastrami today.")
# 使用 while 循环和 in() 函数删掉特定值列表中的*所有*重复项。如果这使用 for 并不是最好的选择
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 将仍然在 sandwich_orders 中的三明治循环移到 finished_sandwiches 中
while sandwich_orders:
    # pop() 默认移除最末尾元素并返回该元素的值
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    # 将刚取出的三明治放入空列表
    finished_sandwiches.append(current_sandwich)

print("\n")
# 显示制作好的三明治
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")

# 7-10 梦想的度假胜地 (Dream Vacation)
# 类似民意调查的循环机制。
print("\n7-10 Dream Vacation:")
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# 将调查结果存入字典
responses = {}

while True:
    # 请求用户输入姓名和地点
    name = input(name_prompt)
    place = input(place_prompt)
    
    # 存入字典
    responses[name] = place
    
    # 获取其他人的意向
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break  # 如果不是 yes，则结束循环

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
