import unittest
import os
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
def new_report(testreport):
    lists = os.listdir(testreport)
    # print('00000', lists)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "//" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print('1111', file_new)
    return file_new
def allTest():
    suit = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), './Demo/testCase/'),
        pattern='*_test.py',
        top_level_dir=None
    )
    return suit
def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))

def run():
    filename = './Demo/report/' + getNowTime() + ' guangdianReport.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(
                            stream=fp,
                            title=u'晋中广电登录自动化测试报告',
                            description=u'环境 ：window 10 浏览器：Chrome',
                            verbosity=2
                                           )
    runner.run(allTest())
    fp.close()
    # file_path = new_report('./report/')

# =========================邮件接收者============================
mailto_list=["353884277@qq.com"]
#============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host="smtp.163.com"
mail_user="xingwengbin@163.com"
mail_pass="abcd1234"
# ===========================发送邮件============================
# test_report = './report/'
def send_mail(to_list,file_new):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    print(file_new,'333')
    f = open(file_new, 'rb')
    mail_body = f.read()
    # print(mail_body,'00000')
    f.close()

    me = mail_user
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg = MIMEMultipart()
    msg['Subject'] = Header(u'自动化测试报告', 'utf-8').encode()
    msg['From'] = Header(me)
    msg['To'] = ";".join(to_list)
    msg.attach(body)

    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename = "test_report.html"'
    msg.attach(att)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host, 25)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ =='__main__':
    run()
    file_path = new_report('./Demo/report/')
    print(file_path, '000')

    if send_mail(mailto_list, file_path):
        print(file_path, '111')
        print(u"发送成功")
    else:
        print(u"发送失败")