import requests
import re
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """



soup = BeautifulSoup(html_doc,'html.parser') #创建 beautifulsoup 对象

# result = soup.prettify()       #打印一下 soup 对象的内容，格式化输出



'''
找标签


soup加标签名轻松地获取这些标签的内容,
不过有一点是，它查找的是在所有内容中的第一个符合要求的标签
'''
result = soup.title
# result = soup.head
result = soup.a
result = soup.p      #直接打印标签



'''


对于标签，它有两个重要的属性，是 name 和 attrs


'''

# result = soup.name
# result = soup.head.name





#result = soup.p['class']           #单独获取某个属性

result = soup.b.string             #获取标签内部的文字



result = soup.a['href']
#result = soup.p.attrs



'''

CSS选择器

'''

result = soup.select('title')       #通过标签名查找
result = soup.select('.sister')     #通过类名查找

result = soup.select('#link1')

result = soup.select('p #link1')    #组合查找，查找 p 标签中，id 等于 link1的内容，二者需要用空格分开


result = soup.select("head > title")    #直接子标签查找


result = soup.select('a[class="sister"]')
result = soup.select('a[href="http://example.com/elsie"]')  #查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。


result = soup.select('p a[href="http://example.com/elsie"]')

'''
属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格




'''

result = soup.select('title')[0].get_text()



print(type(result))

print(result)

for title in soup.select('a'):
    print (title.get_text())

'''
select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
'''
