

import unittest
import os
from common import HTMLTestReportCN
from common.email_utils import EmailUtile

case_path = os.path.join(os.path.dirname(__file__),'testcases')
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_*.py',
                                               top_level_dir=case_path)
all_suite = unittest.TestSuite()
all_suite.addTest(discover)


report_path = os.path.join(os.path.dirname(__file__),'reports/')
report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
report_dir.create_dir('feng_') #调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
report_html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='微信公众平台接口测试报告',
                                              description='unittest接口测试框架使用',
                                              tester='李传风')
html_runner.run(all_suite)
EmailUtile('微信共平台接口测试报告',report_html_path).send_email()