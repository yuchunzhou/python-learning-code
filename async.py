import asyncio
import time


async def func1():
    print("func1 is running ...")
    await asyncio.sleep(1)
    print("func1 will exit ...")
    return 1


async def func2():
    print("func2 is running ...")
    await asyncio.sleep(2)
    print("func2 will exit ...")
    return 2


async def func3():
    print("func3 is running ...")
    await asyncio.sleep(3)
    print("func3 will exit ...")
    return 3


async def main():
    result = await asyncio.gather(func1(), func2(), func3())
    print(f"last result: {result}")


start = time.time()
asyncio.run(main())
end = time.time()
print(f"cost time: {end - start}")
