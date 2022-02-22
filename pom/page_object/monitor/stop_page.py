from pom.base.base_page import BasePage

#通道启动
class StaerPage(BasePage):
    url='https://192.168.15.221:50443/manage.html#view-listen-rule'
    id_=('xpath','//*[text()="protocol"]') #通道ID
    stop=('xpath','//*[text()="停止"]')


    def Staer_page(self):
        self.open(self.url)
        self.click(self.id_)
        self.click(self.stop)