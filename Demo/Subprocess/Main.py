# -*- coding: utf-8 -*-
# @Time    : 2017/10/9 下午6:13
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Main.py
# @Software: PyCharm

import subprocess
'''

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入输出。

'''

def Demo():
    '''

    演示如何在Python代码中运行命令nslookup www.python.org。这和命令行直接运行的效果是一样的。

    :return:
    '''
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


def Process_Arg():
    '''

    如何子进程还需要输入，则可以通过communicate()方法输入。

    :return:
    '''

    print('$ nslookup')

    p = subprocess.Popen(['nslookup'], stdin= subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code', p.returncode)

    pass


def Main():
    Process_Arg()

if __name__ == '__main__':
    Main()


