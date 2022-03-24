# -*- coding:utf-8 -*-
import unittest
import os
import time
import logging
import datetime
from HTMLTestRunner import HTMLTestRunner
from util.ksfitUtil import ksfitUtilClass
from common.loginCommon import ksfitLoginCommonClass


class run_test():

    def run_case():
        print("================================开始测试================================")
        startTime = time.time()   #获取开始时间点
        # 先登录接口，ini文件中获取token
        ksfitLoginCommonClass().ksfitDomesticLogin()
        # 用例读取路径
        case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "case")
        suite = unittest.TestLoader().discover(case_path)
        '''
        suite.addTest(ksfitLogin("test_userWxbind"))
        suite.addTest(ksfitLogin("test_userWxUnbind"))
        '''
        # 测试报告存放路径
        report_path = os.path.join(os.path.dirname(os.path.realpath(__file__)) + "/report/ksfit_Interface_Result.html")
        with open(report_path, "wb") as f:
            runner = HTMLTestRunner(stream=f, title="KsFit后台接口测试", description="测试结果", verbosity=2)
            # LOG日志记录
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filemode='w')
            logger = logging.getLogger()
            logger.info(suite)
            # 发送邮件
            result = runner.run(suite)  # 拿取测试报告结果(error_count,failuer_count,success_count)
            time.sleep(5)  # 测试报告html生成过慢，所以需等待5秒钟，进行邮件发送
            ksfitUtilClass().send_main(result.success_count, result.failure_count, result.error_count)  # 调用util类中邮件发送
            endTime = time.time()        #获取结束时间点
            print("===============================结束测试=================================")
            print("本次测试共耗时" + str(int(endTime - startTime)) + "秒")

if __name__ == "__main__":
    run_test.run_case()