# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 下午8:49
# @Author  : 逍遥哥哥
# @Email   : hellocatmao@gmail.com
# @File    : Send_Email.py
# @Software: PyCharm

'''

SMTP发送邮件代码

'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(), addr)


def Send_Text_Mail():
    '''

    发送纯文本邮件。

    :return:
    '''
    From_addr = 'hellocatmao@gmail.com'
    password = ''
    SMTP_Server = 'smtp.gmail.com'
    To_addr = 'hackxiaoyue@vip.qq.com'
    server = smtplib.SMTP(SMTP_Server, 25)

    # 第一个参数是邮件正文，第二个参数是MIME的subtype,参数plain表示纯文本，最终的MIME就是'text/plain',最后用utf-8编码保证多语言兼容性
    msg = MIMEText('Hello, Send By 逍遥哥哥', 'plain', 'utf-8')
    msg['From'] = _format_addr('ZDH <%s>' % From_addr)
    msg['To'] = _format_addr('Hello <%s>' % To_addr)
    msg['Subject'] = Header('来自SMTP的邮件。。。', 'utf-8').encode()
    # set_debuglevel()可以打印出和SMTP服务器交互的所有信息
    server.set_debuglevel()

    server.login(From_addr, password)
    server.sendmail(From_addr, [To_addr], msg.as_string())  # 邮件正文是一个str，as_string()把MIMEText对象变成str.
    server.quit()

def Send_Accessory_Mail():
    '''

    发送带附件的邮件

    :return:
    '''

    pass




def Main():
    pass


if __name__ == '__main__':
    pass