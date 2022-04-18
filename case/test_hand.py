import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitHand(unittest.TestCase):
    '''徒手课程相关接口'''

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

    #查询所有徒手课程
    def test_courseHandList(self):
        '''查询所有徒手课程'''
        data={
                "service": "course.handList",
                "token":self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #徒手课程详情
    def test_courseHandDetail(self):
        '''徒手课程详情'''
        data={
                "service": "course.handDetail",
                "token":self.user_token,
                "xjid":self.xj_id,
                "course_id":10
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #开始徒手课程接口
    def test_courseCandBegin(self):
        '''开始徒手课程'''
        data={
                "service": "course.handBegin",
                "token":self.user_token,
                "xjid":self.xj_id,
                "course_id":10
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #徒手课程评价
    def test_courseHandFeedback(self):
        data= {
                "service": "course.handFeedback",
                "token": self.user_token,
                "xjid":self.xj_id,
                "score":10,
                "course_id":1,
                "content":"测试测试测试"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])



if __name__ == "__main":
    unittest.main()