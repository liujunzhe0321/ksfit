import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitDumbbell(unittest.TestCase):
    '''哑铃相关接口'''
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


    #评价哑铃课程
    def test_dumbbellFeedback(self):
        '''评价哑铃课程'''
        data = {
            "service": "course.dumbbellFeedback",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 2,
            "score": 1,
            "content": "1"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("评价哑铃课程接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #获取哑铃课程列表(select)
    def test_getDumbbellList(self):
        '''获取哑铃课程列表'''
        data={
            "service": "course.dumbbellList",
            "token": self.user_token,
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取哑铃课程列表接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #评价课程
    def test_bicycleFeedback(self):
        '''评价课程'''
        data={
            "service": "course.bicycleFeedback",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 1,
            "score": 1,
            "content": "abcabc"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("评价课程接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #获取哑铃课程详情(select)
    def test_getDumbbellDetail(self):
        '''获取哑铃课程详情'''
        data={
            "service": "course.dumbbellDetail",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 2
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取哑铃课程详情接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #开始哑铃课程
    def test_getDumbbellDetail(self):
        '''开始哑铃课程'''
        data={
            "service": "course.dumbbellBegin",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 2
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取哑铃课程详情接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])



if __name__ == "__main":
    unittest.main()