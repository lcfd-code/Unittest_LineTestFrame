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
from common.config_utils import config

class EmailUtile:
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 25
        self.smtp_sender = config.SMTP_SENDER
        self.smtp_password = 'uzjgpuzphoxmbejf'
        self.smtp_receiver = config.SMTP_RECEIVER
        self.smtp_cc = '592257128@qq.com,742659925@qq.com'
        self.smtp_subject = '自动化测试报告'
        self.smtp_body = smtp_body  # 正文
        self.smtp_attch_path = smtp_attch_path  # 附件路径

    def email_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver  # 收件人
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach(MIMEText(self.smtp_body,'html','utf-8'))
        if self.smtp_attch_path:
            attach_file_obj = MIMEText(open(self.smtp_attch_path, 'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.smtp_attch_path)))
            message.attach(attach_file_obj)
        return message

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server,self.smtp_port)
        smtp.login(self.smtp_sender,self.smtp_password)
        smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(','),self.email_message_body().as_string())

if __name__ == '__main__':
    email_u = EmailUtile('test使用')
    email_u.send_email()

