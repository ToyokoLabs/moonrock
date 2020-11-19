import os
import unittest
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from config import DRIVER_PATH, URL

from pages.HomePage import HomePage



class MainElements(unittest.TestCase):
 
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(URL)
 
    def test_BasicHome(self):
        home_page = HomePage(driver)
        title = home_page.logo_title.text
        # Check for main title
        self.assertEqual(title, 'MoonRock')
        # Check that title is displayed
        self.assertTrue(home_page.logo_title.is_displayed)
        # Check there are 2 order buttons
        #order_buttons = home_page.order_buttons
        #obn = len(order_buttons)
        #self.assertEqual(obn,2, 
        #    'There are {} order buttons and should be 2'.format(obn))

        

    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


