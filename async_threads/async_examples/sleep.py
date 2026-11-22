import asyncio
import time

async def my_task():
    ...

coro = my_task() #calling it gives a coroutine OBJECT (not run yet)

# await suspend the coroutine, run others, resume when done
async def caller():
    result = await my_task() #yields control here

asyncio.run(caller()) # creates the eventloop for just the caller function and runs until done

async def task(name : str, duration : int) -> str:
    print(f"[{name}] starting")
    await asyncio.sleep(duration) # yields control, event loop run others(non blocking)
    print(f"[{name}] done after {duration}s")
    return f"{name}"

async def main():
    start = time.time()
    # Run tasks SEQUENTIALLY(await one, then the next)
    await task("A", 1)
    await task("B", 2)
    print(f"Sequential: {time.time() - start:.2f}s") # 3 seconds

    start = time.time()
    # Run tasks concurrently(all start, then all awaited)
    results = await asyncio.gather(
            task("A", 1),
            task("B", 2),
            task("C", 3)
            )
    print(f"Concurent: {time.time() - start:.2f}s") # ~3 seconds
    print(f"results: {results}")

asyncio.run(main())




