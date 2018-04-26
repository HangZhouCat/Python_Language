#coding:utf-8

import requests
from queue import Queue
import parser
import threading

class WebDirScan(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._queue = Queue
    def run(self):
        while not self._queue.empty():
            url = self._queue.get()

            #输出url
            try:
                r = requests.get(url=url,timeout=8)
                if r.status_code == 200:
                    print('[*]' + url)
            except:
                pass

def start(url,ext,count):
    queue = Queue()

    with open('./dict/%s.txt'%ext,'r') as f:
        pass

