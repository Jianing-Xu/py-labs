# Python编程：从入门到实践 (代码案例与项目集)

这是一个基于《Python编程：从入门到实践（第2版）》的学习项目仓库。此仓库包含从基础语法到三大综合实战项目（2D游戏、数据可视化、Web应用）的完整代码实现，所有的代码均配备了详尽的中文注释以便于新手学习、复习和二次修改。

## 目录结构
仓库分为两大部分：
1. **基础语法章节案例 (`chapter_02` ~ `chapter_11`)**
2. **三大实战项目 (`alien_invasion`, `data_visualization`, `learning_log`)**

### 模块说明
- **`chapter_02_variables.py`**: 变量和简单数据类型（如字符串方法，f-string）
- **`chapter_03_lists.py`**: 列表的基础操作（增删改查、排序）
- **`chapter_04_working_with_lists.py`**: 操作列表循环、列表解析、元组初步
- **`chapter_05_if_statements.py`**: `if` 语句和条件测试
- **`chapter_06_dictionaries.py`**: 字典以及字典的高级嵌套用法
- **`chapter_07_user_input_and_while_loops.py`**: `while` 循环和 `input()` 用户交互
- **`chapter_08_functions.py`**: 函数的定义、参数传递 (位置、关键字、默认、可变长度)
- **`chapter_09_classes.py`**: 面向对象基础：类、对象、属性、方法、继承和组合
- **`chapter_10_files_and_exceptions.py`**: 文件读写操作、`try-except` 异常处理、JSON 序列化存储
- **`chapter_11_testing_your_code.py`**: 使用内置的 `unittest` 对函数和类进行代码测试
- **`alien_invasion/`**: 构建2D游戏《外星人入侵》
- **`data_visualization/`**: 数据可视化项目
- **`learning_log/`**: Django Web 应用 —— 学习笔记

---

## 环境准备与依赖安装

建议通过 `venv` 虚拟环境隔离你的库安装。

### 1. 激活虚拟环境 (macOS/Linux)
在项目根目录下打开终端，运行：
```bash
# 激活虚拟环境 (当终端提示符前出现 (venv) 则表示激活成功)
source venv/bin/activate
```

*(如果虚拟环境未初始化，请使用 `python3 -m venv venv` 重新建立)*

### 2. 安装依赖库
激活虚拟环境后，安装本书项目中需要用到的所有第三方库：
```bash
pip install -r requirements.txt

# 或者手动安装
pip install pygame matplotlib plotly django django-bootstrap5
```

---

## 快速启动指南

### 1. 运行基础语法案例
直接执行对应的 python 脚本即可，它会将每个小的习题例子清晰地输出在终端中：
```bash
python chapter_04_working_with_lists.py
```

### 2. 实战项目一：《外星人入侵》(Alien Invasion)
这是一个利用 `pygame` 模块开发的 2D 射击生存游戏。
- **目标：** 驾驶飞船消灭下落的外星人舰队。一旦遭受碰撞或让外星人突破底端，即失去一条命。
- **操作：**
  - **`←` / `→`**: 左右移动飞船
  - **`Space (空格)`**: 发射子弹
  - **`Q`**: 快速退出游戏

**启动方法：**
```bash
cd alien_invasion
python alien_invasion.py
```

### 3. 实战项目二：数据可视化 (Data Visualization)
利用 `matplotlib` 生成数学与统计图表。提供了简单的折线图、散点图以及经典的随机漫步（Random Walk）算法展现。
- **特性：** `rw_visual.py` 每次运行都会重新计算随机漫步的点（共 50,000 个），因此每次生成的图案都不会相同，犹如细胞或是星系。
  
**启动方法：** (以随机漫步为例)
```bash
cd data_visualization
python rw_visual.py
```
*(绘图完毕后，可以放大、平移、或将图片保存至本地)*

### 4. 实战项目三：学习笔记 Web 应用 (Learning Log)
使用 `Django` 框架搭设的用户级在线系统。目前建立好了核心的数据模型层 (`Topic` 主题 和 `Entry` 学习条目)，并完成了初始的数据库迁移。
- **核心逻辑位于：** `learning_log/learning_logs/models.py`

**启动基础后台：**
```bash
cd learning_log

# 若还没做过迁移或者想重置数据库：
python manage.py makemigrations learning_logs
python manage.py migrate

# 启动 Django 开发服务器
python manage.py runserver
```
启动后可以在浏览器中访问控制台。由于目前还主要是数据模型结构，后续可以继续开发前端视图与模板来完善整个全栈项目。

---

如果遇到依赖未找到的错误，请确保你已经通过 `source venv/bin/activate` 进入了正确的虚拟开发环境！
