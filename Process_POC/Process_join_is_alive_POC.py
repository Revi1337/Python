import logging
from multiprocessing import Process, current_process
import time
import random 
import os

"""
Author : revi1337
Date : 2022-08-15
"""

def task(sec):
    child_process_name = current_process().name
    child_process_pid = current_process().pid
    print("Named {} Child Process Started (PID : {}, sleep {} seconds)".format(child_process_name, child_process_pid, sec))
    print("Named {} Child Process Running? : {}".format(current_process().name, current_process().is_alive()))
    time.sleep(sec)
    print("Named {} Child Process Finished!".format(child_process_name))


def main():
    logging.info("[+] Parent Process Started ( PID : {})".format(os.getpid()))    
    print()

    logging.info("[+] Several Child Processes  Created")
    processes = list()
    for i in range(4):
        sec = random.randint(1,7)
        p = Process(name = str(i) , target = task, args = (sec,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    for process in processes:
        print("Named {} Child Process Running? : {}".format(process.name, process.is_alive()))

    print()
    logging.info("[+] Parent Process Finished. .join() methods wait for Child-Process til done")
    print()


if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")
    main()