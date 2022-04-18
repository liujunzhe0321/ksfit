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

    # 获取全部跑步记录(select)
    def test_getAllRecords(self):
        '''获取全部跑步记录'''
        data = {
            "service": "record.GetAllRecords",
            "token": self.user_token,
            "xjid": self.xj_id,
            "timestamp": ""
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("获取全部跑步记录返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    def test_getAllRecords(self):
        '所有的运动记录'
        data= {
                "service": "record.getRecordDetail",
                "token": self.user_token,
                "xjid":self.xj_id,
                "detailid":"99145193"
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])

    #删除跑步记录运动接口(delete)
    def test_deleteRecord(self):
        '''删除跑步记录运动'''
        data={
            "service":"record.delete",
            "token":self.user_token,
            "xjid":self.xj_id,
            "detailid":19045219
        }
        response=requests.post(self.ksfitHttp,data=json.dumps(data))
        ksfitlogCommon().printLog("删除跑步记录运动返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])







if __name__ == "__main":
    unittest.main()