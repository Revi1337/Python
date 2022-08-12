import logging
from concurrent.futures import ThreadPoolExecutor
from operator import add
from functools import reduce

"""
Author : revi1337
Date : 2022-08-12
"""

def task(args): 
    logging.info("Sub-Thread : {} Sub-Thread Running...".format(args[0]))
    res = reduce(add, range(args[1] + 1))
    logging.info("Sub-Thread : {} Sub-Thread Completed...".format(args[0]))
    return res


def main():
    logging.info("Main-Thread : Before Creating Sub-Thread")
    
    logging.info("Main-Thread : Create Sub-Threads. But not run")
    executor = ThreadPoolExecutor(max_workers = 10)

    logging.info("Main-Thread : Sub-Thread Start")
    task1 = executor.submit(task, ('First', 100000000,))
    task2 = executor.submit(task, ('Second', 100,))
    task3 = executor.submit(task, ('Third', 10000,))
    task4 = executor.submit(task, ('Fourth', 99990,))
    task5 = executor.submit(task, ('Fifth', 200000000))

    print(task1.result())    
    print(task2.result())
    print(task3.result())
    print(task4.result())
    print(task5.result())

    print()
    logging.info("Main-Thread : executor.submit() wait for the Sub-Thread to finish and can confirm return \
        value by .result()")
    

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")
    main()