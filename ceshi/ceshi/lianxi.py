from selenium import webdriver
from time import sleep

options=webdriver.ChromeOptions()
options.add_argument('start_maximized')#更改浏览器默认设置，启动时默认最大化
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
sleep(1)
driver.get('https://music.163.com/')
driver.find_element('link text','登录').click()
driver.find_element('xpath','//*[@id="otherbtn"]/a').click()
driver.find_element('id','j-official-terms').click()
driver.find_element('xpath',"//i[@class='u-mlg2 u-mlg2-qq']").click()
# driver.find_element('link text','qq等录')
handles=driver.window_handles #获取当前浏览器所有句柄
print(driver.title)   #打印当前标签页title
print(handles)
sleep(1)
driver.switch_to.window(handles[1])# 切换句柄到新的标签页
sleep(2)
print(driver.title)
driver.switch_to.frame('ptlogin_iframe') #切换到iframe  iframe只能切换的当前标签页内才能操作
driver.find_element('xpath','//*[@id="img_out_469052173"]').click()
driver.switch_to.default_content()#切换回进入iframe前的窗口
driver.switch_to.window(handles[0])#切换回第一个句柄
sleep(3)
print(driver.title)
driver.find_element('id','follow_count').click()


