# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第六章：字典
"""

# 6-1 人 (Person)
# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}
print("6-1 Person:")
print(f"First name: {person['first_name'].title()}")
print(f"Last name: {person['last_name'].title()}")
print(f"Age: {person['age']}")
print(f"City: {person['city'].title()}")

# 6-2 喜欢的数字 (Favorite Numbers)
# 使用字典来存储一些人喜欢的数字，打印出每个人的名字和他们喜欢的数字。
print("\n6-2 Favorite Numbers:")
favorite_numbers = {
    'mikael': 42,
    'john': 7,
    'jane': 13,
    'alice': 2,
    'bob': 100,
}
for name, number in favorite_numbers.items():
    # items() 返回一个包含键值对的元组列表
    print(f"{name.title()}'s favorite number is {number}.")

# 6-3 词汇表 (Glossary)
# 类似于编程术语和其释义组成的字典。字典中的键必须唯一，通常用字符串表示。
print("\n6-3 Glossary:")
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}
for word, definition in glossary.items():
    print(f"{word.title()}:\n\t{definition}") # \t 是制表符，用于排版

# 6-4 词汇表 2 (Glossary 2)
# 使用 for 循环遍历字典的键（通常默认即可，或者使用 keys() 方法）和值（values() 方法）。
print("\n6-4 Glossary 2 (Adding new keys):")
# 在字典中添加新的键值对
glossary['set'] = 'A collection in which each item must be unique.'
glossary['boolean'] = 'An expression that evaluates to True or False.'
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'

# 遍历键并打印，可以对键列表 sorted() 进行排序
for word in sorted(glossary.keys()): # 确保总是以字母顺序输出术语
    print(f"{word.title()}:\n\t{glossary[word]}")

# 6-5 河流 (Rivers)
# 创建一个字典，包含三条河流及其流经的国家，使用循环打印一条有意义的句子。
print("\n6-5 Rivers:")
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}
# 1. 打印句子
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 2. 单独打印河流名字
print("\nRivers included in this dictionary:")
for river in rivers.keys(): # 等同于 for river in rivers:
    print(f"- {river.title()}")

# 3. 单独打印流经的国家名字
print("\nCountries included in this dictionary:")
for country in set(rivers.values()): # set() 集合可以剔除重复元素，这里演示即使有重复国家也只显示一次
    print(f"- {country.title()}")

# 6-6 调查 (Polling)
# 创建一个应该参与最喜欢的编程语言调查的名单（列表）。
print("\n6-6 Polling:")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
coders_to_poll = ['jen', 'sarah', 'matt', 'colin', 'phil']
for coder in coders_to_poll:
    if coder in favorite_languages.keys(): # 也可以写成 if coder in favorite_languages:
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")

# 6-7 人们 (People)
# 这是一个关于“嵌套”的例子：在一个列表中嵌套多个字典。
print("\n6-7 People (Nesting - List of Dictionaries):")
# 创建另外两个人的字典，并在末尾把它们和一个旧字典组成列表。
person_1 = person # 我们在 6-1 定义好的 person 字典
person_2 = {
    'first_name': 'marie',
    'last_name': 'curie',
    'age': 66,
    'city': 'paris',
}
person_3 = {
    'first_name': 'albert',
    'last_name': 'einstein',
    'age': 76,
    'city': 'princeton',
}
people = [person_1, person_2, person_3] # 这是一个列表！

for p in people: # 此时的 p 就是每一个字典
    full_name = f"{p['first_name']} {p['last_name']}".title()
    print(f"{full_name}, of {p['city'].title()}, is {p['age']} years old.")

# 6-8 宠物 (Pets)
# 类似 6-7，列表中嵌套多个代表宠物的字典。
print("\n6-8 Pets:")
pet_1 = {'animal_type': 'python', 'owner': 'guido'}
pet_2 = {'animal_type': 'dog', 'owner': 'eric'}
pet_3 = {'animal_type': 'cat', 'owner': 'jaden'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"\nHere's what I know about {pet['owner'].title()}'s {pet['animal_type']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

# 6-9 喜欢的地方 (Favorite Places)
# 字典中嵌套列表（即一个键对应着一个值列表）。
print("\n6-9 Favorite Places (Nesting - Dictionary of Lists):")
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. washington', 'the rusty logger', 'jackson hole'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places: # 内部进行第二个 for 循环来遍历列表
        print(f"- {place.title()}")

# 6-10 喜欢的数字 (Favorite Numbers 2)
# 基于 6-2，让每个人可以有多个喜欢的数字，同样是字典中嵌套列表。
print("\n6-10 Favorite Numbers 2:")
favorite_numbers = {
    'mikael': [42, 17],
    'john': [7, 11, 23],
    'jane': [13],
    'alice': [2, 4, 8],
    'bob': [100, 200, 300],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for num in numbers:
        print(f"  {num}")

# 6-11 城市 (Cities)
# 字典中嵌套另一个字典。键为城市名，值为包含该城市信息的字典（包括所在国家、大概人口以及一个表示该城市的特长）。
print("\n6-11 Cities (Nesting - Dictionary of Dictionaries):")
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'fact': 'andes mountains are nearby',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'fact': 'it is near denali mountain',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'fact': 'it has himalaya mountains',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].capitalize()
    
    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  Fact: {fact}.")
