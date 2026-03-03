# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第三章：列表简介
"""

# 3-1 姓名 (Names)
# 将几个朋友的姓名存入一个列表，依次访问并打印每个人的姓名，以显示列表内容。
names = ["Alice", "Bob", "Charlie"]
print("3-1 Names:")
print(names[0])  # 列表的索引从0开始，0代表第一个元素
print(names[1])
print(names[2])

# 3-2 问候语 (Greetings)
# 继续使用3-1中的列表，但为他们每人打印一条相同的问候语。
print("\n3-2 Greetings:")
# 使用f-string来格式化字符串，将列表元素直接镶嵌进去
print(f"Hello {names[0]}, nice to meet you!")
print(f"Hello {names[1]}, nice to meet you!")
print(f"Hello {names[2]}, nice to meet you!")

# 3-3 自己的列表 (Your Own List)
# 创建一个包含各种交通方式的列表，并打印一些宣言。
transportations = ["Honda motorcycle", "BMW car", "Giant bicycle"]
print("\n3-3 Your Own List:")
print(f"I would like to own a {transportations[0]}.")
print(f"Driving a {transportations[1]} is cool.")

# 3-4 嘉宾名单 (Guest List)
# 邀请几个人共进晚餐，存入列表，向每人打印邀请函。
guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print("\n3-4 Guest List:")
print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")

# 3-5 修改嘉宾名单 (Changing Guest List)
# 其中一位无法赴约，需要替换。
print("\n3-5 Changing Guest List:")
cannot_attend = "Isaac Newton"
print(f"Unfortunately, {cannot_attend} cannot make it to the dinner.")

# 使用 remove() 移除特定元素，或者根据索引进行修改：
# guests[2] = "Niels Bohr"
# 这里演示先移除再追加
guests.remove(cannot_attend)
guests.append("Niels Bohr")

# 重新发出邀请
print(f"Dear {guests[0]}, you are still invited.")
print(f"Dear {guests[1]}, you are still invited.")
print(f"Dear {guests[2]}, welcome to my dinner!")

# 3-6 添加嘉宾 (More Guests)
# 找到了一个更大的餐桌，可以邀请更多人。
print("\n3-6 More Guests:")
print("Good news! We found a bigger dinner table!")
# 使用 insert() 将元素插入到列表中的特定位置
guests.insert(0, "Galileo Galilei")  # 在开头插入
guests.insert(2, "Richard Feynman")  # 在中间插入
guests.append("Stephen Hawking")     # 使用 append() 在末尾附加

for guest in guests:
    print(f"Dear {guest}, please join my dinner party.")

# 3-7 缩减名单 (Shrinking Guest List)
# 大餐桌无法及时送达，只能邀请两位嘉宾。
print("\n3-7 Shrinking Guest List:")
print("Oh no, the table won't arrive in time, so I can only invite two people.")

# 使用 pop() 移除列表末尾的元素，并将其弹出（这样还能使用弹出的元素）
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"Sorry {popped_guest}, I can't invite you to dinner this time.")

for guest in guests:
    print(f"Dear {guest}, you're still on the guest list. See you soon!")

# 使用 del 语句删除最后两位嘉宾，清空列表
del guests[1]
del guests[0]
print(f"Final guest list:", guests)  # 列表应该为空 []

# 3-8 放眼世界 (Seeing the World)
# 将想去的地方存入列表。
print("\n3-8 Seeing the World:")
places = ["Tokyo", "Paris", "New York", "London", "Sydney"]
print("Original list:", places)

# 使用 sorted() 对列表进行临时排序（不改变原列表的内容或顺序）
print("Sorted alphabetically:", sorted(places))
print("Original list again:", places)

# 再次使用 sorted()，加上 reverse=True 参数进行反向字母排序
print("Sorted reverse alphabetically:", sorted(places, reverse=True))
print("Original list again:", places)

# 使用 reverse() 永久性反转列表顺序
places.reverse()
print("Reversed list:", places)

# 再次使用 reverse() 会将列表恢复到原始顺序
places.reverse()
print("Reversed again (back to original):", places)

# 使用 sort() 永久性按字母顺序排列列表
places.sort()
print("Sorted permanently:", places)

# 使用 sort(reverse=True) 永久性按反向字母顺序排列
places.sort(reverse=True)
print("Sorted permanently in reverse:", places)
