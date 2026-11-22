import asyncio
import aiohttp   # pip install aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# Fetch 10 URLs concurrently
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 11)]

start = time.time()
results = asyncio.run(fetch_all(urls))
print(f"Fetched {len(results)} URLs in {time.time()-start:.2f}s")
# Typically 0.3-0.5s instead of 3-5s sequentially
