#import requests
#import bs4
import argparse
print("test")

# if __name__ == '__main__':
#     pass

#命令行参数处理
parser = argparse.ArgumentParser()
parser.add_argument('filename')   #输入文件
parser.add_argument('-o', '--output')  #输入文件
parser.add_argument('--width', type= int , default=80)  #输出字符画度
parser.add_argument('--height', type= int, default=80)  #输出字符画高