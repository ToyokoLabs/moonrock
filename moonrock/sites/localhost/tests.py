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

    def _carousel_content_check(self, items):
        expected_items = (
            ('MoonRock', 
            'Join us on a voyage of discovery and explore and learn.',
            'Join Us Today',
            'rgba(255, 255, 255, 1)'),
            ('Explore and Learn', 
            'Bringing you everything under the Moon.', 
            'Learn Now',
            'rgba(255, 255, 255, 1)'),
            ('MoonRock Kits', 
            'Your purchase helps the MoonRock bring exciting learning experiences to everyone!.', 
            'Subcribe Today',
            'rgba(255, 255, 255, 1)')
            )
        for item, expected in zip(items, expected_items):
            title = item['title'].get_attribute('innerHTML')
            self.assertEqual(title, expected[0])
            titlecolor = item['title'].value_of_css_property('color')
            self.assertEqual(titlecolor, expected[3])
            description = item['text'].get_attribute('innerHTML')
            self.assertEqual(description, expected[1])
            button = item['button'].get_attribute('innerHTML')
            self.assertEqual(button, expected[2])
            'rgba(255, 255, 255, 1)'


    def test_Home(self):
        home_page = HomePage(driver)
        home_page.validate_title()
        #home_page.validate_carousel_items()
        # Check for items in the carousel
        ##carousel_items = home_page.carousel_items
        ##carousel_items_nmbr = len(carousel_items)
        ##self.assertEqual(carousel_items_nmbr , 3, 
        ##    'There are {} order buttons and should be 3'.format(
        ##        carousel_items_nmbr))
        # Check for Carousel Title
        ##self._carousel_content_check(carousel_items)

        

    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


