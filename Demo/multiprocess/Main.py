# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 下午12:09
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : main.py
# @Software: PyCharm

from multiprocessing import Process, Pool
import os, time, random

def Main():
    More_Process()

def Demo():
    pass


def Single_Process():
    '''

    启动一条子进程

    :return:
    '''
    print('父进程 %s. ' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('子进程将要启动.')
    p.start()
    p.join()    #join方法可以等待子进程结束后再继续往下运行，通常用于子进程间的同步。
    print('子进程结束.')

def More_Process():
    '''

    使用进程池的方式批量创建子进程

    :return:
    '''
    print('父进程 %s.' % os.getpid())
    p = Pool(4)     #使用multiprocess模块中的Pool方法
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('等待所有进程结束...')
    p.close()
    p.join()
    print('所有进程完毕')


    pass

def long_time_task(name):
    print('运行任务 %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 运行 %0.2f 秒.' % (name, (end - start)))
    pass


def run_proc(name):
    print('运行子进程 %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    Main()