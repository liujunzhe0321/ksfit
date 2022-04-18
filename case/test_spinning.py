import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitRecord(unittest.TestCase):
    '''运动记录相关接口'''

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


    #获取单车活动列表
    def test_getBicycleList(self):
        '''获取单车活动列表'''
        data={
                "service": "course.bicyclelist",
                "token": self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取首页活动列表接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #单车课程评价
    def setBicycleFeedback(self):
        '''单车课程评价'''
        data= {
                "service": "course.bicycleFeedback",
                "token": self.login(),
                "xjid":self.xj_id,
                "score":3,
                "content":"测试测试测试",
                "course_id":"1"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #开始单车课程(观看视频)
    def test_bicycleBegin(self):
        '''开车单车课程'''
        data={
            "service": "course.bicycleBegin",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("开车单车课程接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    # 完成单车课程（打卡）
    def test_bicycleFinishTimes(self):
        '''完成单车课程(打卡)'''
        data = {
            "service": "course.bicycleFinish",
            "token": self.user_token,
            "xjid": self.xj_id,
            "course_id": 1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("完成单车课程(打卡)接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #完成单车课程（打卡）
    def test_bicycleFinishTimes(self):
        '''完成单车课程(打卡)'''
        data={
            "service": "course.bicycleFinishTimes",
            "token": self.user_token,
            "xjid":self.xj_id,
            "course_id": 1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("完成单车课程(打卡)接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #获取个人设备列表
    def test_boxDeviceList(self):
        '''获取个人设备列表'''
        data = {
            "service": "box.deviceList",
            "token": self.user_token,
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("完成单车课程(打卡)接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)  # 日志
        self.assertEqual(200, json.loads(response.text)['ret'])





if __name__ == "__main":
    unittest.main()