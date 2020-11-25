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


    def test_Home(self):
        home_page = HomePage(driver)
        home_page.validate_title()
        home_page.validate_carousel_items()
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        subscribe_page.validate_text()

        ##self.assertEqual(carousel_items_nmbr , 3, 
        ##    'There are {} order buttons and should be 3'.format(
        ##        carousel_items_nmbr))
        # Check for Carousel Title

        

    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


