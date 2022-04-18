import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon



class ksfitBind(unittest.TestCase):
    '''ksfit绑定小米'''

    user_token = None
    ksfit_http = None
    xj_id=None

    # 测试前执行(赋值token,ksfithttp)
    def setUp(self):
       self.user_token=ksfitUtilClass().readIni("logininformation","user_token")
       self.ksfitHttp=ksfitUtilClass().readIni("logininformation","ksfit_http")
       self.xj_id=ksfitUtilClass().readIni("logininformation","xj_id")

    # 测试后执行
    def tearDown(self):
        print("over")

    #绑定小米账号
    def test_userMiBind(self):
        '''绑定小米账号'''
        data={
            "service": "user.miBind",
            "mi_openid":ksfitUtilClass().readIni("miInformation","mi_openid"),
            "mi_token": ksfitUtilClass().readIni("miInformation","mi_token"),
            "mi_nickname":ksfitUtilClass().readIni("miInformation","mi_nickname"),
            "mi_expires_in": ksfitUtilClass().readIni("miInformation","mi_expires_in"),
            "token": self.user_token,
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("绑定小米账号接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #解绑小米账号
    def test_userMiUnBind(self):
        '''解绑小米账号'''
        data={
                "service": "user.miUnbind",
                "token": self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("解绑小米账号接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    # 微信账号绑定ksfit账号
    def test_userWxbind(self):
        '''微信账号绑定ksfit账号'''
        data = {
            "service": "user.wxBind",
            "wx_openid":ksfitUtilClass().readIni("wxInformation", "wx_openid"),
            "wx_unionid": ksfitUtilClass().readIni("wxInformation", "wx_unionid"),
            "wx_token": ksfitUtilClass().readIni("wxInformation", "wx_token"),
            "wx_nickname": ksfitUtilClass().readIni("wxInformation", "wx_nicknam"),
            "wx_expires_in": ksfitUtilClass().readIni("wxInformation","wx_expires_in"),
            "token": self.user_token,
            "xjid": self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("微信账号绑定ksfit账号接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    # ksfit解绑微信账号
    def test_userWxUnbind(self):
        '''ksfit解绑微信账号'''
        data = {
            "service": "user.wxUnbind",
            "token": self.user_token,
            "xjid": self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("ksfit解绑微信账号接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])



if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    # 将测试用例添加到测试容器中,设置执行顺
    suite.addTest(TestLogin('test_userMiBind'))
    suite.addTest(TestLogin('test_userMiUnBind'))
    suite.addTest(TestLogin('test_userWxbind'))
    suite.addTest(TestLogin('test_userWxUnbind'))
