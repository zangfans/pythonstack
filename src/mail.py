#!/usr/bin/env python
'''
代码说明：自动发送邮件
编写日期：2018.07.16
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def send_email(filename):
    #   打开报告文件读取文件内容
    #filename = './report/'+ time.strftime('%Y-%m-%d %H_%M_%S')
    f = open(filename,'r')
    file_msg = f.read()
    #print(filename)
    #print(file_msg)
    f.close()

    #   邮件服务器
    smtpserver = 'smtp.163.com'
    #   发件人用户名和密码
    user = 'zf_strange@163.com'
    password = 'andme1024'
    #   发件人
    sender = 'zf_strange@163.com'
    #   收件人
    receiver = 'zang.fan@cnmo.com'
    #   邮件主题
    subject = 'Python'
    #   邮件设置
    msg = MIMEText(file_msg,'html','utf-8')
    msg['subject'] = Header(subject,'utf-8')
    msg['from'] = sender
    #   连接服务器，登录服务器，发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user,password)
    try:
        smtp.sendmail(sender,receiver,msg.as_string())
    except Exception as e:
        print('send failed',e)
    else:
        print('send success！')
    smtp.quit()#   结束SMTP会话
    print('send email success!')
if __name__ == '__main__':
    send_email('./test.txt')