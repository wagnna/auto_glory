#coding: utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
import unittest
import smtplib
from email.mime.text import MIMEText
import time,os,sys
REPORT_PATH = os.path.join(os.path.split(os.path.dirname(__file__))[0],'reports.html')
# print(REPORT_PATH)
def send_mail(file_new):
    mail_from='1415711435@qq.com'#邮件发送地址
    #mail_to='xupeiqing@artbloger.com'#邮件接收地址
    # mail_to='wangna@hupu.com,1415711435@qq.com,linke@hupu.com,wangmengdi@hupu.com,liuyanyun@hupu.com'#邮件接收地址
#     mail_to_user =['1415711435@qq.com','wangna@hupu.com','linke@hupu.com','wangmengdi@hupu.com','liuyanyun@hupu.com','dongshuming@hupu.com']
    mail_to = ','.join(mail_to_user)
    print(mail_to)
    # [x.encode('utf-8') for x in mail_to]
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='UTF-8')
    msg['from']=mail_from
    msg['to']=mail_to
    msg['Subject']=u"hupu自动化报告"
    msg['Accept-Language']='zh-CN'
    # msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    # msg = MIMEText(content,format,'gbk')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(mail_from,'hewsirhbmsqticci')
               # 'rpdhayxdwuqxighi')
               #                # 'hewsirhbmsqticci')
    smtp.sendmail(mail_from,mail_to.split(","),msg.as_string())
    smtp.quit()
    print("发送邮件成功")

if __name__ == '__main__':
    time.sleep(1)
    send_mail(REPORT_PATH)
