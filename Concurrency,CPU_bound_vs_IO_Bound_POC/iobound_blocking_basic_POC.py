import requests
import time

"""
IO Bounds, Sync_Blocking - Threading vs asyncio vs multiprocessing
    Basic
"""

"""
Author : revi1337
Date : 2022-08-21
"""

def request_site(url, session):
    with session.get(url) as response:
        print(f"Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}")


def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


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