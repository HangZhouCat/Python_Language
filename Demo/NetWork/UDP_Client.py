# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 上午12:23
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : UDP_Client.py
# @Software: PyCharm

import socket

target_host = '127.0.0.1'
target_port = 80

#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#发送一些数据
data = bytes('AAABBBCCC', encoding='utf-8')

client.sendto(data, (target_host, target_port))

#接收一些数据

data, addr = client.recvfrom(4096)

print(data)
