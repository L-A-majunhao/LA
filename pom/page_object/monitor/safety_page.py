from pom.base.base_page import BasePage

class Safety_Page(BasePage):

    url='https://192.168.15.221:50443/manage.html#view-safe-rule'
    add=('id','button-1142-btnInnerEl')
    name=('id','//input[@name="name"]')
    natework=('id','//input[@name="ifaceId"]')
    submit=('xpath','//*[text()="提交"]')

    def safety(self,name_,slot):
        self.open(self.url)
        self.click(self.add)
        self.input(self.name,name_)
        self.input(self.natework,slot)
        self.click(self.submit)
