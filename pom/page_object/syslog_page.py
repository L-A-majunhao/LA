from pom.base.base_page import BasePage
from selenium import webdriver
import unittest


# syslog启动页面
class Syslog_page(BasePage):
    # syslog url
    url = ('https://192.168.15.221:50443/manage.html#view-syslog')
    # 接受地址
    take_ip = ('xpath', '//input[@id="textfield-1138-inputEl"]')
    # 启动
    start = ('id', 'checkbox-1139-inputEl')
    # syslog端口的元素
    syslog_port = ('id', 'numberfield-1140-inputEl')

    # 输入的端口
    # syslog_ports='514'

    def Syslong(self, ip, port):
        self.open(self.url)
        self.click(self.take_ip)
        self.input(self.take_ip, ip)
        self.click(self.start)
        self.input(self.syslog_port, port)
        self.wite(3)
        self.quit(self.driver)

