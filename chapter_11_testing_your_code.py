# -*- coding: utf-8 -*-

"""
《Python编程：从入门到实践（第2版）》
第十一章：测试代码
"""
import unittest

# -------------------------------------------------------------------
# 第一部分：测试函数
# -------------------------------------------------------------------

# 11-1 城市和国家 (City, Country)
# 编写一个接受两个参数（城市名和国家名）的函数，返回类似于 Santiago, Chile 的字符串。
def city_country(city, country, population=''):
    """生成格式化的城市和国家名。"""
    # 11-2 人口数量 (Population)
    # 修改该函数，使其包含第三个必不可少的形参 population
    # 为了让11-1的测试依然通过，我们将其设为可选形参（默认值为空字符串）
    if population:
        formatted_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_name = f"{city.title()}, {country.title()}"
    return formatted_name

# 为上面定义的函数编写测试用例
# 测试类必须继承 unittest.TestCase
class CityTestCase(unittest.TestCase):
    """测试 city_country() 函数。"""

    # 所有以 test_ 打头的方法在运行测试时都会自动运行
    def test_city_country(self):
        """测试像 Santiago, Chile 这样的字符串能否正确处理。"""
        # 调用要测试的函数
        formatted_name = city_country('santiago', 'chile')
        # 断言方法 (assertEqual): 检查函数返回的值是否与我们期望的值匹配
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """测试带有人口参数的输入能否正确处理。"""
        formatted_name = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


# -------------------------------------------------------------------
# 第二部分：测试类
# -------------------------------------------------------------------

# 11-3 雇员 (Employee)
# 编写一个名为 Employee 的类。
class Employee:
    """一个表示雇员的简单类。"""

    def __init__(self, first_name, last_name, annual_salary):
        """初始化雇员的属性。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """默认将年薪增加 5000 美元，但也能够接受其他增加的金额。"""
        self.annual_salary += amount


# 为上面定义的类编写测试用例
class TestEmployee(unittest.TestCase):
    """测试 Employee 类的方法。"""

    # setUp() 方法：如果你需要在多个测试方法中使用相同的实例或对象，
    # 可以在 setUp() 中创建它们。unittest 会在运行每个 test_ 方法前先运行 setUp()。
    def setUp(self):
        """
        创建一个 employee 实例供所有测试方法使用。
        这避免了在每个测试方法中重复实例化 Employee 对象。
        """
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """测试使用默认金额加薪是否正确工作。"""
        self.eric.give_raise()
        # 原年薪 65000 + 默认加薪 5000 = 70000
        self.assertEqual(self.eric.annual_salary, 70000)

    def test_give_custom_raise(self):
        """测试自定义金额的加薪是否正确工作。"""
        self.eric.give_raise(10000)
        # 原年薪 65000 + 新增 10000 = 75000
        self.assertEqual(self.eric.annual_salary, 75000)


# -------------------------------------------------------------------
# 运行测试
# -------------------------------------------------------------------
if __name__ == '__main__':
    # 只有在该文件被直接运行（而不是被当做模块导入）时，才会执行单元测试
    # unittest.main() 会自动去寻找当前文件中继承了 unittest.TestCase 的类，
    # 并运行这些类中所有以 test 开头的方法。
    print("Running Chapter 11 Unittests...\n")
    unittest.main()
