import requests
import shadowsocks
from stem import Signal
from stem.control import Controller
url = 'http://www.ident.me'



ip = '127.0.0.1'
port = '1080'



zhima_url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=&city=0&yys=0&port=1&pack=11150&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='

proxies_result = requests.get(zhima_url).json()


ok_proxies = []


success_num = 0

def jianyan():
    with open('ip.txt') as f:
        result = f.read()
        result = result.split('\n')
    for ip_port in result:
        ip_port = ip_port.split(':')
        ip = ip_port[0]
        port = ip_port[1]
        proxies = {
                'http': 'http://{}:{}'.format(ip, port),
                'https': 'https://{}:{}'.format(ip, port),
        }
        print(proxies)
        try:
            rp = requests.get(url,proxies=proxies,timeout=5).text
            print(rp)
            success_num = success_num + 1
        except:
            print(ip,'不能使用')
    print('成功可用的代理数目为: {}'.format(success_num))


def Demo():
    controller = Controller.from_port(port=9151)
    proxies = {
        'http': 'socks5://127.0.0.1:9150',
        'https': 'socks5://127.0.0.1:9150',
    }

    result = requests.get(url,proxies=proxies).text
    print(result)
    controller.signal(Signal.NEWNYM)
    result = requests.get(url, proxies=proxies).text
    print(result)



def DaXiangIP():
    API_URL = 'http://pvt.daxiangdaili.com/ip/?tid=557021530640380&num=1000'
    response = requests.get(API_URL)
    print(response)
    with open('ip.txt','w') as file:
        file.write(response.text)


'''

https://github.com/qiyeboy/IPProxyPool

'''




if __name__ == '__main__':
    #print(shadowsocks.division)
    # Demo()
    #DaXiangIP()
    jianyan()
    # print('连接率为:',success_num/20)