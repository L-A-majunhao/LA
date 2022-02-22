# from  import *
import unittest
from time import sleep
from selenium import webdriver
d = webdriver.Chrome()
# d.maximize_window()  # 最大化浏览器窗口
d.implicitly_wait(8)
#

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('执行测试用例')
        d.get("https://192.168.15.110:50443")  # 地址栏输入百度地址
        d.find_element_by_id('details-button').click()
        d.find_element_by_id('proceed-link').click()
    def tearDown(self) -> None:
        print('test,end')
class test_dakai(MyTestCase):
    def test_denglu(self):
        d.find_element_by_id('name').send_keys('sysadmin')  # 点击输入框，输入用户名
        d.find_element_by_id('password').send_keys('Admin@123')  # 点击密码输入框，输入密码
        d.find_element_by_id('clickLogin').click()  # 点击登录
        sleep(3)
        # d.find_element_by_id('button-1005').click()
        #       self.assertEqual(True, False)  # add assertion here
class test_xitong(MyTestCase):
    def test_xitongguanli(self):
        # d.find_element_by_id('ext-element-136').click()  # 点击系统管理
        # time.sleep(3)
        d.find_element_by_id('ext-element-114').click()
        # d.find_element_by_xpath('ext-element-89').clear()
        # time.sleep(2)

        # d.find_element_by_id('ip-inputEl').send_keys()
        # #点击并输入IP地址
    # def test_SNMP(self):
    #     d.find_element_by_id('')



if __name__ == '__main__':
    unittest.main()

