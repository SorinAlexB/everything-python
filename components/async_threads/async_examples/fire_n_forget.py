import asyncio

async def background_job(name, delay):
    await asyncio.sleep(delay)
    print(f"[{name}] background job done")
    return name

async def main():
    # ── Create tasks: schedule them to run, don't wait immediately
    task_a = asyncio.create_task(background_job("A", 2))
    task_b = asyncio.create_task(background_job("B", 1))

    print("Tasks started, doing other work...")
    await asyncio.sleep(0.5)
    print("Still doing other work...")

    # ── Now wait for them
    result_b = await task_b   # B finishes first (1s delay)
    result_a = await task_a   # A finishes second (2s delay)
    print(f"Results: {result_a}, {result_b}")

asyncio.run(main())
