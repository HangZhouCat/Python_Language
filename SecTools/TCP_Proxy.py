# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 下午1:12
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : TCP_Proxy.py
# @Software: PyCharm

import argparse
import sys
import socket
import threading

def Server_Loop(local_host, local_port, remote_host, remote_port, receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except:
        print('[!!]Filed to listen on %s:%d' % (local_port, local_port))
        print('[!!]Check for other listenning socksts or correct permissions.')
        sys.exit(0)

    print('[*] Listening on %s:%d' %(local_host, local_port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        #打印出本地连接信息

        print('[==>] Received incoming connection from %s:%d' %(addr[0], addr[1]))

        #开启一个线程与远程主机通信

        #proxy_thread = threading.Thread(target=pro)


def proxy_handler(client_socket, remote_host,remote_port, receive_first):

    #连接远程主机
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    remote_socket.connect((remote_host, remote_port))

    #如果必要从远程主机接收数据

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)


        #发送给我们的相应处理

def receive_from(connection):
    '''

    用来接收本地和远程主机的数据

    :param connection:
    :return:
    '''
    pass

def hexdump(src, length=16):
    '''

    十六进制转存函数

    :param src:
    :param length:
    :return:
    '''
    pass

