import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(10)
    print("Hello again!")

# @asyncio.coroutine
def batch_hello():
    tasks = []
    for i in range(10):
        tasks.append(hello())
    return tasks

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(hello())
loop.run_until_complete(asyncio.wait(batch_hello()))
loop.close()