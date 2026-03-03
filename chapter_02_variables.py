# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第二章：变量和简单数据类型
"""

# 2-1 简单消息 (Simple Message)
# 将一条消息分配给变量，然后将其打印出来。
message = "Hello, Python Crash Course World!"
print(message)  # 打印变量时不需要加引号

# 2-2 多条简单消息 (Simple Messages)
# 将一条消息分配给变量，将其打印出来；然后将变量的值修改为一条新消息，再将其打印出来。
message = "Hello again, exploring Python is fun!"
print(message)

# 2-3 个性化消息 (Personal Message)
# 让用户将一个用户的姓名存入变量，并向该用户显示一条消息。
name = "Eric"
# 使用 f-string (格式化字符串字面量) 来插入变量的值，这是Python 3.6引入的便捷语法
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4 调整名字的大小写 (Name Cases)
# 将一个人名存入变量，然后以小写、大写和首字母大写的方式显示出来。
name = "ada lovelace"
print(name.lower())  # 转换为全小写
print(name.upper())  # 转换为全大写
print(name.title())  # 每个单词的首字母大写

# 2-5 名言 (Famous Quote)
# 找一句你钦佩的名人说的名言，将姓名和名言打印出来。
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# 2-6 名言2 (Famous Quote 2)
# 重复练习2-5，但将名人的姓名存储在变量famous_person中，再创建要显示的消息存入message变量。
famous_person = "Albert Einstein"
# 在f-string中同时使用单双引号来处理名言中的引号
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# 2-7 剔除人名中的空白 (Stripping Names)
# 用变量表示人名，并在其开头末尾包含一些空白字符，如 "\t" (制表符) 和 "\n" (换行符)。
# 然后依次展示 lstrip(), rstrip() 和 strip() 对字符串的影响。
name = "\t\n  Ada Lovelace  \n\t"
print("Original:")
print(name)

print("\nlstrip() - 移除左侧空白:")
print(name.lstrip())

print("\nrstrip() - 移除右侧空白:")
print(name.rstrip())

print("\nstrip() - 移除两侧空白:")
print(name.strip())

# 2-8 数字8 (Number Eight)
# 编写4个表达式，分别使用加、减、乘、除运算，且结果均为 8。
print(5 + 3)
print(11 - 3)
print(4 * 2)
# 注意：在Python 3中，除法 (/) 的结果总是浮点数 (float)。
print(16 / 2) 

# 2-9 最喜欢的数字 (Favorite Number)
# 将最喜欢的数字存入变量，再使用这个变量创建一条消息。
favorite_number = 42
message = f"My favorite number is {favorite_number}."
print(message)

# 2-10 添加注释 (Adding Comments)
# 已经在这个文件中加了注释 :)
