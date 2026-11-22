import asyncio

# ── Async generator: yield results as they come in
async def stream_data(n):
    for i in range(n):
        await asyncio.sleep(0.1)   # simulate receiving data chunk
        yield i * i                # yield each result

async def main():
    # Consume async generator
    async for value in stream_data(5):
        print(f"Received: {value}")

    # ── Async context manager (aiofiles, aiohttp sessions, etc.)
    # async with aiofiles.open("data.txt") as f:
    #     content = await f.read()

asyncio.run(main())
