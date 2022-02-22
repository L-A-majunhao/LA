from pom.base.base_page import BasePage

#snmp启动页面
class SNMP(BasePage):
    url=('https://192.168.15.221:50443/manage.html#view-snmp')
    id=('id','checkboxfield-1075-inputEl')
    save=('id','button-1077-btnInnerEl')
    def Snmp(self):
        self.open(self.url)
        self.click(self.id)
        self.click(self.save)
