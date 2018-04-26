# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 上午10:13
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Pillow_Demo.py
# @Software: PyCharm
from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

password = 'BBFFD6CD826BCD00'

PADDING = '{'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

EncodeAES = lambda c,s : base64.b64encode(c.encrypt(pad(s)))

#DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

secret = os.urandom(BLOCK_SIZE)

cipher = AES.new(secret)

encoded = EncodeAES(cipher, password)

#decoded = DecodeAES(cipher, encoded)

print('Encrypted String:{}'.format(encoded))

#print('Decrypted String:{}'.format(decoded))
