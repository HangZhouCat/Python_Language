# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 下午1:36
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Thread_Lock.py
# @Software: PyCharm
'''

    多进程和多线程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。
    而多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于
    多个线程同时修改一个变量，把内容给改乱了。

'''
import time,threading

#假设这是银行存款

balance = 0
thread_lock = threading.Lock()

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_No_Lock_thread(n):
    for i in  range(100000):
        change_it(n)


def run_Use_Lock_thread(n):
    for i in range(100000):
        #先获得锁
        thread_lock.acquire()
        try:
            change_it(n)
        finally:
            #改完了一定要释放锁
            thread_lock.release()
        '''
        
        获得锁的线程用完以后一定要释放锁，否则等待锁的线程将永远等待下去，成为死线程，所有用try...finally来确保锁一定会被释放，
        
        '''




def Main():
    t1 = threading.Thread(target=run_Use_Lock_thread, args=(5, ))
    t2 = threading.Thread(target=run_Use_Lock_thread, args=(8, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
if __name__ == '__main__':
    Main()