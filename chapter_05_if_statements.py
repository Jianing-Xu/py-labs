# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第五章：if 语句
"""

# 5-1 条件测试 (Conditional Tests)
# 编写一系列如果…否则…条件的测试，先写明预测结果，再输出实际结果。
car = 'subaru'
print("5-1 Conditional Tests:")
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') # 这里等于运算符 == 检查两个值是否相等

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')   # 由于不等于，所以返回 False

# 5-2 更多条件测试 (More Conditional Tests)
# 使用不同类型的比较。包括字符串、大小写、数字比较和多个条件的组合。
string1 = "Hello"
string2 = "hello"

# 检查字符串相等和不相等
print("\n5-2 More Conditional Tests:")
print("string1 == string2?", string1 == string2)
print("string1 != string2?", string1 != string2)

# 使用 lower() 进行不区分大小写的比较
print("string1.lower() == string2?", string1.lower() == string2)

# 数字比较和逻辑运算符 (and, or)
age_0 = 22
age_1 = 18
print("age_0 >= 21 and age_1 >= 21 ?", (age_0 >= 21) and (age_1 >= 21)) # 必须两者都为真
print("age_0 >= 21 or age_1 >= 21 ?", (age_0 >= 21) or (age_1 >= 21))   # 其中一个为真即可

# 测试特定的值是否包含在列表中 (in 关键字)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

# 5-3 外星人颜色 1 (Alien Colors #1)
# 想象有一个可以在游戏中击落的外星人。如果它是绿色的，玩家得 5 分。
print("\n5-3 Alien Colors #1:")
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

# 这个版本的外星人颜色不符合 if 语句，将不会有任何输出
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

# 5-4 外星人颜色 2 (Alien Colors #2)
# 使用 if-else 结构处理两种情况，如果是绿色的得 5 分，否则得 10 分。
print("\n5-4 Alien Colors #2:")
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!") # 这条会被执行

# 5-5 外星人颜色 3 (Alien Colors #3)
# 分为绿、黄、红三种不同的条件，使用 if-elif-else 结构。
print("\n5-5 Alien Colors #3:")
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == 'yellow':     # elif 可以有多个连续的块
    print("You earned 10 points.")
else:                             # else 是最后一个默认选项（可以省略）
    print("You earned 15 points.") # 这条会被执行

# 5-6 人生的不同阶段 (Stages of Life)
# 设置一个变量 age，然后根据年龄打印出他是婴儿、蹒跚学步、儿童、青少年、成年还是老年。
print("\n5-6 Stages of Life:")
age = 65
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# 5-7 喜欢的水果 (Favorite Fruit)
# 创建一个列表，包含你喜欢的水果，然后编写 5 条独立的 if 语句检查某种水果是否在列表中。
print("\n5-7 Favorite Fruit:")
favorite_fruits = ['apples', 'bananas', 'mangoes']
# 这里之所以用多个无关的 if，是因为可能需要触发多条逻辑分支，而不是像 elif 互斥
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!") # 不会被执行

# 5-8 招呼管理员 (Hello Admin)
# 遍历列表，如果用户名是 'admin' 就打印特殊问候语，否则打印普通问候语。
print("\n5-8 Hello Admin:")
usernames = ['admin', 'jaden', 'eric', 'alice', 'bob']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9 处理没有用户的情形 (No Users)
# 检查列表是否为空，空列表作为 bool 值进行判断时会返回 False。
print("\n5-9 No Users:")
usernames = [] # 清空用户列表
# 测试列表是否有元素
if usernames:  # 在 Python 中，非空列表在判断真假时为 True，空列表为 False
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!") # 因为列表为空，这条将被执行

# 5-10 检查用户名 (Checking Usernames)
# 网站模拟：区分哪些用户名已被占用（模拟注册功能，并且大小写不敏感）。
print("\n5-10 Checking Usernames:")
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

# 为确保不区分大小写，先将 current_users 的元素全部转换为小写
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # 检查小写版本的 new_user 是否存在于列表 current_users_lower
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

# 5-11 序数 (Ordinal Numbers)
# 遍历 1 到 9 的列表。并打印各个数字对应的序数，例如 1st, 2nd, 3rd, 4th。
print("\n5-11 Ordinal Numbers:")
numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")
