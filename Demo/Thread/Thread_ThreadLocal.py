# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 下午3:34
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Thread_ThreadLocal.py
# @Software: PyCharm


import threading

#创建全局ThreadLocal对象
local_school = threading.local()
def Process_Student():
    #获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


    pass

def Process_thread(name):
    #绑定ThreadLocal的student

    local_school.student = name

    process_

    pass