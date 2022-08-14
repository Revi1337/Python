"""
Section 1
MultiThreading - Thread(4) - Prod vs Cons Using Queue
Keyword - 생산자 소비자 패턴(Producer / Consumer Pattern)
"""
"""
Producer - Consumer Pattern
(1). 멀티스레드 디자인 패턴의 정석이라고 볼 수 있음.
(2). 서버측 프로그래밍의 핵심
(3). 주로 허리역할을 하는 중요한 역할

Python Event 객체 (무조건 외워라)
(1). Flag 초기값 (0)
(2). Set() -> 1 로 바꿔줌
     Clear() -> 0
     Wait() -> 0 : 리턴, Wait() -> 1 : 대기
     is_set() -> 현 플래그 상태.
"""

import concurrent.futures 
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    """ 네트워크 대기 상태라 가정 (서버) """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info('Producer got message : %s', message)
        queue.put(message)
    logging.info('Producer redeived event')


# 소비자
def consumer(queue, event):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장 """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info('Consumer storing message : %s (size = %d)', message, queue.qsize())
    logging.info('Consumer redeived event Exiting')


if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize = 10)

    # 이벤트 플래그 초기값 0
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info('Main : About to set Event')
        event.set()