import HTMLTestRunner

import HtmlTestRunner
import unittest

from pom.test_cases.case import TestDemo01

cases = unittest.TestLoader().loadTestsFromTestCase(TestDemo01)

with open('report.html','wb') as report:
    runner= HTMLTestRunner.HTMLTestRunner(stream=report, title='测试报告', description='测试用例详情')
    runner.run(cases)

