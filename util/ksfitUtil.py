import base64
import configparser
import os
import smtplib
import requests
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class ksfitUtilClass:

    #图片转换base64
    @classmethod   #调用此方法不用实例化类
    def baseImg(self,url):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(BASE_DIR, url), "rb") as f:
            base64_data = base64.b64encode(f.read())  # 使用base64图片转换为码
            return base64_data.decode('ascii')      #需进行一次decode解码,否则有b’‘
        ini_absolute_path = os.path.abspath("test.ini")

    # 依据 [module] 来读取 ini 文件
    @classmethod   #调用此方法不用实例化
    def readIni(abc,section,option):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()   #实例化配置文件
        config.read(os.path.join(BASE_DIR, '../common/test.ini'))  # 读取配置文件
        return config.get(section,option)      #返回获取的值

    # 依据 [module] 来写入ini 文件
    @classmethod  # 调用此方法不用实例化
    def setIni(abc, section,option,content):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()  # 实例化配置文件
        config.read(os.path.join(BASE_DIR, '../common/test.ini'))  # 读取配置文件
        config.set(section,option,content)  # 写入值
        config.write(open(os.path.join(BASE_DIR, '../common/test.ini'),"w"))

    global send_user
    global email_host
    global password
    email_host = 'smtp.163.com'
    send_user = '18406467155@163.com'
    password = 'liujz0321'

    #发送邮件测试报告方法
    @classmethod  # 调用此方法不用实例化类
    def send_main(self, pass_count, fail_count, error_count):
        pass_num = float(pass_count)       #通过数，取小数点后两位
        fail_num = float(fail_count)       #失败数，取小数点后两位
        error_count = float(error_count)   #错误数，取小数点后两位
        countAll_num = pass_num + fail_num + error_count   #所有的接口数
        failAndError_num = fail_num + error_count   #失败跟错误的接口数
        # 取小数后2位,通过率
        pass_result = "%.2f%%" % (pass_num / countAll_num * 100)   #通过率
        fail_result = "%.2f%%" % (failAndError_num / countAll_num * 100)  #失败率(失败+错误)/总接口数
        user_list = [ksfitUtilClass.readIni("emailinformation","user_list")]     #接受人
        sub = "ksfit接口自动化测试"
        content = "这次一共测试%s个接口,通过个数为%s,失败个数为%s,错误个数为%s,通过率为%s,失败率为%s" % (
        countAll_num, pass_num, fail_num, error_count, pass_result, fail_result)
        contentn = "共测试接口数量:%s个\n通过个数:%s\n失败个数:%s\n错误个数:%s\n通过率:%s\n失败率:%s" % (
            countAll_num, pass_num, fail_num, error_count, pass_result, fail_result)
        ksfitUtilClass().dingDingSend(contentn)              #调用钉钉群消息通知
        print(content)
        self.send_mail(user_list, sub, content)

    # 接受人，主题，内容
    def send_mail(user_list, sub, content):
        user = "cherish" + "<" + send_user + ">"   # 发件者
        message=MIMEMultipart('related')    # 定义邮件类型，related可以增加多种附件
        message.attach(MIMEText(content,_subtype='plain',_charset='utf-8'))   #添加邮件内容
        #message = MIMEText(content, _subtype='plain', _charset='utf-8')   # 内容、格式、编码
        message['Subject'] = sub     # 主题
        message['From'] = user  # 发送人
        message['To'] = ";".join(user_list)   # 接受人
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        mail_path = open(os.path.join(BASE_DIR, '../report/ksfit_Interface_Result.html'),'r',encoding='utf-8').read()   #这几句里边可以修改路径和文件名称，具体以实际为准
        att = MIMEText(mail_path,"base64","utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = "attachment;filename = ksfit_Interface_Result.html"
        message.attach(att)      #附件放入邮件中
        server = smtplib.SMTP()
        server.connect(email_host)     # 连接邮件服务器
        server.login(send_user, password)  # 邮件登录
        server.sendmail(user, user_list, message.as_string())  # 发送邮件内容
        server.close()  # 关掉连接
        print("=============发送邮件成功==============")

    #发送钉钉群通知
    @classmethod
    def dingDingSend(self,content):
            headers = {'Content-Type': 'application/json'}
            webhook =ksfitUtilClass().readIni("dingding","dingding_url")
            data = {
                "msgtype": "text",
                "text": {
                    "content": content + '\n'
                },
                "at": {
                        "atMobiles": [
                        ],
                    "isAtAll": False
                }
            }
            res=requests.post(url=webhook, data=json.dumps(data), headers=headers)




