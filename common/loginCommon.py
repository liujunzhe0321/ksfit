import hashlib
import requests
import json
from util.ksfitUtil import ksfitUtilClass

#登录公共类
class ksfitLoginCommonClass:



    #ksfit国内登录接口
    @classmethod
    def ksfitDomesticLogin(self):
        data = {
            'service': 'user.login',
            'phone': ksfitUtilClass().readIni("logininformation", "user_phone"),
            'pwd': hashlib.md5(
                ksfitUtilClass().readIni("logininformation", "user_pwd").encode(encoding='UTF-8')).hexdigest()
            # 将密码进行md5加密
        }
        response = requests.post(ksfitUtilClass().readIni("logininformation", "ksfit_http"),
                                 data=json.dumps(data))  # 接受响应头
        ksfitUtilClass().setIni("logininformation","user_token",
                                json.loads(response.text)['data']['info']['token'])   #token放入在ini配置文件中


    #ksfit国外登录接口
    @classmethod
    def ksfitOverseasLogin(self):
        data={
            'service': 'user.login',
            'email': ksfitUtilClass().readIni("logineuinformation", "user_email"),
            'pwd': hashlib.md5(
                ksfitUtilClass().readIni("logineuinformation", "user_emailPwd").encode(encoding='UTF-8')).hexdigest()
            # 将密码进行md5加密
        }
        response=requests.post(ksfitUtilClass().readIni("logineuinformation","ksfit_euTttp"),data=json.dumps(data))
        ksfitUtilClass().setIni("logineuinformation", "user_euToken",
                                json.loads(response.text)['data']['info']['token'])  # token放入在ini配置文件中


    #walkingpad国内登录接口
    @classmethod
    def wpDomesticLogin(self):
        '''登录接口'''
        data = {
            'phone': ksfitUtilClass().readIni("wpinformation", "user_phone"),
            'password': hashlib.md5(
                ksfitUtilClass().readIni("wpinformation", "user_pwd").encode(encoding='UTF-8')).hexdigest()
        }
        response = requests.post(ksfitUtilClass().readIni("wpinformation", "wp_http")+"/user/api/v2/login", data=json.dumps(data))
        print(response.cookies)
        return response.cookies                 #waikingpad 身份验证使用的是cookie


    # walkingpad国外登录接口
    @classmethod
    def wpOverseasLogin(self):
        data = {
            'email': ksfitUtilClass().readIni("wpeuinformation", "user_email"),
            'password': hashlib.md5(
                ksfitUtilClass().readIni("wpeuinformation", "user_emailpwd").encode(encoding='UTF-8')).hexdigest()
        }
        wpEuLoginHttp = ksfitUtilClass().readIni("wpeuinformation", "wp_eu_http") + "/user/api/v2/login"  # 拼接登录接口url
        response = requests.post(wpEuLoginHttp, data=json.dumps(data))
        return response.cookies      #waikingpad 身份验证使用的是cookie身份验证使用的是cookie







