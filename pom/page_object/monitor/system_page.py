from pom.base.base_page import BasePage
import os

#监听通道  添加
class System_Page(BasePage):
    url='https://192.168.15.221:50443/manage.html#view-listen-rule'

    add_=('xpath',"//*[text()='添加']")#添加
    name_=('id',"@role='textbox'")#名称
    id_=('id','numberfield-1285-inputEl')#id
    genre_=('id','combo-1286-inputEl')#协议类型
    # http_genre=('xpath',"2") #http协议
    site_=('id','combo-1288-inputEl')#监听地址
    site=('id','ext-603')
    listener_port_=('id','numberfield-1126-inputEl')#监听端口
    submit_=('id','button-1289-btnInnerEl')#提交
    perform=('id','button-1005-btnInnerEl')


    def system(self, user, ID, listener_port,HTTP,ip):
        self.open(self.url)
        self.click(self.add_)
        self.input(self.name_,user)
        self.input(self.id_,ID)
        self.wite(1)
        js = 'return document.getElementById("combo-1286-inputEl").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input(self.genre_,HTTP)
        js = 'return document.getElementById("combo-1288-inputEl").removeAttribute("readonly")'
        self.driver.execute_script(js)
        self.input(self.site_,ip)
        self.input(self.listener_port_,listener_port)
        self.click(self.submit_)
        self.click(self.perform)