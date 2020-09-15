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
        driver.get(py3us.URL)
 
    def test_BasicHome(self):
        home_page = HomePage(driver)
        title = home_page.main_title.text
        # Check for title
        self.assertEqual(title, 'Python for Bioinformatics')
        # Check that title is displayed
        self.assertTrue(home_page.main_title.is_displayed)

        

    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


