import requests
import timeit

"""
Author : revi1337
Date : 2022-08-20
"""

def request_sites(url, session):
    print(session)
    print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')
    

def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_sites(url, session)

def main():
    urls = [
        'https://www.jython.org',
        'https://www.exploit-db.com/',
        'https://realpython.com'   
    ] * 3 
    
    start_time = timeit.default_timer()
    request_all_sites(urls)
    duration_time = timeit.default_timer() - start_time
    print()
    print(f'Download {len(urls)} sites in {duration_time} seconds')

if __name__ == '__main__':
    main()