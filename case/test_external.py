import unittest
import hashlib
import requests
import json
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon

#国外接口
class ksfitExternal(unittest.TestCase):
    '''国外接口'''


    #登录
    def test_ksfitOverseasLogin(self):
        '''国外登录接口'''
        data={
            'service': 'user.login',
            'email': ksfitUtilClass().readIni("logineuinformation", "user_email"),
            'pwd': hashlib.md5(
                ksfitUtilClass().readIni("logineuinformation", "user_emailPwd").encode(encoding='UTF-8')).hexdigest()
            # 将密码进行md5加密
        }
        response=requests.post(ksfitUtilClass().readIni("logineuinformation","ksfit_euTttp"),data=json.dumps(data))
        ksfitlogCommon().printResponseLog(response)  # 日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #邮箱注册
    def test_userEmailReg(self):
        '''邮箱注册'''
        data={
            "service": "user.emailReg",
            "email": ksfitUtilClass().readIni("wpeuinformation","user_email"),
            "pwd":hashlib.md5(
                ksfitUtilClass().readIni("logineuinformation", "user_emailPwd").encode(encoding='UTF-8')).hexdigest(),
            "avatar":ksfitUtilClass().baseImg('../img/guowai.jpg'),
            "gender": "男",
            "nickname":"黄飞鸿",
            "brand":None,
            "IMEI":None,
            "longitude":None,
            "latitude":None
        }
        response = requests.post(ksfitUtilClass().readIni("logineuinformation", "ksfit_euTttp"), data=json.dumps(data))
        ksfitlogCommon().printResponseLog(response)  # 日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #忘记密码
    def test_userEmailFindPwd(self):
        '''忘记密码'''
        data={
            "service": "user.emailFindPwd",
            "email": ksfitUtilClass().readIni("wpeuinformation","user_email")
        }
        response = requests.post(ksfitUtilClass().readIni("logineuinformation", "ksfit_euTttp"), data=json.dumps(data))
        ksfitlogCommon().printResponseLog(response)  # 日志
        self.assertEqual(200, json.loads(response.text)['ret'])


if __name__=="__main__":
    unittest.main()

