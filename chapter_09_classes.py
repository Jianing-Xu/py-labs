# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第九章：类
"""

# 9-1 餐馆 (Restaurant)
# 定义一个表示餐馆的简单类。
class Restaurant:
    """一个表示餐馆的简单类"""

    # __init__ 是一个特殊的方法，每当你根据 Restaurant 类创建新实例时，Python 都会自动运行它
    # self 是一个指向实例本身的引用，让实例能够访问类中的属性和方法
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type"""
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印关于餐馆的信息"""
        print(f"\n{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """显示餐馆正在营业的消息"""
        print(f"{self.name} is currently open!")

print("9-1 Restaurant:")
# 根据类创建一个实例，提供餐馆名和菜系
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
# 调用实例中定义的方法
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 三家餐馆 (Three Restaurants)
print("\n9-2 Three Restaurants:")
ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

# 9-3 用户 (Users)
# 创建一个表示用户的类，包含基本属性如姓、名和其他可以存储在用户简介中的信息。
class User:
    """一个表示用户的简单类"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户属性"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"Welcome back, {self.username}!")

print("\n9-3 Users:")
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()


# 9-4 就餐人数 (Number Served)
# 给已有的类增加一个属性，并编写方法来修改和更新它的值。
class RestaurantV2(Restaurant): # 为了演示演进，我们继承之前的类（虽然这里可以直接修改原类）
    """在原有 Restaurant 类基础上增加就餐人数功能"""
    
    def __init__(self, name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(name, cuisine_type) # 调用父类的 __init__ 方法
        # 给属性指定默认值：0
        self.number_served = 0

    def set_number_served(self, number_served):
        """设定就餐人数"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """增加就餐人数"""
        self.number_served += additional_served

print("\n9-4 Number Served:")
restaurant_v2 = RestaurantV2('the mean queen', 'pizza')
restaurant_v2.describe_restaurant()

# 打印初始值
print(f"Number served: {restaurant_v2.number_served}")
# 直接修改属性的值
restaurant_v2.number_served = 430
print(f"Number served: {restaurant_v2.number_served}")
# 通过方法修改属性的值
restaurant_v2.set_number_served(1257)
print(f"Number served: {restaurant_v2.number_served}")
# 通过方法增加属性的值
restaurant_v2.increment_number_served(239)
print(f"Number served: {restaurant_v2.number_served}")


# 9-5 尝试登录次数 (Login Attempts)
class UserV2(User):
    """在 User 类基础上添加处理登录尝试次数的功能"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户"""
        super().__init__(first_name, last_name, username, email, location)
        self.login_attempts = 0

    def increment_login_attempts(self):
        """将尝试登录的次数加 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将 login_attempts 重置为 0"""
        self.login_attempts = 0

print("\n9-5 Login Attempts:")
eric = UserV2('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"Login attempts: {eric.login_attempts}") # 应为 3

eric.reset_login_attempts()
print(f"Login attempts: {eric.login_attempts}") # 应重置为 0


# 9-6 冰淇淋小店 (Ice Cream Stand)
# 继承 (Inheritance)。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
class IceCreamStand(Restaurant):
    """一个表示冰淇淋小店的特殊餐馆"""

    def __init__(self, name, cuisine_type='ice_cream'):
        """初始化父类的属性，然后初始化冰淇淋小店特有的属性"""
        super().__init__(name, cuisine_type)
        self.flavors = [] # 这是一个新建立的特有属性

    def show_flavors(self):
        """显示出售的冰淇淋口味"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

print("\n9-6 Ice Cream Stand:")
# 创建一个冰淇淋小店实例，只需要一个餐馆名字作为参数
big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
# 可以调用父类的方法
big_one.describe_restaurant()
# 也能调用子类特有的方法
big_one.show_flavors()


# 9-7 管理员 (Admin)
# 创建子类。管理员是一种特殊的用户。
class Admin(User):
    """一种具有管理权限的特殊用户"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员特有的属性。将权限放在本类里，不如把它提取成另一个类更为清晰 (参考 9-8)。这里我们先提供基本实现。"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """显示当前管理员的权限"""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

print("\n9-7 Admin:")
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

eric.show_privileges()


# 9-8 权限 (Privileges)
# 将实例用作属性（组合/聚合）。将 privileges 提取为一个独立的类。
class Privileges:
    """一个存储管理员权限的类"""

    def __init__(self, privileges=[]):
        """初始化 privileges 属性"""
        self.privileges = privileges

    def show_privileges(self):
        """显示权限"""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

class AdminV2(User):
    """具有管理权限的特殊用户，使用了提取出来的 Privileges 类"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员"""
        super().__init__(first_name, last_name, username, email, location)
        # 将一个 Privileges 的实例用作 Admin 的属性，即组合！
        self.privileges = Privileges()

print("\n9-8 Privileges:")
eric = AdminV2('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

# 直接修改被用作属性的 Privileges 类的内置列表元素
eric.privileges.privileges = [
    'can add posts',
    'can delete posts',
    'can ban users',
]
# 调用被用作属性的 Privileges 类的方法
eric.privileges.show_privileges()
