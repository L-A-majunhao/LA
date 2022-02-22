import unittest
from time import sleep
from selenium import webdriver
# d.maximize_window()  # 最大化浏览器窗口
# d.implicitly_wait(8)

d=webdriver.Chrome()
#

d.get("https://192.168.15.110:50443")  # 地址栏输入百度地址
d.find_element('id','details-button').click()
d.find_element('id','proceed-link').click()
d.find_element('id','name').send_keys('sysadmin')  # 点击输入框，输入用户名
d.find_element('id','password').send_keys('Admin@123')  # 点击密码输入框，输入密码
d.find_element('id','clickLogin').click()  # 点击登录
sleep(3)
d.get('https://192.168.15.110:50443/manage.html#view-system')
sleep(3)
d.find_element('id','ip-inputEl').clear()

d.find_element('id','ip-inputEl').send_keys('192.168.15.111')