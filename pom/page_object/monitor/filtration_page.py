from pom.base.base_page import BasePage


#过滤条件页面
class Filtration_page(BasePage):
    url='https://192.168.15.221:50443/manage.html#view-listen-rule'
    add=('xpath','//*[text()="添加"]')
    filtration=('xpath','//*[text()="过滤条件"]')
    agreement=('xpath','//*[text()="HTTP响应内容类型"]')
    add2_=('xpath','//*[text()="添加"]')
    name=('id','textfield-1294-inputEl')
    cf=('id','textfield-1295-inputEl')
    submit=('xpath','//*[text()="提交"]')

    def filtration_(self,name_,cf_):
        self.open(self.url)
        self.click(self.add)
        self.click(self.filtration)
        self.click(self.agreement)
        self.click(self.add2_)
        self.input(self.name,name_)
        self.input(self.cf,cf_)
        self.click(self.submit)
