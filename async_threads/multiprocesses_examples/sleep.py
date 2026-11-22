import multiprocessing
import time
"""
For I use a MacBook, the MacOS uses spawn when creating a new process, causing the file to be ran 3 times(needs to use __name__ verification) and also the stdout buffer is not printed so it will be deleted after the processes ends execution, meaning nothing will appear on the screen. flush=True kicks in and says "You right there, throw up the content of your buffer" and fixs our issue.
"""


def process_one():
    time.sleep(1)
    print("first", flush=True)

def process_second():
    time.sleep(2)
    print("second", flush=True)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=process_one)
    p2 = multiprocessing.Process(target=process_second)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
