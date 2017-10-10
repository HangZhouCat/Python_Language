# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 上午12:10
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : TCP_Client.py
# @Software: PyCharm

import socket

target_host = 'www.baidu.com'
target_port = 80

#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接客户端
client.connect((target_host, target_port))

#发送一些数据
data = bytes('GET / HTTP/1.1\r\nHOST: baidu.com\r\n\r\n',encoding='utf-8')
client.send(data)

#接收一些数据
response = client.recv(4096)

print(response)
