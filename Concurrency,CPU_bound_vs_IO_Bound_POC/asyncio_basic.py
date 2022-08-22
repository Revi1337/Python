import asyncio
import time
import logging

"""
IO Bounds, Sync_Blocking (4) - Threading vs asyncio vs multiprocessing
asyncio
"""
"""
async + io
    - 비동기적으로 INPUT OUTPUT 작업할수있게하는 패키지
    - 실행할 함수가 Blocking이면 효과가 미미. (Non-Blocking이어야 함.)
"""

"""
비동기함수는 async로 선언하고
async함수에서 다른 비동기함수를 실행할때는 꼭 await 을 붙여줘서 실행해야함.
"""

def exe_calculate_sync(name: str, n: int):
    for i in range(1, n + 1):
        print('{} -> {} of {} is calculating'.format(name, i, n))
        time.sleep(1)
    print('{} - {} Working Done'.format(name, n))


def process_sync():
    start = time.time()
    exe_calculate_sync('One', 1)
    exe_calculate_sync('two', 2)
    exe_calculate_sync('three', 3)
    end = time.time()

    print('>>> Total Seconds {}'.format(end - start))


async def exe_calculate_async(name: str, n: int):
    for i in range(1, n + 1):
        print('{} -> {} of {} is calculating'.format(name, i, n))
        await asyncio.sleep(1) 
    print('{} - {} Working Done'.format(name, n))


async def process_async():
    start = time.time()
    # 여러개를 묶어서 실행.
    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('two', 2),
        exe_calculate_async('three', 1)
    ])
    end = time.time()

    print('>>> Total Seconds {}'.format(end - start))


if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s", level = logging.INFO, datefmt = "%H:%M:%S")
    # Sync 실행
    # logging.info("[+] Starting Sync functions")
    # process_sync()
    

    # Async 실행
    logging.info("[+] Starting ASync functions")
    # Python 3.7 이상
    # asyncio.run(process_async())
    # Python 3.7 이하
    asyncio.get_event_loop().run_until_complete(process_async())

