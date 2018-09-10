from concurrent.futures import ThreadPoolExecutor
import time

def task(arg):
    print(arg)
    time.sleep(1)


pool = ThreadPoolExecutor(10)

for i in range(50):
    pool.submit(task,i)