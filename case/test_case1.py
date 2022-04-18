import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitCaseOne(unittest.TestCase):

    user_token = None
    ksfit_http = None
    xj_id = None

    # 测试前执行(赋值token,ksfithttp,xjid)
    def setUp(self):
        self.user_token = ksfitUtilClass().readIni("logininformation", "user_token")
        self.ksfitHttp = ksfitUtilClass().readIni("logininformation", "ksfit_http")
        self.xj_id = ksfitUtilClass().readIni("logininformation", "xj_id")

    # 测试后执行
    def tearDown(self):
        print("over")



    # 获取全部课程的接口(select)
    def test_courserRunList(self):
        '''获取全部课程'''    #用例名描述
        data = {
            'service': 'course.runList',
            'token': self.user_token,
            'xjid':self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取全部课程返回内容为:",json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])







    '''
    #意见反馈提交接口(insert)
    def test_userFeedback(self):
        data={
             "service":"user.feedback",
             "token":self.getToken(),
             "xjid":self.xjId,
             "content":"测试测试测试测试测试测试测试测试1111",
        }
        response=requests.post(self.ksfitHttp,data=json.dumps(data))
        self.assertEqual(200, json.loads(response.text)['ret'])
    '''


    #体重记录查询(select)
    def test_userWeightLog(self):
        '''体重记录查询'''
        data={
            "service": "user.weightLog",
            "token": self.user_token,
            "xjid":self.xj_id,
            "sub_user_id": None
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("体重记录查询返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    # 体重图表记录查询(select)
    def test_userWeightChart(self):
        '''体重图表记录查询'''
        data={
            "service": "user.weightChart",
            "token": self.user_token,
            "xjid":self.xj_id,
            "sub_user_id": None,
            "type": 1,
            "startTime": "2018-09-03",
            "endTime": "2022-10-20"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("体重图表记录查询返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #本周积分(select)
    def test_userCoin(self):
        '''本周积分'''
        data={
                "service": "user.coin",
                "token": self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("本周积分接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #获取排行榜(select)
    def test_getRanking(self):
        '''获取排行榜'''
        data = {
            "service": "ranking.get",
            "token": self.user_token,
            "xjid":self.xj_id,
            "type":1             #走步机
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取排行榜接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #获取排行榜默认类型(select)
    def test_getRankingType(self):
        '''获取排行榜默认类型'''
        data = {
            "service": "ranking.getType",
            "token": self.user_token,
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取排行榜默认类型接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #设置按键(update)
    def test_userSetKey(self):
        '''设置按键'''
        data={
            "service": "user.setKey",
            "token": self.user_token,
            "xjid":self.xj_id,
            "hiit": 0,
            "burn": 0,
            "walk": 0,
            "speed_1": 3,
            "speed_2": 6,
            "speed_3": 9,
            "did": 1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("设置按键接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #获取按键
    def test_userGetKey(self):
        '''获取按键'''
        data={
            "service": "user.getKey",
            "token": self.user_token,
            "xjid":self.xj_id,
            "did": 2249142079
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取按键接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #蓝牙跑步机上传运动记录(insert)
    def test_insertRecord(self):
        '''蓝牙跑步机上传运动记录'''
        data={

                "service": "record.uploadRunning",
                "token": self.user_token,
                "xjid":self.xj_id,
                "mac": "FC:58:FA:00:00:01",
                "distance": 3900,
                "time": 5000,
                "consume": 80000,
                "steps": 3000,
                "start_time": "2022-3-2 09:08:08",
                "end_time": "2021-3-2 10:08:08",
                "model": "ZP-EALR1"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("蓝牙跑步机上传运动记录接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #获取最后一次体重数据(select)
    def test_userLastWeight(self):
        '''获取最后一次体重数据'''
        data={
            "service": "user.lastWeight",
            "token": self.user_token,
            "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取最后一次体重数据接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    # 获取消息红点(select)
    def test_getNoticeHint(self):
        '''获取消息红点'''
        data = {
            "service": "notice.hint",
            "token": self.user_token,
            "xjid": self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取消息红点接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    # 获取消息列表(select)
    def test_getAllNoticeHint(self):
        '''获取消息列表'''
        data = {
            "service": "notice.getList",
            "token": self.user_token,
            "xjid":self.xj_id,
            "page":1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取消息列表接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    # 获取广告列表(select)
    def test_getAllNoticeHint(self):
        '''获取广告列表'''
        data = {
            "service": "notice.getList",
            "token": self.user_token,
            "xjid": self.xj_id,
            "page":1
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取广告列表返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #查询设备是否绑定成功
    def test_bindCheck(self):
        '''查询是否绑定成功'''
        data={
            "service": "bind.check",
            "token": self.user_token,
            "xjid":self.xj_id,
            "device_name": "100901210512000009"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("查询是否绑定成功返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #获取首页活动列表
    def test_getActivityList(self):
        '''获取首页活动列表'''
        data={
            "service": "box.activityList",
            "token": self.user_token,
            "xjid":self.xj_id,
            "country": "CN"

        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取首页活动列表接口返回内容为:", json.loads(response.text))
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



if __name__=="__main":
    unittest.main()
