from weihu import *
from selenium.webdriver.common.by import By
from selenium import webdriver

d =webdriver.Chrome()


class LoginPage(page):

 url=('https://192.168.15.170:50443/manage.htmlview-homepage')



# 定位器
 username_loc=(By.ID,'username')
 password_loc=(By.ID,'password')
 submit_loc=(By.ID,'clickLogin')

# 用户名输入框元素
def type_password(self,sysadmin):
    self.find_element(*self.username_loc).clear
    self.find_element(*self.username_loc).send_keny(username_loc)
# 密码输入框元素
def type_password(self,passwrod):
    self.find_element(*self.password_loc).clear
    self.find_element(*self.password_loc).send_keny(password_loc)
# 登录按钮元素
def type_submit_loc(self):
    self.find_element(*self.submit_loc).click


# 登录功能模块封装
def test_user_login(d,username,password):
# 测试用户名密码是否可以登录
    login_page=LoginPage(d)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()