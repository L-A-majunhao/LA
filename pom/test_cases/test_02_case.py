import unittest


from selenium import webdriver
from ddt import ddt, file_data

from pom.base.chrome_options import ChromeOptions
from pom.page_object.login.login_page import LoginPage
from pom.page_object.system_page import System_Page

@ddt
class TestDemo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=ChromeOptions().options())
        cls.lp = LoginPage(cls.driver)
        cls.jt = System_Page(cls.driver)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # @data(['superadmin', 'Admin@123', ])
    # @unpack
    def test_01_login(self):
        name='superadmin'
        password='Admin@123'
        self.lp.longin(name,password)


    @file_data("../data/aisle.yaml")
    def test_06_system(self, user, ID, listener_port):
        self.jt.system(user, ID, listener_port)

if __name__ == '__main__':
    unittest.main()

