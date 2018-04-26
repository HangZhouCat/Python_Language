from urllib import request
import requests


def demo():
    # 要访问的目标页面
    targetUrl = "http://test.abuyun.com/proxy.php"

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H129OKE981W5DU3D"
    proxyPass = "57559880F4283685"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxy_handler = request.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })

    # auth = request.HTTPBasicAuthHandler()
    # opener = request.build_opener(proxy_handler, auth, request.HTTPHandler)

    opener = request.build_opener(proxy_handler)

    request.install_opener(opener)
    resp = request.urlopen(targetUrl).read()

    print(resp)

def MyDemo():

    tarGetUrl = 'http://ident.me'

    proxyUser = 'H129OKE981W5DU3D'
    proxyPass = '57559880F4283685'

    proxies = {
        "http": "http://{}:{}@http-dyn.abuyun.com:9020".format(proxyUser,proxyPass),
    }

    response = requests.get(tarGetUrl,proxies=proxies)

    print(response.text)


if __name__ == '__main__':
    MyDemo()