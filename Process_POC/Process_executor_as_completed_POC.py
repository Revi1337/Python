import timeit
import logging
from concurrent.futures import ProcessPoolExecutor, wait, as_completed
from os import getpid
import requests
from bs4 import BeautifulSoup

"""
Author : revi1337
Date : 2022-08-16
"""

URLS = [
    'http://google.com',
    'https://www.shodan.io/',
    'https://www.exploit-db.com/',
    'https://dnsdumpster.com/',
    'https://www.hackthebox.com/'
]

def scraping_web(url):
    text = requests.get(url).text
    title = BeautifulSoup(text, 'html.parser').title.text
    return title

def main():
    logging.info("[+] Parent-Process Started (PID : {})".format(getpid()))
    print()
    with ProcessPoolExecutor(max_workers = len(URLS)) as executor:
        processes = [
            executor.submit(scraping_web, url) for url in URLS   
        ]
        logging.info("[+] Child-Processes Started")
        logging.info("[!] as_completed() use in Executor and Instead of waiting for all tasks to finish, return a value each time the task is finished.")
        logging.info("[!] Parent-Process waits until Child-Process created by wait() and as_completed() used in Executor is finished.")
        for process in as_completed(processes):
            print("Title Name : {}".format(process.result()))
        logging.info("[+] Child-Processes Finished")

if __name__ == '__main__':
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")
    start_time = timeit.default_timer()
    main()
    duration_time = timeit.default_timer() - start_time
    print()
    logging.info("[+] Parent-Process Finished")
    print("Total Running Time : %r" % duration_time)