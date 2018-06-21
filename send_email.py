import smtplib
from email.mime.text import MIMEText


def send_mail():
    from_add = r'13263107553@163.com'  # 发件人
    password = 'nq1982070811wm'
    to_add = '632166899@qq.com'  # 收件人
    subject = '难道只能用中文？'  # 邮件标题
    content = '你猜我在干嘛'  # 邮件正文内容
    smtp_server = 'smtp.163.com'  # 邮件的服务
    msg = MIMEText(content)  # 发送的内容

    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_add, password)
    server.sendmail(from_add, to_add, msg.as_string())
    print('发送成功')
    server.quit()


if __name__ == '__main__':
    send_mail()
