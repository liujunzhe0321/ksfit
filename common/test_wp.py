import requests
import json
import unittest
import hashlib
import time
from util.ksfitUtil import ksfitUtilClass



class walkingPad:

    # ksfit国内登录接口
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

        return  json.loads(response.text)['data']['info']['token']  # token放入在ini配置文件中



    #开屏广告接口
    def test_userEmailReg(self):
        '''邮箱注册'''
        data={
            "service": "device.addShare",
            "token": walkingPad().ksfitDomesticLogin(),
            "xjid":"21683",
            "keyword":"13001995872",
            "did":""
        }
        response = requests.post(ksfitUtilClass().readIni("logininformation", "ksfit_http"), data=json.dumps(data))
        print(json.loads(response.text))


if __name__ == "__main__":
     aaa=walkingPad()
     aaa.test_userEmailReg()




