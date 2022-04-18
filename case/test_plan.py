import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitPlan(unittest.TestCase):
    '''计划相关接口'''

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

    def user_planList(self):
        '''计划列表'''
        data= {
                "service": "user.planList",
                "token": self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])





if __name__ == "__main":
    unittest.main()