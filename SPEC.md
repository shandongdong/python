# Python 系统学习计划

> **学习者画像**：有 2 年 Java/Spring Boot 全栈经验，用过 Flask/FastAPI 但 Python 基础不牢
> **目标**：系统掌握 Python 基础，进阶主题了解即可
> **时间安排**：每天 2-3 小时，预计 10-12 天完成
> **学习方式**：边做边学 + 按模块集中击破 + Java 对比理解 + 导师出题批改
> **Python 版本**：3.12+

---

## 总览：4 大模块 × 10 天

| 阶段 | 模块 | 天数 | 核心主题 |
|------|------|------|----------|
| 一 | 数据结构与 Pythonic 语法 | Day 1-3 | 内置类型深入、推导式、解包、迭代协议 |
| 二 | 函数进阶与装饰器 | Day 4-5 | 闭包、装饰器、生成器、上下文管理器 |
| 三 | 面向对象与魔法方法 | Day 6-8 | 类机制、魔法方法、继承、Mixin、描述器 |
| 四 | 进阶主题概览 | Day 9-10 | 类型注解、异常体系、并发入门、模块/包管理 |

---

## 模块一：数据结构与 Pythonic 语法（Day 1-3）

### Day 1：内置数据结构深入

**学习目标**：清楚 list / tuple / set / dict 各自的适用场景和底层机制差异

#### 知识点

1. **可变 vs 不可变**
   - Java 对比：`ArrayList`（可变）vs `List.of()`（不可变），Python 的 list vs tuple 类似但更深——tuple 可做 dict key，list 不行
   - 为什么 tuple 可哈希、list 不行？底层的 `__hash__` 机制
   - 实际场景：什么时候该用 tuple 而不是 list

2. **dict 的深入理解**
   - Java 对比：Python dict ≈ Java `LinkedHashMap`（3.7+ 保序），但 Python dict 是语言核心，不是"集合框架的一个实现"
   - `defaultdict`、`Counter`、`OrderedDict` 的使用场景
   - dict 的常用模式：`setdefault()`、`dict.get()` 带默认值、`**` 合并

3. **set 的实际用途**
   - Java 对比：`HashSet`，但 Python 支持 `&` `|` `-` `^` 运算符做集合运算
   - 去重、成员检测（O(1) vs list 的 O(n)）、集合运算

4. **选择数据结构的决策树**
   - 需要有序？→ list / tuple
   - 需要去重？→ set
   - 需要键值映射？→ dict
   - 需要不可变（做 key / 放入 set）？→ tuple / frozenset
   - 需要频繁查找？→ set / dict（O(1)）vs list（O(n)）

#### 练习题（导师出题）
- 题目将在学习当天由导师给出，完成后导师批改并讲解

---

### Day 2：序列操作与解包

**学习目标**：熟练使用切片、解包、zip、enumerate 等 Pythonic 写法

#### 知识点

1. **切片高级用法**
   - Java 对比：Java 没有原生切片，需要 `subList()` 或 `Arrays.copyOfRange()`；Python 切片是一等操作
   - `a[::2]`（步长）、`a[::-1]`（反转）、切片赋值 `a[1:3] = [10, 20, 30]`
   - 切片对象 `slice()` 和命名切片提高可读性

2. **解包（Unpacking）**
   - Java 对比：Java 没有解包，需要逐个赋值；Python 可以 `a, b, c = [1, 2, 3]`
   - 星号解包 `first, *rest = items`
   - 嵌套解包 `(a, b), c = (1, 2), 3`
   - 函数参数中的 `*args` 和 `**kwargs`

3. **迭代三件套：enumerate / zip / itertools**
   - Java 对比：Java 没有 `enumerate`，需要手动维护 index；`zip` 相当于 Java 8 的 `IntStream` 手动合并
   - `enumerate(items, start=1)` 替代手动计数
   - `zip()` 并行迭代、`zip(*matrix)` 转置矩阵
   - `itertools` 常用：`chain`、`groupby`、`product`

4. **排序进阶**
   - `sorted()` vs `list.sort()`（新对象 vs 原地）
   - `key=` 参数 + `lambda` + `operator.itemgetter`
   - 多条件排序：`key=lambda x: (x.age, x.name)`

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

### Day 3：推导式与迭代协议

**学习目标**：写出地道的推导式，理解迭代器/可迭代对象的区别

#### 知识点

1. **列表推导式（List Comprehension）**
   - Java 对比：类似 Java Stream 的 `.map().filter().collect()`，但语法更简洁
   - 基础：`[x**2 for x in range(10)]`
   - 带条件：`[x for x in items if x > 0]`
   - 嵌套推导：`[cell for row in matrix for cell in row]`（注意顺序！）
   - 什么时候不该用推导式：逻辑复杂时用普通 for 循环更清晰

2. **字典推导式和集合推导式**
   - `{k: v for k, v in pairs}`
   - `{x % 3 for x in range(10)}`
   - 实际场景：数据转换、索引构建

3. **生成器表达式 vs 列表推导式**
   - `(x**2 for x in range(10))` 懒求值，不占内存
   - 什么时候用生成器表达式：数据量大、只需迭代一次
   - Java 对比：类似 Java Stream 的懒求值特性

4. **迭代协议**
   - `__iter__()` 和 `__next__()` 的关系
   - 可迭代对象（Iterable）vs 迭代器（Iterator）的区别
   - `for` 循环的底层机制：先调 `iter()`，再反复调 `next()`
   - Java 对比：相当于 `Iterable` 接口 + `Iterator` 接口

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

## 模块二：函数进阶与装饰器（Day 4-5）

### Day 4：闭包与装饰器

**学习目标**：理解闭包原理，能手写和使用装饰器

#### 知识点

1. **函数是一等对象**
   - Java 对比：Java 8 的 lambda 和函数式接口是"近似一等"，Python 函数真正是对象，可以赋值、传参、返回
   - 高阶函数：`map()`、`filter()`、`sorted()` 的 key 参数
   - 函数作为参数、函数作为返回值

2. **闭包（Closure）**
   - 什么是闭包：内部函数引用了外部函数的变量
   - `nonlocal` 关键字的作用（对比 `global`）
   - 闭包的实际用途：工厂函数、配置化行为
   - Java 对比：类似匿名内部类捕获 effectively final 变量，但 Python 更灵活

3. **装饰器（Decorator）**
   - `@decorator` 语法糖的本质：`func = decorator(func)`
   - 手写一个计时装饰器、日志装饰器
   - `functools.wraps` 为什么必须加
   - 带参数的装饰器（三层嵌套）
   - Java 对比：类似 Spring AOP / 注解 + 切面，但实现机制完全不同

4. **常用内置装饰器**
   - `@property`、`@staticmethod`、`@classmethod`
   - `@functools.lru_cache` 做缓存
   - `@dataclass`（Day 7 详细展开）

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

### Day 5：生成器与上下文管理器

**学习目标**：掌握 yield 的工作机制，理解 with 语句背后的协议

#### 知识点

1. **生成器函数（Generator）**
   - `yield` vs `return`：函数变成惰性迭代器
   - 生成器的执行流程：暂停和恢复
   - `yield from` 委托生成器
   - 实际场景：逐行读大文件、分页 API 数据处理
   - Java 对比：Java 没有原生 yield，最接近的是 `Stream.generate()` 或 `Iterator` 实现

2. **生成器的高级用法**
   - `send()` 和 `throw()` 方法
   - 生成器实现协程的雏形（了解即可，不深入）
   - 管道模式：多个生成器串联处理数据流

3. **上下文管理器（Context Manager）**
   - `with` 语句的协议：`__enter__()` 和 `__exit__()`
   - 为什么文件操作要用 `with open()`：保证资源释放
   - 自定义上下文管理器（类方式）
   - `contextlib.contextmanager` 用 `yield` 简化实现
   - Java 对比：相当于 try-with-resources + `AutoCloseable`

4. **实际应用模式**
   - 数据库连接管理
   - 临时修改状态（如临时切换目录）
   - 计时上下文管理器

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

## 模块三：面向对象与魔法方法（Day 6-8）

### Day 6：Python 类的基础机制

**学习目标**：理解 Python 类与 Java 类的根本差异，掌握类的核心机制

#### 知识点

1. **Python 类 vs Java 类的根本差异**
   - 一切皆对象：类本身也是对象（`type` 的实例）
   - 动态属性：可以运行时给实例/类添加属性（Java 做不到）
   - 没有访问修饰符：`_` 是约定私有，`__` 是名称改写（name mangling），不是真正的 private
   - Java 对比：Java 有 `private/protected/public`，Python 靠约定和自觉

2. **`__init__` 不是构造器**
   - `__new__` 才是真正创建实例的，`__init__` 只是初始化
   - 什么时候需要 `__new__`（单例模式、不可变类型子类化）
   - Java 对比：Java 的 `new` 关键字 = Python 的 `__new__` + `__init__`

3. **实例属性 vs 类属性**
   - 类属性是共享的（类似 Java static field）
   - 实例属性覆盖类属性的查找机制（MRO 的前奏）
   - `__dict__` 查看属性字典
   - `__slots__` 限制属性 + 节省内存

4. **方法类型**
   - 实例方法 / 类方法（`@classmethod`）/ 静态方法（`@staticmethod`）
   - 什么时候用 `@classmethod`：替代构造器模式
   - Java 对比：`@classmethod` ≈ Java 的工厂方法，`@staticmethod` ≈ Java 的 `static` 方法

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

### Day 7：魔法方法（Dunder Methods）

**学习目标**：掌握常用魔法方法，让自定义类表现得像内置类型

#### 知识点

1. **字符串表示**
   - `__repr__` vs `__str__`：开发者 vs 用户
   - 规则：`__repr__` 必须实现，`__str__` 可选
   - Java 对比：`__repr__` ≈ 详细的 `toString()`，`__str__` ≈ 用户友好的 `toString()`

2. **比较与排序**
   - `__eq__`、`__lt__`、`__le__` 等
   - `@functools.total_ordering`：只写 `__eq__` + `__lt__`，自动补全其他
   - `__hash__` 与 `__eq__` 的关系（可变对象不应该可哈希）
   - Java 对比：`__eq__` ≈ `equals()`，`__hash__` ≈ `hashCode()`，`__lt__` ≈ `Comparable`

3. **容器协议**
   - `__len__`、`__getitem__`、`__setitem__`、`__contains__`
   - 实现一个简单的自定义序列类
   - `__getitem__` 支持切片
   - Java 对比：`__len__` ≈ `size()`，`__getitem__` ≈ `get()`，`__contains__` ≈ `contains()`

4. **运算符重载**
   - `__add__`、`__mul__`、`__radd__`（反向运算）
   - 实际场景：向量类、货币类
   - `__iadd__`（`+=` 原地操作）
   - Java 对比：Java 不支持运算符重载（除了 String 的 `+`），这是 Python 的优势

5. **`@dataclass` 自动生成魔法方法**
   - 自动生成 `__init__`、`__repr__`、`__eq__`
   - `frozen=True` 不可变数据类
   - `field()` 自定义字段行为
   - Java 对比：`@dataclass` ≈ Java 14 的 `record` 或 Lombok 的 `@Data`

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

### Day 8：继承、Mixin 与协议

**学习目标**：理解 Python 的继承体系和"鸭子类型"哲学

#### 知识点

1. **继承机制**
   - 单继承 + `super()` 的正确用法
   - `super()` 不是"调用父类"，而是按 MRO 调用下一个类
   - Java 对比：Java 的 `super` 是确定性地调用父类，Python 的 `super()` 按 MRO 链查找

2. **多重继承与 MRO**
   - C3 线性化算法（了解规则即可）
   - `ClassName.__mro__` 或 `ClassName.mro()` 查看顺序
   - 菱形继承问题及 Python 的解决方案
   - Java 对比：Java 不支持多重继承（只能多实现接口），Python 支持但需小心使用

3. **Mixin 模式**
   - 什么是 Mixin：提供单一功能的小型类，不单独使用
   - 命名约定：`XxxMixin`
   - 实际场景：`JsonMixin`、`LoggingMixin`
   - Java 对比：Mixin ≈ Java 8 的接口默认方法（default method）

4. **鸭子类型与协议（Protocol）**
   - "如果它走路像鸭子、叫声像鸭子，那它就是鸭子"
   - 不需要显式继承接口，只要实现了方法就行
   - `typing.Protocol`（3.8+）：结构化子类型
   - `ABC`（抽象基类）vs Protocol 的选择
   - Java 对比：Java 必须 `implements` 接口，Python 默认鸭子类型，Protocol 是可选的静态检查工具

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

## 模块四：进阶主题概览（Day 9-10）

### Day 9：类型注解与异常处理

**学习目标**：会写类型注解提高代码可读性，掌握 Python 异常的正确用法

#### 知识点

1. **类型注解基础**
   - 变量注解：`name: str = "hello"`
   - 函数注解：`def greet(name: str) -> str:`
   - 复合类型：`list[str]`、`dict[str, int]`、`tuple[int, ...]`（3.9+原生支持）
   - `Optional[X]` = `X | None`（3.10+ 用 `|` 语法）
   - Java 对比：Python 的类型注解是可选的、运行时不强制，不像 Java 的类型系统那样强制

2. **类型注解进阶（了解）**
   - `TypeVar` 泛型、`Generic` 基类
   - `TypeAlias` 类型别名
   - `Callable`、`Literal`、`TypedDict`
   - mypy 工具简介：静态类型检查

3. **异常处理体系**
   - 异常层次：`BaseException` → `Exception` → 具体异常
   - `try / except / else / finally` 完整语法
   - 多异常捕获：`except (TypeError, ValueError) as e:`
   - Java 对比：Python 没有 checked exception，所有异常都是 unchecked 的

4. **异常的最佳实践**
   - EAFP vs LBYL：Python 倾向 "先做再说"（try），Java 倾向 "先检查再做"（if）
   - 自定义异常类：继承 `Exception`，不要继承 `BaseException`
   - 异常链：`raise NewError() from original_error`
   - 什么时候该抛异常、什么时候该返回 None/默认值

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

### Day 10：模块/包管理 + 并发入门

**学习目标**：搞清 import 机制和包结构，了解 Python 并发的基本概念

#### 知识点

1. **模块与包**
   - 模块 = 一个 `.py` 文件，包 = 一个含 `__init__.py` 的目录
   - `import` 的查找路径：`sys.path` 的构成
   - 相对导入 vs 绝对导入：什么时候用哪个
   - `__init__.py` 的作用：包初始化、控制 `from pkg import *`
   - Java 对比：Python 的 import = Java 的 import，但 Python 的 `sys.path` ≈ Java 的 classpath

2. **虚拟环境与依赖管理**
   - `venv` 创建虚拟环境的原理和用法
   - `pip` + `requirements.txt` 基本工作流
   - `pyproject.toml` 现代项目配置（了解）
   - Java 对比：`venv` ≈ 项目级隔离，`pip` ≈ Maven/Gradle 依赖管理

3. **并发基础概念（了解）**
   - GIL 是什么：为什么 Python 多线程不能真正并行计算
   - 三种并发方案对比：
     - `threading`：适合 I/O 密集型
     - `multiprocessing`：适合 CPU 密集型
     - `asyncio`：适合大量 I/O 并发（网络请求等）
   - Java 对比：Java 没有 GIL，多线程是真并行；Python 的 `asyncio` ≈ Java 的 `CompletableFuture` + NIO

4. **asyncio 入门（了解）**
   - `async def` 和 `await` 的基本语法
   - `asyncio.run()` 启动事件循环
   - `asyncio.gather()` 并发执行多个协程
   - 什么时候该用 async：大量网络 I/O（爬虫、API 调用）

#### 练习题（导师出题）
- 题目将在学习当天由导师给出

---

## 学习方式说明

### 每天的学习流程

```
1. 阅读当天的知识点  （30 分钟）
2. 动手写代码验证    （60 分钟）
3. 完成导师出的练习题 （30-60 分钟）
4. 导师批改 + 讲解   （30 分钟）
```

### 教学约定

1. **Java 对比**：每个核心概念都会对比 Java 的对应物，帮助你快速建立映射关系
2. **边做边学**：鼓励你先动手试，遇到问题再问，而不是先看完所有理论
3. **导师出题批改**：每天学完后我会出 2-3 道练习题，你完成后我来批改讲解
4. **不懂就问**：任何时候可以打断问问题，不用等到练习环节

### 学习资源

- 本仓库 `python-base/` 中的现有示例可以作为补充参考
- Python 官方文档：https://docs.python.org/3/
- Python 官方教程（中文）：https://docs.python.org/zh-cn/3/tutorial/

---

## 准备开始

当你准备好开始 Day 1 的学习时，告诉我：**"开始 Day 1"**，我会：
1. 展开当天的知识点详细讲解
2. 给出可运行的代码示例
3. 出练习题让你完成

**Let's go! 🐍**
