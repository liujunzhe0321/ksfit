import hashlib
import unittest
import requests
import json
from util.ksfitUtil import ksfitUtilClass
from common.loginCommon import ksfitLoginCommonClass
from common.logCommon import ksfitlogCommon


class walkingPadEuClass(unittest.TestCase):
    '''wp国外接口'''


    wp_http = None
    wp_cookies=None

    # 测试前执行(赋值token,ksfithttp,xjid)
    def setUp(self):
        self.wp_http = ksfitUtilClass().readIni("wpeuinformation","wp_eu_http")
        self.wp_cookies=ksfitLoginCommonClass().wpOverseasLogin()

    # 测试后执行
    def tearDown(self):
        print("over")


    #获取运动数据接口
    def test_wpGetlist(self):
        '''获取运动数据接口'''
        data={
            'page':1,
            'per_page':10,
            'timestamp':""
        }
        response = requests.get(self.wp_http+"/user/api/v2/record",data=json.dumps(data),cookies=self.wp_cookies)
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)
        self.assertEqual(200, json.loads(response.text)['code'])



if __name__ == "__main__":
    unittest.main()