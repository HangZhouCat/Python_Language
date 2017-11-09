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

    Image类有resize()、rotate()、和transpose()、transform()方法进行几何变换

    :return:
    '''

    out = image.resize((128, 128))  #调整图像大小

    out = image.rotate(45)  #顺时针旋转45度


    out = image.transpose(Image.FLIP_LEFT_RIGHT)    #左右翻转
    out = image.transpose(Image.FLIP_TOP_BOTTOM)    #顶部底部翻转
    out = image.transponse(Image.ROTATE_90)
    out = image.transponse(Image.ROTATE_180)
    out = image.transponse(Image.ROTATE_270)


    '''
    
    transponse()和rotate没有性能差别
    
    更通用的图像变换方法可以使用transform()
    
    
    '''

    pass


def Color_Conversion():

    '''


    色彩转换

    :return:
    '''



    pass


def Schema_Transformation():

    '''

    模式转换

    利用Image类中的convert方法

    :return:
    '''

    out = image.convert('L')

    pass


def Image_Demo():
    '''

    Pillow的核心模块Image测试代码.

    :return:
    '''

    print(image.format, image.size, image.mode)

    pass


def Image_Enhancement():

    '''

    图像增强、像素点处理

    ImageFilter模块包含了很多预定义的增强filters，通过filter()方法使用

    :return:
    '''

    out = image.filter(ImageFilter.DETAIL)


    '''
    像素点处理
    point()方法通过一个函数或者查询表对图像中的像素点进行处理(例如对比度操作)
    '''

    out = image.point(lambda i: i * 1.2)    #把每个像素都乘以1.2

    #上面的point()方法是对图像进行处理，还可以组合point()和paste()选择性地处理图片的某一区域



    #处理单独通道
    source = image.split()

    R, G, B = 0, 1, 2



    pass
def Main():
    Image_Demo()

if __name__ == '__main__':
    #Main()
    Demo()