from multiprocessing import Process, current_process, Queue
import time
import os

"""
Author : revi1337
Date : 2022-08-18
"""

def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    q.put(sub_total)
    print("Process ID : {}, Process Name : {}, id : {}".format(process_id, process_name, id))
    print("Result : {}".format(sub_total))


def main():
    parent_process_id = os.getpid()
    print("[+] Parent Process ID : {}".format(parent_process_id))

    processes = list()
    start_time = time.perf_counter()
    q = Queue()
    for i in range(5):
        t = Process(name = str(i), target = worker, args = (i, 100000000, q))
        processes.append(t)
        t.start()
    for process in processes:
        process.join()

    print("--- %s Seconds ---" % (time.perf_counter() - start_time))
    q.put('exit')

    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
    print()
    print("[+] Main-Processing Total Count : {}",format(total))
    print('[+] Main-Processing Done')

if __name__ == '__main__':
    main()