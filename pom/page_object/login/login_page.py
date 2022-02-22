

from pom.base.base_page import BasePage
import unittest
class LoginPage(BasePage):
    url=('https://192.168.15.221:50443')
    username=('id','input-uname')
    pwd=('id','input-upwd')
    button=('xpath','//*[text()="登录"]')
    gaoji=('id','details-button')
    anquan=('id','proceed-link')
    def longin(self,name,password):
        self.open(self.url)
        self.click(self.gaoji)
        self.click(self.anquan)
        self.input(self.username,name)
        self.input(self.pwd,password)
        self.click(self.button)
        self.wite(3)# 页面对象类


# if __name__ == '__main__':
#     unittest.main
#     driver =webdriver.Chrome()
#     lp = LoginPage(driver)
#     name='sysadmin'
#     password='Admin@123'
#     lp.longin(name,password)
