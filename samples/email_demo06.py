#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('592257128@qq.com','uzjgpuzphoxmbejf') #邮箱授权码

msg = MIMEMultipart()
msg['from'] = '592257128@qq.com'
msg['to'] = '1134106939@qq.com'  # 收件人
msg['Cc'] = '1134106939qq.com'
msg['subject'] = '测试'

email_content = '测试嘻嘻嘻'
msg.attach( MIMEText(email_content,'html','utf-8') )

attach_file_path = os.path.join( os.path.dirname(__file__),'API_TEST_V2.0.html' )
attach_file_obj = MIMEText( open(attach_file_path,'rb').read(),'base64','utf-8' )
attach_file_obj['Content-Type'] = 'application/octet-stream'
attach_file_obj.add_header('Content-Disposition','atachment',
                           filename=('gbk','',os.path.basename(attach_file_path)))
msg.attach( attach_file_obj )


smtp.sendmail('329999897@qq.com',['329999897@qq.com','294608794@qq.com'],msg.as_string()) #发件人、收件人
# smtp.sendmail('592257128@qq.com',['592257128@qq.com','1134106939@qq.com'],msg.as_string())

smtp.close()