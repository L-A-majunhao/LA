import unittest

from pom.base.base_page import BasePage
from selenium import webdriver
from time import sleep


# 常规页面
class RulePage(BasePage):
    # 常规URL
    url='https://192.168.15.130:50443/manage.html#view-system'
    url2='https://192.168.15.130:50443/manage.html#view-snmp'
    # IP地址
    input_ip=('id', 'ip-inputEl')
    # 掩码
    mask=('id', 'mask-inputEl')
    # 默认网关
    swg=('id', 'gateway-inputEl')
    # 保存
    save=('id', '//*[text()="保存"]')
    # dns1
    dns1=('id', 'textfield-1071-inputEl')
    # dns2
    dns2=('id', 'textfield-1072-inputEl')
    # dns保存
    save2=('id', 'button-1081-btnInnerEl')


    qd=('id','button-1005-btnInnerEl')


    #snmp启动按钮
    snmp=('id','checkbox-1063-inputEl')
    save3=('id','ip-inputEl')
    def system(self,qw,qw2,qw3,qw4,qw5):
        self.open(self.url)

        self.input(self.input_ip,qw)
        self.input(self.mask,qw2)
        self.input(self.swg,qw3)
        self.click(self.save)

        self.click(self.qd)
        self.input(self.dns1,qw4)
        self.input(self.dns2,qw5)
        self.click(self.save)
        # self.wite(3)
        self.click(self.qd)
        self.wite(1)


    # def snmp(self):
    #     self.open(self.url2)
    #     self.click(self.snmp)
    #     self.click(self.save3)
    #     self.wite(3)





    # input1="192.168.15.110"
    #
    # input2: 24
    #
    # input3="192.168.15.protocol"
    #
    # input4="114.114.114.114"
    #
    # input5= "114.114.115.115"
    #
    # driver=webdriver.Chrome
    # zp = RulePage(driver)

