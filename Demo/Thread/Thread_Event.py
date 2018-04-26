'''

Python线程事件测试学习代码

'''

import threading
import time




num = 0
lock = threading.RLock()

def Demo(kar98):
    lock.acquire()
    try:
        time.sleep(1)
        print(kar98)
    finally:
        lock.release()





if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=Demo,args=(i,))
        t.start()