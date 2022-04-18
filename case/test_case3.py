import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitCaseThree(unittest.TestCase):
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

    def test_courseRecently(self):
        data={
                "service": "course.recently",
                "token": self.user_token,
                "xjid":self.xj_id,
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    def test_courseRunDetail(self):
        data = {
            "service": "course.runDetail",
            "token": self.user_token,
            "xjid": self.xj_id,
            "course_id": 1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    def test_courseRunFeedback(self):
        data={
                "service": "course.runFeedback",
                "token": self.user_token,
                "xjid":self.xj_id,
                "course_id":40,
                "content":"测试测试测试",
                "score":3
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    def test_courseExploreBanner(self):
        data={
                "service": "course.exploreBanner",
                "token": self.user_token,
                "xjid":self.xj_id,
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    def test_courseRunBegin(self):
        data={
                "service": "course.runBegin",
                "token": self.user_token,
                "xjid":self.xj_id,
                "course_id":1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    def test_rankingGet(self):
        data= {
                "service": "ranking.get",
                "token": self.user_token,
                "xjid":self.xj_id,
                "type":1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #开屏广告接口
    def test_userEmailReg(self):
        '''开屏广告'''
        data={
            "service": "advertis.AdvertisList",
            "token": self.user_token,
            "country":'CN',
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)  # 日志
        self.assertEqual(200, json.loads(response.text)['ret'])


if __name__ == "__main":
    unittest.main()