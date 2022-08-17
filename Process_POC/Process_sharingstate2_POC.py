from multiprocessing import current_process, Process, Value, Array
import os
import logging

"""
Author : revi1337
Date : 2022-08-17
"""

# Process Can Share Value POC
def generate_update_number(v: int):
    for _ in range(5000):
        v.value += 1
    print("[+] Child Process : {}, PID : {}, Value : {}".format(current_process().name, current_process().pid, v.value))

def main():
    parent_process_id = os.getpid()
    logging.info("[+] Parent Process PID : {}".format(parent_process_id))
    print()

    processes = list() 
    share_value = Value('i', 0) 
    # Share Value Must Specify Data Type (i -> int, c -> char, f -> float)
    # share_numbers = Array('i', range(50))   # Share Array
    for _ in range(1, 10):
        p = Process(target = generate_update_number, args = (share_value,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()

    print()
    logging.info("[!] Process Can Sharing Value (By Using Value(), Array())")
    logging.info("[-] Final Sharing Value : {}".format(share_value))
    logging.info("[-] Expected Value is 45000. But It's not Correct. It Must be Synchronize")

if __name__ == '__main__':
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")
    main()