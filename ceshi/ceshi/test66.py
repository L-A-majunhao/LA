from selenium.webdriver.chrome.webdriver import WebDriver

from basepage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
d=webdriver.Chrome()
username='sysadmin'
password='Admin@123'
d.find_element(By.ID, 'details-button').click()
d.find_element(By.ID, 'proceed-link').click()
test_user_login(d,username,password)
sleep(3)
d.quit()