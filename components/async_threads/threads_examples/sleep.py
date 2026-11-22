import threading
import time

def thread_one() -> None:
    time.sleep(1)
    print("first thread")

def thread_two() -> None:
    time.sleep(2)
    print("second thread")

t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)

t2.start()
t1.start()

t2.join()
t1.join()

