# -*- coding:UTF-8 -*-

import smtplib
import email
from email.message import Message
from email.mime.text import MIMEText
import configparser

#发送邮件的服务器信息
configer=configparser.ConfigParser()
configer.read("email.ini")
smtp = configer["smtp"]
smtp_server=smtp["server"]
user=smtp["username"]
passwd=smtp["passwd"]
port=smtp["port"]

#登陆邮件服务器
def login():
    server=smtplib.SMTP(smtp_server, port)
#    server.ehlo()
    server.login(user, passwd)
    return server

#发送邮件
def sendTextEmail(toAddress, subject, content):
    server=login()
    msg=Message()
#    msg['Mime-Version']='1.0'
    msg['From']=user
    msg['To']=toAddress
    msg['Subject']=subject
#    msg['Date']=email.utils.formatdate()
    msg.set_payload(content)
    mail_status=server.sendmail(user,toAddress,str(msg))
    return mail_status

#测试
if __name__ == '__main__':
    sendTextEmail('five1987@gmail.com', 'Python致函1', 'Sport for life.')
    print("send email success.")

'''
    print("Hello World")
    cfgParser = configparser.ConfigParser()
    cfgParser.read("email.ini")
    cfgInfos = cfgParser.sections()
    print(cfgInfos)
    print(cfgInfos[1])
    print(type(cfgInfos))
'''
