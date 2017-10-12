# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 上午12:52
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : TCP_Server.py
# @Software: PyCharm

import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)    #最大连接数为5

print('[*] Listening on %s:%d ' % (bind_ip, bind_port))

#这是客户处理线程

def handle_client(client_socket):


    #打印出客户端发送得到内容
    request = client_socket.recv(1024)

    print('[*] Received: %s ' % request)

    #返还一个数据包

    client_socket.send('ACK!')

    client_socket.close()



while True:
    client, addr = server.accept()  #将接收到的客户端套接字对象保存到client变量中，将远程连接的细节保存到addr变量中。

    print('【*】Accepted Connection from: %s:%d' % (addr[0], addr[1]))


    #挂起客户端线程，处理传入的数据

    client_handler = threading.Thread(target=handle_client, args=(client, ))

    client_handler.start()