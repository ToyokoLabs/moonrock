import os
import unittest
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from localconfig import DRIVER_PATH
from sites import py3us
from sites.py3us.HomePage import HomePage




class SearchDrug(unittest.TestCase):
 
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        #self.base_url = os.environ.get('RXENV', 'https://www.goodrx.com')
        driver.get(py3us.URL)
        # Set the cookie to prevent AB testing
        driver.add_cookie({
            'name': 'grx_internal_user',
            'value': 'true'
        })
        driver.refresh()
 
    def test_BasicHome(self):
        home_page = HomePage(driver)


    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


