from pom.base.base_page import BasePage

#通道删除页面
class Removepage(BasePage):
    url='https://192.168.15.221:50443/manage.html#view-send-rule'
    remove=('xpath',"//*[text()='删除'")
    id_=('id','')#通道名称
    are=('xpath','//*[text()="是"]')
    def Remove_page(self):
        self.open(self.url)
        self.click(self.id_)
        self.click(self.remove)
        self.click(self.are)