import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
d=webdriver.Chrome()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        d.get('https://192.168.15.170:50443')
        sleep(2)
        d.find_element
        sleep(2)
# self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
