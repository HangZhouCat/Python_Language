import requests
from bs4 import BeautifulSoup

url = 'http://www.phei.com.cn/module/goods/searchkey.jsp?goodtypeid=1&goodtypename=%E8%AE%A1%E7%AE%97%E6%9C%BA'

response = requests.get(url)


bs = BeautifulSoup(response.text)

a_lst = bs.find_all('a')

for a in a_lst:
    if a.text != '':
        print(a.text.strip(),a['href'])



