from concurrent.futures import ThreadPoolExecutor
import threading
import requests
import time

"""
IO Bounds, Sync_Blocking - Threading vs asyncio vs multiprocessing
    Threading
"""

"""
Author : revi1337
Date : 2022-08-21
"""

# This method is used when you want to use each session for each thread.
# This is a method to solve the characteristic of threads that share memory.
# This means that each thread uses a separate NameSpace.
# Since max_workers is 4, 4 sessions are created.
# Since the workload (url) is 15, one session per thread fits 3-4 URLs.

thread_local = threading.local()        # Dict

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def request_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}")


def request_all_sites(urls):
    with ThreadPoolExecutor(max_workers = 4) as executor:
        executor.map(request_site, urls)


def main():
    urls = [
        "https://www.jython.org",
        "https://realpython.com",
        "https://dnsdumpster.com/"
    ] * 5

    start_time = time.time()
    request_all_sites(urls)
    duration_time =  time.time() - start_time

    print()
    print("[+] Download {} sites in {} seconds".format(len(urls), duration_time))


if __name__ == '__main__':
    main()