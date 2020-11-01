#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
smtplib用来发邮件的
email用来编辑正文
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp = smtplib.SMTP() # 创建对象
smtp.connect('smtp.qq.com',25)  # 服务器
smtp.login('592257128@qq.com','uzjgpuzphoxmbejf') #邮箱授权码

email_content = '小红帽测试'
msg = MIMEText(email_content,'html','utf-8')
msg['from'] = '592257128@qq.com'
msg['to'] = '1134106939@qq.com'  # 收件人
msg['Cc'] = '1134106939qq.com'
msg['subject'] = '测试'


smtp.sendmail('592257128@qq.com','592257128@qq.com',msg.as_string()) # 发件人，收件人
# smtp.sendmail('592257128@qq.com',['592257128@qq.com','1134106939@qq.com'],msg.as_string())

smtp.close()