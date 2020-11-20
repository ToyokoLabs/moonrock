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
        title = home_page.logo_title.text
        # Check for main title
        self.assertEqual(title, 'MoonRock')
        # Check that title is displayed
        self.assertTrue(home_page.logo_title.is_displayed)
        # Check for items in the carousel
        carousel_items = home_page.carousel_items
        carousel_items_nmbr = len(carousel_items)
        self.assertEqual(carousel_items_nmbr , 3, 
            'There are {} order buttons and should be 3'.format(
                carousel_items_nmbr))
        # Check for Carousel text
        for carousel_item in carousel_items:
            title = carousel_item[0]
            print(title.get_attribute('innerHTML'))
            #import pdb; pdb.set_trace()

        

    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


