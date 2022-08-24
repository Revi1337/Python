import time

"""
CPU Bounds, Sync
CPU Bounds
"""

"""
Author : revi1337
Date : 2022-08-24
"""

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    print(numbers)
    print()
    
    start_time = time.time()

    total = find_sums(numbers)
    print(f"Total List : {total}")
    print(f"Sum : {sum(total)}")

    duration_time = time.time() - start_time
    print(f"Duration : {duration_time}")

if __name__ == '__main__':
    main()