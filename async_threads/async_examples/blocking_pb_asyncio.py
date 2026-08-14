import asyncio
import time

# ── ❌ BLOCKING CALL INSIDE ASYNC FUNCTION — DESTROYS CONCURRENCY
async def bad_task(name):
    print(f"[{name}] starting")
    time.sleep(2)       # ← THIS BLOCKS THE ENTIRE EVENT LOOP
    # While this sleeps, NO other task can run. asyncio is useless.
    print(f"[{name}] done")

# ── ✅ NON-BLOCKING EQUIVALENT
async def good_task(name):
    print(f"[{name}] starting")
    await asyncio.sleep(2)   # ← yields to event loop, others can run
    print(f"[{name}] done")

# ── What if you MUST use a blocking library?
# Run it in a thread pool so it doesn't block the event loop:
async def task_with_blocking():
    loop = asyncio.get_event_loop()
    # Runs time.sleep in a thread, awaits it non-blockingly
    await loop.run_in_executor(None, time.sleep, 2)
    print("done with blocking call")

asyncio.run(task_with_blocking())
