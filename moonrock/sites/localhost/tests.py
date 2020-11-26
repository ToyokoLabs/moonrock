import os
import time
import unittest
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from config import DRIVER_PATH, URL
from helper import users
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
        # Check clicking on menues
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        subscribe_page.validate_text()


    def test_subscribe_to_box(self):
        home_page = HomePage(driver)
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        # choose plan 1
        card = subscribe_page.get_card('Kit1')
        checkout_page = subscribe_page.click_get_started(card)
        # Test with a valid user
        user = users['valid_user']
        checkout_page.fill_main_form(first_name = user['firstname'],
                                    last_name = user['lastname'],
                                    user_name = user['username'],
                                    address1 = user['address1'],
                                    country = user['country'],
                                    state = user['state'],
                                    zip = user['zip'],
                                    name_on_card = user['name_on_card'],
                                    number_on_card = user['number_on_card'],
                                    cvv = user['cvv'])
        thank_you_page = checkout_page.submit_main_form()
        thank_you_page.check_successful_message(user['firstname'], user['lastname'])
        


    def tearDown(self):
        driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()


