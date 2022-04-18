import requests
import json
import unittest
import hashlib
from util.ksfitUtil import ksfitUtilClass
from common.logCommon import ksfitlogCommon


class ksfitPlan(unittest.TestCase):
    '''用户相关接口'''

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
        '''成员列表'''
        data= {
                "service": "user.subUserList",
                "token": self.user_token,
                "xjid":self.xj_id
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("接口返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #修改个人头像接口(update)
    def test_setUserAvatar(self):
        '''修改个人头像'''
        data = {
            "service": "user.setUserAvatar",
            "token": self.user_token,
            "xjid":self.xj_id,
            "avatar":ksfitUtilClass().baseImg("../img/img-touxiang.bmp")         #调用工具类里面的base64转换方法，将本地图片直接转换为base64
        }
        response = requests.post(self.ksfitHttp, data=json.dumps(data))
        ksfitlogCommon().printLog("修改个人头像返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])


    #编辑个人资料
    def test_setUserOneInfo(self):
        '''编辑个人资料提交'''
        data = {
            'service':'user.setUserOneInfo',
            'token': self.user_token,
            'xjid':self.xj_id,
            'height': 166,
            'birthday': 2000,
            'nickname': '大大大是2',
            'gender': '男',
            'province': '河北省',
            'city': '石家庄市',
            'weight': 60,
            'my_slogan': 'fasfawfasdfasdf'
        }
        response = requests.post(self.ksfitHttp,data=json.dumps(data))
        ksfitlogCommon().printLog("编辑个人资料提交返回内容为:", json.loads(response.text))
        ksfitlogCommon().printResponseLog(response)            #日志
        self.assertEqual(200, json.loads(response.text)['ret'])





if __name__ == "__main":
    unittest.main()