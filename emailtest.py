# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
# import getpass
#
# def send_email(msg, subject, sender, receivers, host, passwd):
#     message = MIMEText(msg, 'plain', 'utf8')        #邮件正文内容
#     message['From'] = Header(sender, 'utf8')        #发件人
#     message['To'] = Header(receivers[0], 'utf8')    #收件人
#     message['Subject'] = Header(subject, 'utf8')    #邮件主题
#     smtp = smtplib.SMTP()
#     smtp.connect(host)                              #邮件服务器地址
#     smtp.login(sender, passwd)                      #发件人邮箱密码
#     smtp.sendmail(sender, receivers, message.as_bytes())
#             #sendmail方法发送邮件,必须有收件人,发件人,消息主体,message是一个字符串,表示邮件
# if __name__ == '__main__':
#     msg = 'python smtplib 邮件测试\r\n'     #邮件正文内容
#     subject = 'py mail test'               #邮件主题
#     sender = 'zhangzhigang79@126.com'      #发件人
#     receivers = ['zhangzhigang79@126.com'] #收件人
#     host = 'smtp.126.com'                  #邮件服务器地址,这个地方要查询
#     passwd = getpass.getpass()             #发件人邮箱密码
#     send_email(msg, subject, sender, receivers, host, passwd)
