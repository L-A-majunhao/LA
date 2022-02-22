from selenium import webdriver
import unittest
from time import sleep
import os
driver=webdriver.Chrome()
driver.get('https://192.168.15.131:50443')

d=driver.find_element("//*[@id='divform']/div[2]/ul[2]/li[3]/span[2]/input[1]")
driver.execute_script('arguments[0].removeAttribute(\"readonly\")', d)

self.locter(*loc)
self.execute_script('arguments[0].removeAttribute(\"readonly\")',self.locter(*loc))
