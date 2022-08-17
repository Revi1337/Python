from multiprocessing import current_process, Process
import os
import logging

"""
Author : revi1337
Date : 2022-08-17
"""

# Process not Share Value POC
def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print("[+] Child Process : {}, PID : {}, Value : {}".format(current_process().name, current_process().pid, v))

def main():
    parent_process_id = os.getpid()
    logging.info("[+] Parent Process PID : {}".format(parent_process_id))
    print()

    processes = list()
    share_value = 0
    for _ in range(1, 10):
        p = Process(target = generate_update_number, args = (share_value,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()

    print()
    logging.info("[!] Process not Sharing Value.")
    logging.info("[!] Final Sharing Value : {}".format(share_value))

if __name__ == '__main__':
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")
    main()