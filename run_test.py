# # -*- coding: utf-8 -*-

# """
# import os
# import unittest
# from datetime import datetime
#
# from libs import HTMLTestRunnerNew
# from scripts.constants import REPORTS_DIR
# from scripts.handle_config import do_config
# from scripts.constants import USER_ACCOUNTS_FILE_PATH, CASES_DIR
# from scripts.handle_user import generate_users_config
#
# if not os.path.exists(USER_ACCOUNTS_FILE_PATH):  # 如果用户账号所在文件不存在, 则创建用户账号
#     generate_users_config()
#
# # 1.创建套件
# # one_suite = unittest.TestSuite()
#
# # 2.加载用例
# # 创建加载器对象
# # one_loader = unittest.TestLoader()
# # one_suite.addTest(one_loader.loadTestsFromModule(register))
#
# one_suite = unittest.defaultTestLoader.discover(CASES_DIR)
#
# # 3.运行用例
# # datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
# report_name = do_config.get_value("report", "report_html_name") + "_" + \
#               datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + '.html'
# report_full_path = os.path.join(REPORTS_DIR, report_name)
# with open(report_full_path, mode='wb') as save_to_file:
#     one_runner = HTMLTestRunnerNew.HTMLTestRunner(stream=save_to_file,
#                                                   title=do_config.get_value("report", "title"),
#                                                   verbosity=do_config.get_int("report", "verbosity"),
#                                                   description=do_config.get_value("report", "description"),
#                                                   tester=do_config.get_value("report", "tester"))
#     one_runner.run(one_suite)
# coding:utf-8


import os
import sys
REPORT_PATH = os.path.join(os.path.split(os.path.dirname(__file__))[0],'reports.html')
# print(REPORT_PATH)
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
sys.path.insert(0, path)
import unittest
from libs import HTMLTestRunnerNew
import time
from configs.sendemail import *
# TESTCASE_PATH=os.path.join(os.path.split(os.path.dirname(__file__)[0]),'cases')
TESTCASE_PATH = os.path.join(os.path.dirname(__file__),'cases')
print(TESTCASE_PATH)
suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='*.py')
if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")
    fp = open(REPORT_PATH, 'wb')
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=fp,
        title=u'接口测试报告',
        description=u'测试报告地址',
        tester="wangna"
    )
    runner.run(suit)
    fp.close()
    print(fp)
    print("生成报告")
    time.sleep(50)
    send_mail(REPORT_PATH)
    print("发送成功")

