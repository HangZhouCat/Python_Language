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
        print('thread %s >> %s')

    pass

def Main():
    pass

if __name__ == '__main__':
    pass