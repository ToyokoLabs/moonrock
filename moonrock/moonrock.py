import os
import unittest
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# self.base_url = os.environ.get('RXENV', '')
#        driver.get(self.base_url)
driver.get('https://www.py3.us')