
import unittest
from pom.base.base_page import BasePage

#配置管理页面
class Cnmd_page(BasePage):
    url='https://192.168.15.110:50443/manage.html#view-sys-config'
    derive=('id','button-1093-btnInnerEl')
