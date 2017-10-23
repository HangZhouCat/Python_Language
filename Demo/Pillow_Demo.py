# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 上午10:13
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Pillow_Demo.py
# @Software: PyCharm

'''

Python图形处理库，Pillow测试代码

'''

from PIL import Image
#导入滤镜
from PIL import ImageFilter

image = Image.open('Photo/1.jpg')   #创建Image对象


def Demo():
    '''

    批量检测Photo目录下

    :return:
    '''
    for i in range(101):
        image = Image.open('Photo/%d.jpg' % i)
        print(image.format, image.size, image.mode)


def Roll(image, delta):

    '''

    翻转图像

    :param image:
    :param data:
    :return:
    '''

    xsize, ysize = image.size

    if delta == 0:
        return image

    part1 = image.crope()

    pass
def Geometric_Transformation():

    '''

    几何变换

    :return:
    '''

    pass


def Color_Conversion():

    '''


    色彩转换

    :return:
    '''

    pass


def Image_Demo():
    '''

    Pillow的核心模块Image测试代码.

    :return:
    '''

    print(image.format, image.size, image.mode)

    pass





def Main():
    Image_Demo()

if __name__ == '__main__':
    #Main()
    Demo()