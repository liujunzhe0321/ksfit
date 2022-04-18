import logging
import requests
import json

class ksfitlogCommon:
    # 输出日志,用在测试报告
    @classmethod
    def printLog(self, InterfaceName, responseTextJson):
        print(InterfaceName, end="")
        print(responseTextJson)  # 输入返回文本，显示在测试报告中


    @classmethod
    def printResponseLog(self,response):
        logging.info(json.loads(response.text))            #日志输出响应文本
