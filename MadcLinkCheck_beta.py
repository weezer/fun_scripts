'''
Created on Apr 21, 2014
http://apc-wgmdcma201/
http://www.moodysanalytics.com/
@author: SuW
'''
import requests, re, csv, time, sys
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from requests.adapters import HTTPAdapter

regst = re.compile(r'20[\d]')

def response_parser(url):
    r = requests.get(url)
#     print_url(url)
#     if 'pdf' not in r.headers['content-type']:
#         q_home.put(url)
    urlList = get_urls_from_response(r.text)
    return urlList

def get_urls_from_response(r):
    soup = BeautifulSoup(r)
    
    urlList = [link.get('href') for link in soup.findAll('a') if link.get('href') is not None and link.get('href').startswith('/')]
            
    return urlList

class AppendUrl:
    def __init__(self, baseUrl):
        self.url = baseUrl
        
    def appendUrl(self, URI):
        return self.url + str(URI)  


s = requests.Session()
s.mount("http://", HTTPAdapter(max_retries=5))
       
def getResponse(url):
    return get_urls_from_response(s.get(url).content)

def urlChecker(url):
    aspxChecker = " "
    reqResult = "Passed"
    r = requests.get(url)
#     if r.headers.has_key('content-type') is not None and 'text/html' in r.headers['content-type'] and 'aspx' in r.url:
#         aspxChecker = "aspx error"
    if regst.search(str(r.status_code)) is not None:
        if r.url.find('error') != -1:
            text = r.text.upper()
            if text.find('SERVER INTERNAL ERROR') != -1:
                reqResult = '500 SERVER INTERNAL ERROR'
            else:
                reqResult = '400 Client Error'
    elif r.status_code > 400 and r.status_code < 500:
        reqResult = '400 Client Error'
    elif r.status_code > 500:
        reqResult = '500 SERVER INTERNAL ERROR'
    
    return [url, reqResult, aspxChecker]


if __name__ == "__main__":
    start_time = time.time()
    for arg in sys.argv:
            url = sys.argv[1]
    
    if url.startswith("http") is not True:
        url = "http://apc-wgmdcma201/"
    
    lst = response_parser(url)
    print lst
    lst = map(AppendUrl(url).appendUrl, lst)
    print len(lst)
#     print lst
    pool = ThreadPool(20)
    results = pool.map(getResponse, lst)
    urlSet = set()
    for i in results:
        urlSet.update(i)
    
    lst = map(AppendUrl(url).appendUrl, urlSet)
    
    madcResult = pool.map(urlChecker, lst)
    
#     print str(urlSet) + " " + str(len(urlSet))
    csvfile = file(r'./urlList.csv', 'wb')
    writer = csv.writer(csvfile)
    for i in madcResult:
        writer.writerow(tuple(i))
    print time.time() - start_time
#     lst = map(requests.get, lst)
#     print lst