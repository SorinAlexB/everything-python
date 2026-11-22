# Python asyncio and threads

## Threads

Threads are components that are managed by the OS and paralize the workload between physical threads that run on CPU cores

## GIL

CPython's GIL(Global Interpreter Lock) manages threads in python. These threads are not concurent due to its limitations, but they shine when there are *blocking blocks*(the only actual case when python threads are concurent)

## asyncio

The asyncio module works only on *one thread* but manages different *tasks* when they are available(same analogy of threads states, but with tasks). However, the downfall is the thing that threads do best in python, async instructions will block in *blocking blocks*.

## Use Cases:
-> I/O bound use asyncio with unblocking libraries or executors that runs the event loop
-> CPU bound use multiprocesses
