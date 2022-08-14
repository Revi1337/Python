"""
Section 1
MultiThreading - Thread(4) - Lock, DeadLock
Keyword - Lock, DeadLock, Race Condition, Thread Synchronization
"""
"""
용어 섦여
(1) 세마포어 (Semaphore) : 프로세스간 공유된 자원에접근시 발생 가능성
    -> 한개의 프로세스만 접근 처리 고안(경쟁 상태 예방)

(2). 뮤텍스(Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 -> (경쟁 상태 예방)
(3). Lock : 상호배제를 위한 잠금(Lock)처리 : 데이터 경쟁
(4). DeadLock : 프로세스가 자원을 획득하지 못해 다음 처리르 못하는 무한 대기 상태
(5). Thread Synchornization(스레드 동기화)를 통해서 안정적으로 동작하게 처리해야 함 (동기화 메서드, 동기화 블럭)
(6). Semaphore와 Mutex의 차이점은?
    -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용함
    -> Mutex는 단일 스레드가 리소스 또는 중요섹션을 소비 허용하는 것이고
    -> 세마포어는 리소스에 대한 제한된 수의 동시 액세스를 허용함.
"""

import logging
import time
from concurrent.futures import ThreadPoolExecutor

class FakeDataStore:
    # 공유 변수 value
    def __init__(self):
        self.value = 0

    # 변수 업데이트
    def update(self, n):
        logging.info('Thread %s: starting update', n)
        # 뮤텍스 & Lock 등 동기화 (Thread Synchronization 필요)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info('Thread %s: finishing update', n)

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s %(message)s", level = logging.INFO, datefmt = "%H:%M:%S")
    
    store = FakeDataStore()
    logging.info("Testing Update. Starting Value is %d", store.value)
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info("Testing Update. Ending Value is %d", store.value)
