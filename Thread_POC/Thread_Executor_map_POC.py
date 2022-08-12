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

    logging.info("Main-Thread : Sub-Thread Start")
    with ThreadPoolExecutor(max_workers = 10) as executor:
        res = executor.map(task, [('First', 1000000), ('Second', 10000000), ('Third', 100010000), ('Fourth', 599991900), ('Fifth', 10000000)])
        print()
        print(list(res))

    logging.info("Main-Thread : executor.map() waits for the subthread to finish")
    

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")
    main()