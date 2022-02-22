from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest

from my_test import d


class page():
    def __init__(self,d):
        self.d=d
        self.base_url='https://192.168.15.170:50443/manage.html#view-homepage'
        # d.find_element(By.ID, 'details-button').click()
        # d.find_element(By.ID, 'proceed-link').click()
    def _open(self,url):
        url_=self.base_url+url
        print('test page is %s' %url_)
        # self.d.maximize.window()
        self.d.get(url_)
        d.find_element(By.ID, 'details-button').click()
        d.find_element(By.ID, 'proceed-link').click()
        sleep(2)
        assert self.d.current_url==url_,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.d.find_element(*loc)

