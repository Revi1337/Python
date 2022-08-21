import multiprocessing
import requests
import time

"""
IO Bounds, Sync_Blocking - Threading vs asyncio vs multiprocessing
    processing
"""

"""
Author : revi1337
Date : 2022-08-21
"""

session = None
def set_global_session():
    global session
    if not session:
        session = requests.Session()


def request_site(url):
    print(session)
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"Name : {name}, Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}")


def request_all_sites(urls):
    # Whenever each process is created, it enters with a session by calling set_global_session.
    with multiprocessing.Pool(initializer = set_global_session, processes = 4) as pool:
        pool.map(request_site, urls)


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