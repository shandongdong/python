def make_power(n):
    print("n =", n)
    def power(x):
        print("x =", x)
        return x ** n
    return power
make_square = make_power(2)     # n = 2
make_square(2)  # x = 2   不调用的话函数里面的函数 x= 都不会打印。内部函数在被调用时才执行，定义时不执行

'''
装饰器模板
def 装饰器名(func):               # 1. 接收原函数
      def wrapper(*args, **kwargs):   # 2. 定义包装函数
          # 前置操作
          result = func(*args, **kwargs)  # 3. 调用原函数
          # 后置操作
          return result
      return wrapper                 # 4. 返回包装函数
'''
import functools  # 导入functools模块以使用wraps装饰器

def logger(func):
    @functools.wraps(func)
    def log(*args, **kwargs):
        print(f'开始调用函数 {func.__name__}，参数为 {args} {kwargs}') 
        result = func(*args, **kwargs)
        print(f'函数 {func.__name__} 调用结束，返回值为 {result}')
        return result
    return log

log = logger("log")

