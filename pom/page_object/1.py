'''
    第一组测试用例
'''
import unittest

from selenium import webdriver
from ddt import ddt, data, file_data, unpack

from pom.base.chrome_options import ChromeOptions
from pom.page_object.login.login_page import LoginPage
from pom.page_object.rule_page import RulePage
from pom.page_object.syslog_page import Syslog_page

@ddt
class TestDemo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOptions().options())
        cls.lp = LoginPage(cls.driver)
        cls.ip = RulePage(cls.driver)
        cls.sy = Syslog_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    # @file_data('../data/login.yaml')
    @data(['superadmin', 'Admin@123', ])
    @unpack
    def test_01_login(self, user, pwd,):
        self.lp.longin(user, pwd)

    @file_data('../data/index.yaml')
    def test_02_rule(self,qw,qw2,qw3,qw4,qw5):
        self.ip.system(qw,qw2,qw3,qw4,qw5)

    # @data(['192.168.15.67','514'])
    # @unpack
    def test_03_syslog(self):
        ip='192.168.15.67'
        port='514'
        self.sy.Syslong(ip,port)

if __name__ == '__main__':
    unittest.main()