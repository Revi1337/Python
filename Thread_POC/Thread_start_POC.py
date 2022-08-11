import logging
import threading
import time

"""
Author : revi1337
Date : 2022-08-11
"""

def task(name, seconds):
    logging.info("Sub-Thread : {} Sub-Thread Running...".format(name))
    time.sleep(seconds)
    logging.info("Sub-Thread : {} Sub-Thread Completed...".format(name))


def main():
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")

    logging.info("Main-Thread : Before Creating Sub-Thread")
    
    logging.info("Main-Thread : Create Sub-Threads. But not run")
    x = threading.Thread(target = task, args = ('First', 2))
    y = threading.Thread(target = task, args = ('Second', 1))
    z = threading.Thread(target = task, args = ('Third', 4))
    r = threading.Thread(target = task, args = ('Fourth', 3))


    logging.info("Main-Thread : Sub-Thread Start")
    x.start()
    y.start()
    z.start()
    r.start()

    logging.info("Main-Thread : Completed")

if __name__ == '__main__':
    main()