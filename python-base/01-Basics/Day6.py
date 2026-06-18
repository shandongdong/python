class Counter:
    count = 0    # 类属性
    print("成员变量Counter.count:", count)  

    def __init__(self, name):
        self.name = name
        Counter.count = Counter.count + 1
        print("Counter.count:", Counter.count)
        print("实例变量self.count:", self.count)

a = Counter("a")    
b = Counter("b")    
c = Counter("c")    

print(a)       # 0，1， 1
print("----------------")
print(b)       # 2，2
print("----------------")
print(c)       # 3，3


