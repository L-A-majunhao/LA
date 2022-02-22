import unittest

from ddt import ddt,file_data
from selenium import webdriver
from pom.base.chrome_options import ChromeOptions
from pom.page_object.monitor.system_page import System_Page


@ddt
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome(options=ChromeOptions().options())
        cls.jt = System_Page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data_yaml/aisle.yaml')
    def test_06_system(self, name, id, listener_port):
        self.jt.system(name, id, listener_port)

if __name__ == '__main__':
    unittest.main()
