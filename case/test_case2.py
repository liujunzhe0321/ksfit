import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon



class ksfitCaseTwo(unittest.TestCase):

        user_token = None
        ksfitHttp = None
        xj_id = None

        # 测试前执行(赋值token,ksfithttp,xjid)
        def setUp(self):
            self.user_token = ksfitUtilClass().readIni("logininformation", "user_token")
            self.ksfitHttp = ksfitUtilClass().readIni("logininformation", "ksfit_http")
            self.xj_id = ksfitUtilClass().readIni("logininformation", "xj_id")

        # 测试后执行
        def tearDown(self):
            print("over")

        #绑定用户
        def test_userbind(self):
            data={
                    "service": "user.userbind",
                    "token": self.user_token,
                    "xjid":self.xj_id
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        #查询所有的轮播活动(目前轮播活动app不调用接口)
        def test_motionArticleList(self):
            '''所有的轮播活动'''
            data={
                    "service": "explore.motionArticleList",
                    "token": self.user_token,
                    "xjid":self.xj_id,
                    "country": "CN"
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        #查询所有的轮播活动
        def test_advertisAdvertisList(self):
            '''所有的轮播活动'''
            data={
                    "service": "advertis.AdvertisList",
                    "token": self.user_token,
                    "xjid":self.xj_id,
                    "country": "CN"
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_getProgram(self):
            data={
                    "service": "user.getProgram",
                    "token": self.user_token,
                    "xjid":self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])



        ''' 
        def test_deleteProgram(self):
    
        #获取蓝牙固件版本
        def test_getFirmware(self):
        '''

        #
        def test_getProgram(self):
            data = {
                "service": "box.deviceList",
                "token": self.user_token,
                "xjid": self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_wxiotBindlist(self):
            data = {
                "service": "wxiot.bindlist",
                "token": self.user_token,
                "xjid": self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_getSelect(self):
            data = {
                "service": "user.getGuide",
                "token": self.user_token,
                "xjid": self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_userGetGuide(self):
            data = {
                "service": "user.getGuide",
                "token": self.user_token,
                "xjid": self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])


        def test_userSetGuide(self):
            data = {
                "service": "user.setGuide",
                "token": self.user_token,
                "xjid": self.xj_id,
                "device": "C1"
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_deviceShareMember(self):
            data = {
                "service": "device.shareMember",
                "token": self.user_token,
                "xjid":self.xj_id,
                "did": "FD:58:4A:09:76:B6"
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])

        def test_deviceShareList(self):
            data = {
                "service": "device.shareList",
                "token":self.user_token,
                "xjid": self.xj_id,
            }
            response = requests.post(self.ksfitHttp, data=json.dumps(data))
            ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
            ksfitlogCommon().printResponseLog(response)  # 日志
            self.assertEqual(200, json.loads(response.text)['ret'])


if __name__=="__main":
    unittest.main()