# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第十章：文件和异常
"""
import json

# 10-1 Python 学习笔记 (Learning Python)
# 读取整个文件。我们首先需要创建一个包含学习内容的文本文件。
print("10-1 Learning Python (Reading entire file):")
filename = 'learning_python.txt'

# 动态生成所需文件
with open(filename, 'w', encoding='utf-8') as f:
    f.write("In Python you can create classes.\n")
    f.write("In Python you can test conditions.\n")
    f.write("In Python you can read data from files.\n")

# reading entire file
with open(filename) as f: # 打开文件。'with' 会在不再需要访问文件后将其自动关闭。
    contents = f.read() # 读取全部内容
print(contents)

# 逐行读取并在循环中处理
print("\nReading line by line:")
with open(filename) as f:
    for line in f:
        # rstrip() 用来消除文件中每行末尾不可见的换行符，以及 print 自动加上的换行符。
        print(line.rstrip())

# 在 with 代码块外面也可以访问读取出来的内容：
print("\nReading within a list:")
with open(filename) as f:
    # readlines() 从文件中读取每一行并存放到一个列表中。
    lines = f.readlines()

for line in lines:
    print(line.rstrip())


# 10-2 C语言学习笔记 (Learning C)
# 字符串替换。使用 replace() 方法将字符串中特定的单词替换为另一个。
print("\n10-2 Learning C:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # 将原本的 'In Python' 替换为了 'In C'
    # 注意，replace 并不修改原始字符串本身，而是返回一个修改好的新副本。
    modified_line = line.rstrip().replace('Python', 'C')
    print(modified_line)


# 10-3 访客 (Guest)
# 写入文件。
print("\n10-3 Guest:")
name = "Eric" # 模拟 input("Please enter your name: ")
output_filename = 'guest.txt'

# 使用 'w' 模式写入文件，如果文件不存在会自动创建。如果文件已存在它会先被清空 (覆盖)！
with open(output_filename, 'w') as f:
    f.write(name)
print(f"I wrote '{name}' to {output_filename}.")


# 10-4 访客名单 (Guest Book)
# 附件到文件末尾。
print("\n10-4 Guest Book:")
output_filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
# 模拟用户连续输入，这里我们直接给一个列表
names = ['willie', 'jane', 'mikael'] 

# 使用 'a' 模式（附加模式），新写入的内容将被添加到文件已有的内容之后
with open(output_filename, 'a') as f:
    for name in names:
        # 加上换行符，确保每个访客占一行
        f.write(f"{name.title()}\n")
print(f"Added names to {output_filename}.")


# 10-5 编程调查 (Programming Poll)
# 类似于 10-4，不过内容更换为了编程的理由。
print("\n10-5 Programming Poll:")
output_filename = 'programming_poll.txt'

responses = [
    'I like finding solutions.',
    'It helps me automate tasks.',
]

with open(output_filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
print(f"Wrote responses to {output_filename}.")


# 10-6 加法运算 (Addition)
# 异常处理：处理 ValueError 异常。
print("\n10-6 Addition:")
# 模拟用户输入
num_1 = "10" 
num_2 = "cat" # 这是一个不是数字的字符串

try:
    # 尝试执行可能会引发错误的代码
    answer = int(num_1) + int(num_2)
except ValueError:
    # 如果发生 ValueError (比如尝试转换 'cat' 为 int)，执行这里
    print("Sorry, I really needed a number.")
else:
    # 只要 try 块里代码执行成功，即没有报异常，就会执行 else
    print(answer)


# 10-8 猫和狗 (Cats and Dogs)
# 异常处理：处理 FileNotFoundError。
print("\n10-8 Cats and Dogs:")
filenames = ['cats.txt', 'dogs.txt']

# 为了演示，我们先创建一个文件 cats.txt，但是不建 dogs.txt
with open('cats.txt', 'w') as f:
    f.write("tom\n")
    f.write("luna\n")
    f.write("simba\n")

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
         with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        # 找不到文件时报错
        print(f"Sorry, the file {filename} does not exist.")


# 10-9 沉默的猫和狗 (Silent Cats and Dogs)
# 异常处理：除了使用 pass 让其静默失败。
print("\n10-9 Silent Cats and Dogs:")
for filename in filenames:
    try:
         with open(filename) as f:
            print(f"Successfully read {filename}")
    except FileNotFoundError:
        # pass 相当于一个占位符，作用是什么都不做，这样即不报错，也不中断执行
        pass


# 10-10 常见单词 (Common Words)
# 使用 count() 方法分析文本。
print("\n10-10 Common Words:")
line = "Row, row, row your boat"
# 统计文本中 'row' 出现的次数，区分大小写
print("Count of 'row':", line.count('row'))
# 转换为小写后再统计，得到更准确的全部次数
print("Count of 'row' (case-insensitive):", line.lower().count('row'))


# 10-11 喜欢的数字 (Favorite Number)
# 存储数据：使用 json 模块将数据保存到文件中。
print("\n10-11 Favorite Number:")
# json 模块允许你转储 (dump) 简单的数据结构到文件，并在程序再运行时加载 (load) 这些数据
favorite_number = 42 # 获取到的值
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f) # 写入 JSON 文件
    print(f"I dumped your favorite number: {favorite_number}")

# 加载数据。可以写在另一个程序或本次重新获取。
with open(filename) as f:
    number = json.load(f) # 从 JSON 文件读取内容
print(f"Loaded: I know your favorite number! It's {number}.")


# 10-13 验证用户 (Verify User)
# 一个非常常用的重构实践，综合了异常和数据存储。如果你经常写相似代码，也可以考虑将其提取进函数。
print("\n10-13 Verify User:")
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        # 返回 None 是表示数据不存在的良好习惯
        return None 
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = "Jaden" # 模拟 input()
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    # 如果已经有数据了，就继续（本例中并没有真正交互判断）
    if username:
       # 这里可以通过 input(f"Are you {username}? (y/n)") 加入更多验证逻辑
       print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# 首先创建一个没包含名字的场景
greet_user() # 触发 get_new_username
greet_user() # 文件有内容了，能够欢迎回来
