import chromedriver
from selenium import webdriver
from time import sleep
from selenium .webdriver.chrome.webdriver import WebDriver
driver=webdriver.Chrome()
driver.get('https://baidu.com')
driver.find_element('id','kw').send_keys('虚竹')
driver.find_element('id','su').click()
