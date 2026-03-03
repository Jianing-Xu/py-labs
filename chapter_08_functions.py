# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第八章：函数
"""

# 8-1 消息 (Message)
# 定义一个打印消息的简单函数。
print("8-1 Message:")
def display_message():
    """打印本章学习主题的一条消息"""
    print("I'm learning about functions in this chapter!")

# 调用函数
display_message()

# 8-2 喜欢的图书 (Favorite Book)
# 带有形参（实参）的函数。
print("\n8-2 Favorite Book:")
def favorite_book(title):
    """显示一条包含书名的消息"""
    print(f"One of my favorite books is {title.title()}.")

# 将 'Alice in Wonderland' 作为实参传递给 name='title'
favorite_book('Alice in Wonderland')

# 8-3 T恤 (T-Shirt)
# 带有多个形参的函数。这展示了位置实参和关键字实参的用法。
print("\n8-3 T-Shirt:")
def make_shirt(size, message):
    """显示制作的T恤的尺码和字样"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

# 使用位置实参调用函数
make_shirt('large', 'I love Python!')
# 使用关键字实参调用函数
make_shirt(message='Readability counts.', size='medium')

# 8-4 大号 T恤 (Large Shirts)
# 给参数设置默认值。
print("\n8-4 Large Shirts:")
def make_shirt(size='large', message='I love Python!'): # 重写函数以添加默认值
    """显示带默认值的T恤的尺码和字样"""
    print(f"\nI'm making a {size} t-shirt.")
    print(f'It says, "{message}"')

# 调用该函数，创建一个保持默认大小的 'large' 号T恤
make_shirt()
# 创建印有默认字样的 'medium' 号T恤
make_shirt(size='medium')
# 创建 'small' 号并且印有其他字样的T恤
make_shirt('small', 'Programmers are loopy.')

# 8-5 城市 (Cities)
# 返回简单值的函数。
print("\n8-5 Cities:")
def describe_city(city, country='chile'): # 有默认值的形参必须放在末尾
    """描述一个城市"""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

# 8-6 城市名 (City Names)
# 函数可以通过 return 语句将值返回给调用它的代码。
print("\n8-6 City Names:")
def city_country(city, country): # 该函数不再直接 print()，而是返回字符串
    """返回如 'Santiago, Chile' 这样的字符串格式"""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)
print(city_country('ushuaia', 'argentina'))
print(city_country('longyearbyen', 'svalbard'))

# 8-7 专辑 (Album)
# 建立一个返回字典的函数。
print("\n8-7 Album:")
def make_album(artist, title, tracks=None): # tracks 是一个可选形参（通常设为 None）
    """创建一个包含专辑信息的字典"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    # 如果用户传入了 tracks 参数（不是 None），将其加入字典中
    if tracks:
        album_dict['tracks'] = tracks
        
    return album_dict # 把建好的字典返回出去

album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks=8) 
print(album) # 这次打印包括了音轨数

# 8-9 魔术师 (Magicians)
# 传递列表给函数，在函数内部遍历并修改。
print("\n8-9 Magicians:")
def show_magicians(magicians):
    """打印传入列表中每个魔术师的名字"""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

# 8-10 了不起的魔术师 (Great Magicians) # 注意：这里修改了原有列表
print("\n8-10 Great Magicians:")
def make_great(magicians):
    """在每个魔术师之前加入字样 'the Great'。返回修改后的列表"""
    # 建一个空列表来装新名字
    great_magicians = []
    
    # 只要原列表中还有人，就弹出来修改
    while magicians:
        magician = magicians.pop()
        great_magician = f"{magician} the Great"
        great_magicians.append(great_magician)
        
    # 把加入了 the Great 的新名字放回原本空了的列表中
    for great_magician in great_magicians:
        magicians.append(great_magician)

# 注意：这将永久修改原列表 magicians
make_great(magicians)
show_magicians(magicians) # 返回带有 the Great 的名字

# 8-11 不变的魔术师 (Unchanged Magicians)
# 这个练习的目的在于避免修改原始列表，通过传递副本的方式。
print("\n8-11 Unchanged Magicians:")
# 我们通过切片 [:] 传递 magicians 列表的一个副本。
magicians = ['harry houdini', 'david blaine', 'teller']
print("Original magicians:")
show_magicians(magicians) # 没有改变

print("\nGreat magicians:")
# 如果不希望直接修改内部元素，可以建一个新的列表并返回，如下：
def make_great_copy(magicians):
   """在不改变原列表的情况下返回新列表 (这也是更推荐的做法)"""
   great_magicians = []
   for magician in magicians:
       great_magicians.append(f"{magician} the Great")
   return great_magicians
   
great_magicians = make_great_copy(magicians)
show_magicians(great_magicians)


# 8-12 三明治 (Sandwiches)
# 传递任意数量的实参。使用 *args 让 Python 收集多个位置实参于一个「元组」中。
print("\n8-12 Sandwiches:")
def make_sandwich(*items):
    """接受顾客点的一个或多个三明治配料"""
    print("\nI'll make you a great sandwich:")
    # *items 是一个收集了所有实参的元组
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

# 8-13 用户简介 (User Profile)
# 结合位置实参和任意数量关键字实参。使用 **kwargs 将收到的关键字实参存入「字典」中。
print("\n8-13 User Profile:")
def build_profile(first, last, **user_info): # user_info 往往也被称作 kwargs
    """创建一个包含我们知道的有关用户的一切的字典"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 遍历存储在 kwargs 中的所有额外键值对
    for key, value in user_info.items():
        profile[key] = value
        
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# 8-14 汽车 (Cars)
print("\n8-14 Cars:")
def make_car(manufacturer, model, **options):
    """制造一辆汽车，包含必备属性及任意选配"""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
        
    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
                      headlights='popup')
print(my_accord)
