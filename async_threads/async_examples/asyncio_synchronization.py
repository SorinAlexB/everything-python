import asyncio

# ── asyncio.Lock: same concept as threading.Lock
async def demo_lock():
    lock  = asyncio.Lock()
    counter = 0

    async def safe_increment():
        nonlocal counter
        async with lock:    # non-blocking acquire
            value = counter
            await asyncio.sleep(0)   # yield
            counter = value + 1

    await asyncio.gather(*[safe_increment() for _ in range(100)])
    print(f"Counter: {counter}")   # always 100

# ── asyncio.Semaphore: limit concurrent access
async def demo_semaphore():
    semaphore = asyncio.Semaphore(3)   # max 3 concurrent

    async def limited_task(n):
        async with semaphore:
            print(f"Task {n} running")
            await asyncio.sleep(1)
            print(f"Task {n} done")

    await asyncio.gather(*[limited_task(i) for i in range(10)])

# ── asyncio.Event: signal between coroutines
async def demo_event():
    event = asyncio.Event()

    async def waiter():
        print("Waiting for event...")
        await event.wait()
        print("Event received!")

    async def setter():
        await asyncio.sleep(1)
        print("Setting event")
        event.set()

    await asyncio.gather(waiter(), setter())

asyncio.run(demo_lock())
asyncio.run(demo_semaphore())
asyncio.run(demo_event())
