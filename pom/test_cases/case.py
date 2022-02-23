'''
    第一组测试用例
'''
import unittest


from selenium import webdriver
from ddt import ddt, data, file_data, unpack

from pom.base.chrome_options import ChromeOptions
from pom.page_object.login.login_page import LoginPage

from pom.page_object.rule_page import RulePage
from pom.page_object.monitor.system_page import System_Page

from pom.page_object.monitor.safety_page import Safety_Page
@ddt
class TestDemo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOptions().options())
        cls.lp = LoginPage(cls.driver)
        cls.ip = RulePage(cls.driver)
        # cls.sy = Syslog_page(cls.driver)
        cls.jt = System_Page(cls.driver)
        cls.sf = Safety_Page(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # @data(['superadmin', 'Admin@123', ])
    # @unpack
    @file_data('../data/login.yaml')
    def test_01_login(self, user, pwd,):
        self.lp.longin(user, pwd)

    @file_data('../data/index.yaml')
    def test_02_rule(self,qw,qw2,qw3,qw4,qw5):
        self.ip.system(qw,qw2,qw3,qw4,qw5)

    # @data(['192.168.15.67','514'])
    # @unpack
    # def test_03_syslog(self,ip,port):
    #     self.sy.Syslong(ip,port)

    # def test_04_system(self):
    #     self

    # def test_05_snmp(self):
    #     self

    # @file_data("../data/aisle.yaml")
    # def test_06_system(self, user, ID, listener_port,http,ip):
    #     self.jt.system(user, ID, listener_port,http,ip)

    # @data(['安全通道名称','slot0-1'])
    # @unpack
    #
    # # @file_data("../data/safe.yaml")
    # def test_08_safety(self,designation,network):
    #     self.sf.safety(designation,network)

if __name__ == '__main__':
    unittest.main()