# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午10:00
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Get_Scrrent_Shot.py
# @Software: PyCharm

'''

获取屏幕截图

调用PyWin32模块，通过调用本地Windows API的方式实现抓屏功能。

屏幕抓取器利用Windows图形设备接口(GDI)获得抓取屏幕时必要的参数，如屏幕大小、分辨率等信息。

'''

import win32gui
import win32ui
import win32con
import win32api

#获得桌面窗口的句柄
hdesktop = win32gui.GetDesktopWindow()

#获得所有显示屏的像素尺寸

width = win32api.GetSystemMetrics(win32con.)

