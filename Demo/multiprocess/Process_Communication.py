# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 下午12:18
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Process_Communication.py
# @Software: PyCharm

from multiprocessing import Process, Queue
import os, time,random

'''

进程间的通信：
        Python的multiprocess模块包装了底层的机制，提供了Quene、Pipes等多种方式来交换数据。

'''




def write(q):
    '''

    写数据进程执行的代码

    :param q:
    :return:
    '''


    print('Process to write: %s' % os.getpid())

    for value in ['A','B','C']:
        print('Put %s to quene...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    '''



    读数据进程执行的代码


    :param q:
    :return:
    '''
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)



def Main():
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q, ))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程里是死循环，无法等待其结束，智能强行终止
    pr.terminate()

if __name__ == '__main__':
    Main()