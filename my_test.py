import time
from selenium import webdriver

from selenium.webdriver.support.select import Select

d = webdriver.Chrome()
d.maximize_window()  # 最大化浏览器窗口
d.implicitly_wait(8)
d.get("https://192.168.15.140:50443")  # 地址栏输入百度地址
d.find_element('id','details-button').click()
d.find_element('id','proceed-link').click()
d.find_element('id','input-uname').send_keys('superadmin') #点击输入框，输入用户名
d.find_element('id','input-upwd').send_keys('Admin@123') #点击密码输入框，输入密码
d.find_element('id','loginBtn').click() #点击登录
d.find_element('id','ext-element-239')
d.find_element('id','ext-element-213')
d.find_element('id','ext-element-203')
d.find_element('id','button-1076')
d.find_element('id','combo-1113-inputEl')
# d.find_element('id',"")
# d.find_element('id','ext-element-115').click() #系统管理
# d.find_element('id','ext-element-136').click() #网络管理
# # time.sleep(3)
# # d.find_element_by_id('ext-treelistitem-15').click() #点击常规
# # time.sleep(3)
# # d.find_element_by_id('ext-treelistitem-16').click() #点击snmp
# # time.sleep(3)
# d.find_element_by_id('ext-treelistitem-17').click() #点击syslong
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-18').click() #点击配置管理
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-19').click() #点击系统升级
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-20').click() #点击网络管理
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-21').click() #点击IP地址管理
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-22').click() #点击路由管理
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-23').click() #点击网络诊断
# time.sleep(3)
# d.find_element_by_id('ext-treelistitem-24').click() #点击路由管理
# time.sleep(3)
# d.find_element_by_id('main-navigation-btn-btnIconEl').click() #点击菜单伸缩按钮
# time.sleep(3)
# d.find_element_by_id('button-1014').click() #点击设备信息
# time.sleep(3)
# d.find_element_by_id('tool-1114').click()
# time.sleep(3)
# d.find_element_by_id('userBtn-btnIconEl').click() #点击用户信息
# time.sleep(3)
# d.find_element_by_id('userBtn-btnIconEl').click() #点击用户信息
# time.sleep(3)
