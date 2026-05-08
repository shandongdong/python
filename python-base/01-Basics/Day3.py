# 2. dict 深入理解
#   dict 是 Python 的灵魂数据结构，使用频率远超 Java 的 HashMap。

#   Java 对比： Python 的 dict ≈ Java 的 LinkedHashMap（3.7+ 保证插入顺序），但它是语言核心，JSON 解析、函数参数、对象属性底层都是 dict。

# --- 基本操作你肯定会，重点看这些进阶用法 ---

# 1. get() 带默认值：避免 KeyError
config = {"host": "localhost", "port": 8080}
timeout = config.get("timeout", 30)  # key 不存在时返回 30，而不是报错
# Java 对比：map.getOrDefault("timeout", 30)

# 2. setdefault()：key 不存在时设置并返回默认值
groups = {}
for name, dept in [("张三", "工程"), ("李四", "产品"), ("王五", "工程")]:
    groups.setdefault(dept, []).append(name)
print(groups)

# 3. defaultdict：更优雅的分组方式
from collections import defaultdict

groups = defaultdict(list)
for name, dept in [("张三", "工程"), ("李四", "产品"), ("王五", "工程")]:
    groups[dept].append(name)
print(groups)


# --- 场景二：快速成员检测 ---
# list 的 in 操作是 O(n)，set 是 O(1)
allowed_users = {"admin", "editor", "viewer"}  # 用 set 而不是 list
user_role = "editor"
if user_role in allowed_users:
    pass
print("用户角色是否在允许的用户集合中:", user_role in allowed_users)

students = [
    {"name": "张三", "scores": [85, 92, 78]},
    {"name": "李四", "scores": [90, 88, 95]},
    {"name": "王五", "scores": [72, 85, 80]},
    {"name": "张三", "scores": [88, 76, 92]},  # 注意：张三出现了两次
    {"name": "赵六", "scores": [95, 91, 89]},
]
print("学生列表:", set([student["name"] for student in students]))
for student in students:
    print(
        student["name"],
        "的平均成绩是:",
        sum(student["scores"]) / len(student["scores"]),
    )


project_a = {"张三", "李四", "王五", "赵六", "钱七"}
project_b = {"李四", "王五", "孙八", "周九"}
project_c = {"王五", "赵六", "孙八", "吴十"}

print(f"同时参与了全部三个项目的人 是 {project_a & project_b & project_c}")
print(
    f"只参与了 project_a、没参与其他任何项目的人是 { project_a - project_b - project_c}"
)
only_a = project_a - project_b - project_c
only_b = project_b - project_a - project_c
only_c = project_c - project_a - project_b
print(f"恰好只参与一个项目的人是 {only_a | only_b | only_c}")

logs = [
    ("2024-01-15", "ERROR", "数据库连接超时"),
    ("2024-01-15", "WARNING", "内存使用率超过80%"),
    ("2024-01-15", "ERROR", "数据库连接超时"),
    ("2024-01-16", "ERROR", "文件未找到"),
    ("2024-01-16", "INFO", "服务启动成功"),
    ("2024-01-16", "WARNING", "磁盘空间不足"),
    ("2024-01-16", "ERROR", "数据库连接超时"),
    ("2024-01-17", "ERROR", "文件未找到"),
    ("2024-01-17", "ERROR", "文件未找到"),
    ("2024-01-17", "WARNING", "内存使用率超过80%"),
]
result = [date for date, level, message in logs if level == "ERROR"]
print(f"所有 ERROR 日志的日期是 {result}")
from collections import Counter

top_error, count = Counter(result).most_common(1)[0]
print(f"最频繁的错误： {top_error}，出现了 {count} 次")


print(f"{'*'  * 20} Day 02 {'*' * 20}") 
# === 命名切片：提高可读性 ===
# 比如解析固定格式的文本行
line = "张三      95   88   92"
# 对字符串进行切片
print(line[1:14])
NAME = slice(0, 6)

SCORE1 = slice(10, 12)
SCORE2 = slice(15, 17)
print(line[NAME].strip())  # "张三"
print(line[SCORE1])  # "95"
# 比起到处写 line[0:6]、line[10:12]，命名切片意图更清晰



  # === 嵌套解包 ===
(a, b), c = [1, 2], 3
print(a, b, c)  # 1 2 3

points = [(1, 2), (3, 4), (5, 6)]
# 遍历时解包，是把"取值"和"解包"合二为一
for x, y in points:
    print(f"x={x}, y={y}")

for point in points:
    x, y = point # 先取元组，再解包
    print(f"x={x}, y={y}")


print("*" * 20)
# enumerate：同时拿索引和值
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    
print("*" * 25)
for i, fruit in enumerate(fruits, start=1):  # 从1开始
    print(f"{i}: {fruit}")

print("迭代器------")

# 手动验证
lst = [1, 2, 3]
it = iter(lst)       # 获取迭代器
print(next(it))      # 1
print(next(it))      # 2
print(next(it))      # 3
# print(next(it))      # StopIteration 异常！

# 重要区别 ：迭代器是一次性的，遍历完就空了：
it = iter([1, 2, 3])
print(list(it))   # [1, 2, 3]
print(list(it))   # [] ← 已经耗尽了！



products = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]
prices = [5.5, 3.0, 4.2, 8.8, 12.0]
stocks = [100, 50, 75, 30, 20]

# --- 第 1 问：构建价格字典 ---
price_dict = dict(zip(products, prices))
print(price_dict)   # {'苹果': 5.5, '香蕉': 3.0, '橘子': 4.2, ...}
# zip 把两个列表配对 → [("苹果", 5.5), ("香蕉", 3.0), ...]
# dict() 把配对列表直接转成字典


print(list(zip(products, prices)))
print(dict(zip(products, prices)))

#zip 是惰性的、以短为准的、产出元组的配对工具 。
for product, price, stock in zip(products, prices, stocks):
    print(f"{product} 的价格是 {price}，库存是 {stock}")


print("*sort and groupby*")




# 排序

words = ["banana", "pie", "Washington", "book"]
print(sorted(words))    # ['Washington', 'banana', 'book', 'pie']
# 按字符串长度排序
sorted(words, key=len)  
# ["pie", "book", "banana", "Washington"]

# 按小写后的字母排序
sorted(words, key=str.lower)  
# ["banana", "book", "pie", "Washington"]

students = [
    {"name": "Alice", "score": 88, "age": 22},
    {"name": "Bob", "score": 95, "age": 20},
    {"name": "Charlie", "score": 72, "age": 21},
]
# 排序 + lambda + groupby

# 按分数排序
sorted(students, key=lambda s: s["score"])
# [Charlie(72), Alice(88), Bob(95)]

# 按名字排序
sorted(students, key=lambda s: s["name"])
# [Alice, Bob, Charlie]

# 按分数降序
sorted(students, key=lambda s: s["score"], reverse=True)
# [Bob(95), Alice(88), Charlie(72)]




from itertools import groupby

employees = [
    {"name": "张三", "dept": "工程", "salary": 15000},
    {"name": "李四", "dept": "产品", "salary": 18000},
    {"name": "王五", "dept": "工程", "salary": 22000},
    {"name": "赵六", "dept": "产品", "salary": 16000},
    {"name": "钱七", "dept": "工程", "salary": 15000},
]

# --- 第 1 问：按工资从高到低 ---
by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
for e in by_salary:
    print(f"{e['name']} - {e['salary']}")
# 王五-22000, 李四-18000, 赵六-16000, 张三-15000, 钱七-15000



# --- Day 03 继续 ---
"""
  1. 列表推导式（List Comprehension）  
   === 基本语法：[表达式 for 变量 in 可迭代对象] ===
"""

  # ❌ Java 思维：用 for 循环
squares = []
for x in range(10):
    squares.append(x ** 2)  # ** 是 Python 的 幂运算 （求乘方）：x ** 2 表示 x 的平方
    print(x, x ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# ✅ 列表推导式：一行搞定
squares = [(x + 1)  for x in range(10)]
print(squares)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 带条件过滤：只有当 x > 5 时，才会被添加到列表中
squares = [x + 1  for x in range(10) if x > 5]
print(squares)  # [6, 7, 8, 9, 10]

# 带条件转换（if-else）：
# 注意！if-else 放在 for 前面，不是后面
# 语法：[A if 条件 else B for 变量 in 可迭代对象]
squares = [ x if x > 5 else 0 for x in range(10)]
print(squares)  # [0, 0, 0, 0, 0, 0, 6, 7, 8, 9]
# 带条件过滤：只有当 x < 8 时，才会被添加到列表中
squares = [ x if x > 5 else 0 for x in range(10) if x < 8]
print(squares)  # [0, 0, 0, 0, 0, 0, 6, 7]

# 容易搞混的点：
# [x for x in nums if x > 0]       ← 过滤：扔掉不满足条件的
# [x if x > 0 else 0 for x in nums] ← 转换：每个元素都保留，但值可能变

  # === 字典推导式：{key: value for ...} ===

names = ["张三", "李四", "王五"]
scores = [85, 92, 78]

# 构建字典
score_dict = {name: score for (name, score) in zip(names, scores)}
# {'张三': 85, '李四': 92, '王五': 78}
# 效果和 dict(zip(names, scores)) 一样，但推导式可以加条件
print(score_dict) # {'张三': 85, '李四': 92, '王五': 78}

# 只要90分以上的
high_scores = {name: score for name, score in zip(names, scores) if score >= 90}
print(high_scores) # {'李四': 92}

# === 集合推导式：{表达式 for ...} ===

nums2 = [1, 2, 2, 3, 3, 3, 4]
unique_squares2 = {x ** 2 for x in nums2}    # {...} 是 集合推导式 ，产出的是 set （集合），而集合天生就去重。
print(unique_squares2) # {16, 1, 4, 9}. 集合元素是无序的，所以打印结果可能和预期不同。

nums3 = [1, 2, 2, 3, 3, 3, 4]
unique_squares3 = [x ** 2 for x in nums3]    # {...} 是 列表推导式 ，产出的是 list （列表），而列表天生就不去重。
print(unique_squares3) # [1, 4, 4, 9, 9, 9, 16]. 列表元素是有序的，所以打印结果和预期相同。

# 怎么区分字典推导式和集合推导式？ 看有没有冒号 :
[x ** 2 for x in nums2]   # [] → 列表推导式，不去重，有序    # [1, 4, 4, 9, 9, 9, 16]
{x ** 2 for x in nums2}   # {} → 集合推导式，自动去重，无序  # {16, 1, 4, 9}
{x: x**2 for x in nums2}  # {:} → 字典推导式，key去重      # {1: 1, 2: 4, 3: 9, 4: 16}
""" 推导过程：
    1 → 1² = 1    加入集合 {1}
    2 → 2² = 4    加入集合 {1, 4}
    2 → 2² = 4    已存在，跳过
    3 → 3² = 9    加入集合 {1, 4, 9}
    3 → 3² = 9    已存在，跳过
    3 → 3² = 9    已存在，跳过
    4 → 4² = 16   加入集合 {1, 4, 9, 16}
"""

# 3. 生成器表达式 vs 列表推导式

# Why：列表推导式会一次性把所有结果放到内存里。如果数据量很大（比如一百万行日志），内存会爆。生成器表达式是"懒计算"的，每次只算一个值。

# 列表推导式：用 []，立刻计算所有结果，存在内存里
squares_list = [x ** 2 for x in range(1000000)]   # 占内存！

# 生成器表达式：用 ()，不立刻计算，遍历时才一个一个算
squares_gen = (x ** 2 for x in range(1000000))     # 几乎不占内存

# 生成器只能遍历一次
for s in squares_gen:
    pass   # 遍历完了

for s in squares_gen:
    pass   # 第二次遍历什么都拿不到！

# Java 对比：生成器 ≈ Java Stream，都是懒求值、只能消费一次

words = ["Hello", "WORLD", "Python", "java", "Flask", "SPRING"]
lower = [(word.lower(), len(word)) for word in words]
print(lower)  # ['hello', 'world', 'python', 'java', 'flask', 'spring']
print(dict(lower))  # {'hello': 5, 'world': 5, 'python': 6, 'java': 4, 'flask': 5, 'spring': 6}
