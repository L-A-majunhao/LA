import unittest
import time
from selenium import webdriver



d = webdriver.Chrome()
# d.maximize_window()  # 最大化浏览器窗口
# d.implicitly_wait(8)



d.get("https://192.168.15.131:50443")  # 地址栏输入百度地址
d.find_element_by_id('details-button').click()
d.find_element_by_id('proceed-link').click()
d.find_element_by_id('name').send_keys('superadmin')  # 点击输入框，输入用户名
d.find_element_by_id('password').send_keys('Admin@123')  # 点击密码输入框，输入密码
d.find_element_by_id('clickLogin').click()  # 点击登录
d.find_element('id','ext-element-261')
# d.find_element('id','//*[text()="监听地址"]')
# d.find_element('xpath','//*[text()="协议解析并摆渡通道"]')

js = 'return document.getElementById("combobox-1704-inputEl").removeAttribute("readonly")'
driver.execute_script(js)



if __name__ == '__main__':
    unittest.main()