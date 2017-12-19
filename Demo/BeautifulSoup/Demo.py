from bs4 import BeautifulSoup

html = u"""<a class='uncheck2 a-hide' jxbh='02080027151001' xf='2'>隐藏</a>
</td>
<td><a href="javascript:void(0)" onclick="courseDet('02080027151001')">电子音乐合成技术与应用</a></td>
<a class='uncheck2 a-hide' jxbh='02080006151001' xf='2'>隐藏</a>
</td>
<td><a href="javascript:void(0)" onclick="courseDet('02080006151001')">电子设计与维修</a></td>"""

bs_obj = BeautifulSoup(html)
a_list = bs_obj.findAll('a', attrs={'jxbh': True})
for a in a_list:
    print(a.attrs['jxbh'])