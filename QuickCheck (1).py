'''
Created on Apr 23, 2014

@author: SuW
'''
import requests, re, csv, time, sys
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from requests.adapters import HTTPAdapter
import threading

regst = re.compile(r'20[\d]')
stack = []
visited = set()
quickCheckResult = []

def response_parser(url):
    reqResult = []
    r = s.get(url)
    if regst.search(str(r.status_code)) is not None and 'text/html' in r.headers['content-type']:
        urlList = get_urls_from_response(r.text)
    else:
        urlList = []
        
    result = urlChecker(r)
    result.insert(0, url)
#     print result
    reqResult.append(urlList)
    reqResult.append(result)
    return reqResult

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

def urlChecker(r):
    aspxChecker = " "
    reqResult = "Passed"
#     r = s.get(url)
    if 'text/html' in r.headers['content-type'] and 'aspx' in r.url:
        aspxChecker = "aspx error"
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
    
    return [reqResult, aspxChecker]
            
    
mylock = threading.Lock()

class BFSCheck(threading.Thread):
    
    def __init__(self, url, tname):
        global stack, visited
        threading.Thread.__init__(self)
        self.thread_name = tname
        self.url = url
        visited , stack = set(), [url]
#         print stack
        
    def run(self):    
        global stack, visited
#         print stack
        if len(stack) == 0:
            time.sleep(10)
        while stack:
#             mylock.acquire()
            self.vertex = stack.pop()
            print self.thread_name.ljust(5) + " " + str(len(stack)).ljust(8) + " " + str(len(visited)).ljust(8) + " " + self.vertex 
            if self.vertex not in visited:
                visited.add(self.vertex)
                parsedList = response_parser(self.vertex)[0]
                urlList = map(AppendUrl(self.url).appendUrl, parsedList)
                stack.extend(set(urlList) - visited)
                stack = list(set(stack))
                quickCheckResult.append(response_parser(self.vertex)[1])
#             mylock.release()
            
            
if __name__ == "__main__":
    start_time = time.time()
    thList = []
    url = "http://apc-wgmdcma201/"
    if len(sys.argv) >= 2 :
        for arg in sys.argv:
            url = sys.argv[1]
    
    if url.startswith("http") is not True:
        url = "http://apc-wgmdcma201/"
    
    for i in range(20):
        bfsCheck = BFSCheck(url, 't:' + str(i))
        thList.append(bfsCheck)
    for i in thList:
        i.start()
        
    for i in thList:
        i.join()
    print stack
    print time.time()- start_time
#     print quickCheckResult
    csvfile = file(r'./urlList.csv', 'wb')
    writer = csv.writer(csvfile)
    for i in quickCheckResult:
        writer.writerow(tuple(i))
#     print time.time() - start_time
#     lst = BFS_quickcheck('http://apc-wgmdcma201/')
#     print len(lst)
            
    
            