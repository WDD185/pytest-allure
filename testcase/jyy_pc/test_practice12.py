# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self):
        self.sendmail = '1403228211@qq.com'
        self.password = 'rqupgnklumofhabg'
        self.receive_mail = 'wdd185@126.com'
        self.title = "python邮件测试4"
        self.content = "这是我使用python发送的邮件4"
        self.image_path = r'E:\pic\photo.png'

    def send_mail(self):
        msg = MIMEText(self.content, 'plain', 'utf-8')
        image = MIMEImage(open(self.image_path, mode='rb').read())
        #  CD保证图片可以显示，attachment保证发送的图片可以预览和下载
        image.add_header('Content-Disposition', 'attachment', filename='photo.png')
        m = MIMEMultipart()
        m.attach(msg)
        m.attach(image)
        m['Subject'] = self.title
        m['From'] = self.sendmail
        m['To'] = self.receive_mail
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com", 465, 'utf-8')
            server.login(self.sendmail, self.password)
            server.sendmail(self.sendmail, self.receive_mail, m.as_string())
            print("发送成功")
        except smtplib.SMTPException as e:
            print("发送失败,失败原因：%s" % e)
        finally:
            server.quit()


if __name__ == '__main__':
    Mail().send_mail()
