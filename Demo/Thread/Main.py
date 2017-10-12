# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 下午12:14
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Main.py
# @Software: PyCharm

import threading,time

def loop():
    '''

    新线程执行的代码

    :return:
    '''

    print('thread %s is running...' % threading.current_thread().name )
    n = 0

    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print('thread %s ended,' %threading.current_thread().name)
    '''
    
    current_thread():
它永远返回当前线程的实例，主线程的实例名字叫MainThread，子线程的名字在创建时指定。名字仅仅用来打印时用来显示，
如果不起名字Python就会自动给线程命名Thread-1，Thread-2.... 
    
    '''

def Demo():

    '''

    多进程和多线程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。
    而多线程中

    :return:
    '''


def Main():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop,name='LookThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
    Main()