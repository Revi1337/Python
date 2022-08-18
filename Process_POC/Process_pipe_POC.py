from multiprocessing import Process, current_process, Pipe
import time
import os

"""
Author : revi1337
Date : 2022-08-18
"""

def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
 
    sub_total = 0
    for _ in range(baseNum):
        sub_total += 1

    conn.send(sub_total)
    conn.close()

    print("Process ID : {}, Process Name : {}, id : {}".format(process_id, process_name, id))
    print("Result : {}".format(sub_total))


def main():
    parent_process_id = os.getpid()
    print("[+] Parent Process ID : {}".format(parent_process_id))

    start_time = time.perf_counter()
    parent_conn, child_conn = Pipe()
    
    t = Process(name = str(1), target = worker, args = (1, 100000000, child_conn))
    t.start()
    t.join()

    print("--- %s Seconds ---" % (time.perf_counter() - start_time))
    print()
    print("[+] Main-Processing Total Count : {}",format(parent_conn.recv()))
    print('[+] Main-Processing Done')

if __name__ == '__main__':
    main()