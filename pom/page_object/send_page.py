from pom.base.base_page import BasePage
import os

#发送通道  添加
class Send_Page(BasePage):
    url='https://192.168.15.221:50443/manage.html#view-listen-rule'

    add_=('xpath',"//*[text()='添加']")#添加
    name_=('id','textfield-1117-inputEl')#名称
    id_=('id','numberfield-1119-inputEl')#id
    genre_=('id','combobox-1120-inputEl')#协议类型
    # http_genre=('xpath',"2") #http协议
    site_=('id','combobox-1122-inputEl')#发送地址
    DA=('','')#目的地址
    listener_port_=('id','numberfield-1123-inputEl')#目的端口
    submit_=('id','button-1150-btnInnerEl')#提交


    def Send(self, user, ID, listener_port,HTTP,ip,da):
        self.open(self.url)
        self.click(self.add_)
        self.input(self.name_,user)
        self.input(self.id_,ID)
        self.wite(1)
        js = 'return document.getElementById("combobox-1120-inputEl").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input(self.genre_,HTTP)
        js = 'return document.getElementById("combobox-1122-inputEl").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input(self.site_,ip)
        js = 'return document.getElementById("combobox-1122-inputEl").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input(self.DA,da)
        self.input(self.listener_port_,listener_port)
        self.click(self.submit_)