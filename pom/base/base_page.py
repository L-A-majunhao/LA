import logging
from time import sleep
from selenium import webdriver
# 基类

from selenium.webdriver.support.select import Select
from undetected_chromedriver import ChromeOptions
import logging.config
import os


# def open_browser(type_):
#     if type_ == 'Chrome':
#         driver = webdriver.Chrome(options=ChromeOptions().options())
#     else:
#         try:
#             driver = getattr(webdriver, type_)()
#         except Exception as e:
#             print("Exception Information:" + str(e))
#             driver = webdriver.Chrome()
#     return driver

from pom.logs.log1 import test_log
log=test_log()
class BasePage:

    # driver=webdriver.Chrome()
    #
    def __init__(self, driver):
        log.info('初始化浏览器{}'.format(driver))
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, url):
        log.info('正在打开{}网址'.format(url))
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).clear()
        log.info('通过{}定位，输入{}内容'.format(loc, txt))
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        log.info('通过{}定位，进行点击'.format(loc))
        self.locator(loc).click()

    # 等待
    def wite(self, txt):
        log.info('正在等待')
        sleep(txt)

    def user(self, loc):
        self.locator(loc).clear()

    # 退出
    def quit(self, driver):
        log.info('正在等待')
        self.quit(driver)

    def inport(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def select(self, loc, txt):
        self.select = Select(self.locator(loc))
        self.select.select_by_value(txt)

    # def input2(self, loc, txt):
    #     if txt == None:
    #         self.locator(loc).send_keys(txt)
    #     else:
    #
    #         self.locator(loc).clear()
    #         self.locator(loc).send_keys(txt)

    def remove(self,name):
        js='return document.getElementById("name").removeAttribute("readonly")'
        self.driver.execute_script(js)