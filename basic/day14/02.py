# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          02
# Description:   发送邮件，带附件
# Author:        xuezy
# Date:          2020/10/21 18:54
# --------------------------------------------------------------
# smtp服务器
import smtplib
# 邮件文本
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    # 邮件构建
    subject = "滴滴答答"  # 邮件标题
    sender = "18622818540@163.com"  # 发送方
    content = "新年快乐！"
    recver = "1395219833@qq.com"  # 接收方
    password = "xzy1234"  # 邮箱密码

    #  与发送文字不一样
    message = MIMEMultipart()
    # content 发送内容     "plain"文本格式   utf-8 编码格式

    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人

    filename = 'test.txt'
    # 构造附件1，传送当前目录下的 filename 文件
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="' + filename + '"'
    message.attach(att1)

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()
    print('发送完成')


if __name__ == '__main__':
    main()
