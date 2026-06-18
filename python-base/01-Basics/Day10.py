"""
Python Async: Python 异步编程基础

async def ：声明这是一个协程函数，调用它不会立即执行，而是返回一个协程对象。

await ：等待一个异步操作完成，等待期间让出控制权，事件循环可以去执行其他协程。

"""
import asyncio


print("======== async await 基础语法 =========")

# async def 定义协程函数
async def cook(name, seconds):
    print(f"开始做 {name}...")
    await asyncio.sleep(seconds)   # await：异步等待，不阻塞，让出控制权，比如：异步等待第三方处理完毕。不加 await 程序会直接往下执行，不会等待异步操作完成
    print(f"{name} 好了！用了 {seconds} 秒")
    return name

# asyncio.sleep() 是异步版的 time.sleep()
# time.sleep()  → 阻塞，整个线程停下来等
# asyncio.sleep() → 非阻塞，告诉事件循环"我等几秒，你先去干别的"


asyncio.run(cook("鱼香肉丝", 2))
asyncio.run(cook("红烧肉", 3))


print("======== 事件循环与 asyncio.run() =========")

import asyncio

async def cook(name, seconds):
    print(f"开始做 {name}...")
    await asyncio.sleep(seconds)
    print(f"{name} 好了！")
    return name

async def main():
    # 串行执行：总共 5 秒
    await cook("菜1", 1)
    await cook("菜2", 2)
    await cook("菜3", 3)

# asyncio.run() 启动事件循环，运行 main 协程
asyncio.run(main())

print("======== 并发执行 —— asyncio.gather() =========")
"""
时间轴 →

协程1:  cook("菜1",1)  ──await sleep(1)──┐  ← 让出控制权                     ┌──恢复──打印"菜1好了"
协程2:  cook("菜2",1)  ──await sleep(1)──┤  ← 让出控制权                     ├──恢复──打印"菜2好了"
协程3:  cook("菜3",1)  ──await sleep(1)──┘  ← 让出控制权                     └──恢复──打印"菜3好了"
                                           │                                       │
事件循环:                         收到3个sleep请求，同时计时          1秒后依次唤醒
"""
import asyncio

async def cook(name, seconds):
    print(f"开始做 {name}...")
    await asyncio.sleep(seconds)
    print(f"{name} 好了！")
    return name

async def main():
    # 并发执行：3 道菜同时做，总共只要 1 秒！
    results = await asyncio.gather(
        cook("菜1", 1),
        cook("菜2", 1),
        cook("菜3", 1),
    )
    print(results)  # ["菜1", "菜2", "菜3"]

asyncio.run(main())