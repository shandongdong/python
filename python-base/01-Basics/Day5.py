  # === 没有 yield from ===
def chain_manual(*iterables):
    for it in iterables:
        for item in it:
            yield item

print(list(chain_manual([1, 2, 3], [4, 5, 6])))


  # === 用 yield from 简化 ===
def chain_simple(*iterables):
    for it in iterables:
        yield from it
print(list(chain_simple([1, 2, 3], [4, 5, 6])))

# 生成器：函数包含 yield 关键字，返回的是迭代器（生成器对象）
def countdown(n):
    while n > 0:
        yield n
        n -= 1
result = countdown(5)
print(next(result))     # 5
print(next(result))     # 4
print(next(result))     # 3
print(next(result))     # 2
print(next(result))     # 1

print(f'偶数生成器：')
def even_numbers(n):
    for i in range(n) :
        if i % 2 == 0:
            yield i
result = even_numbers(5)
print(next(result))     # 0
print(next(result))     # 2
print(next(result))     # 4
