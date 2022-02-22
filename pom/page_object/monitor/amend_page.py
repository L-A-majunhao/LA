from pom.base.base_page import BasePage

#修改通道信息
class Amendpage(BasePage):
    url=''
    amend = ('', '')
    save = ('xpath', "//*[text()='修改']")
    name = ('id', '')#通道名称
    genre_ = ('', '')#协议类型
    site_ = ('', '')#监听地址
    port = ('', '')
    submit = ('', '')
    listener_port_=('','')

    def Amend_page(self,name_=None,site=None,port_=None):
        self.open(self.url)
        self.click(self.amend)
        self.click(self.save)
        self.input(self.name,name_)
        self.click(self.genre_)
        self.click(self.genre_)
        self.input(self.site_,site)
        self.input(self.listener_port_,port_)
        self.click(self.submit)