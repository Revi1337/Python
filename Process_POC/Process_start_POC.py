import logging
from multiprocessing import Process
import time
import random 

"""
Author : revi1337
Date : 2022-08-15
"""

def task(i, sec):
    time.sleep(sec)
    print("{} th Child Process Finished!".format(i))

def main():
    logging.info("[+] Parent Process Started")    
    print()

    logging.info("[+] Several Processes Created and Started")
    for i in range(4):
        sec = random.randint(1,7)
        p = Process(name = str(i) , target = task, args = (i, sec,))
        print("{} th Process Created and Started (sleep {} seconds)".format(i, sec))
        p.start()

    print()
    logging.info("[+] Parent Process Finished. .start() methods not wait for Sub-Process til done")
    print()


if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")
    main()