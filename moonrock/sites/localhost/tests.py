"""
Run these tests with:

pytest tests.py

"""

import os
import time
import pytest
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from config import DRIVER_PATH, URL
from helper import users
from pages.HomePage import HomePage



class TestMainElements():
 
    def setup_class(self):
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

    @pytest.mark.parametrize("plan",['Kit1', 'Kit6', 'Kit12'])
    def test_subscribe_to_box(self, plan):
        # TODO: parametrize this.
        home_page = HomePage(driver)
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        # choose plan 1
        card = subscribe_page.get_card(plan)
        total_price = subscribe_page.get_total_price(card)
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
        thank_you_page.check_successful_message(user['firstname'], 
                                                user['lastname'],
                                                plan, 
                                                total_price)
        #import pdb; pdb.set_trace()
        
#We got your order for MoonRock Kit 1 at $15
#We got your order for MoonRock Kit 6 at $72
#We got your order for MoonRock Kit 12 at $108


    #def teardown_method(self):
    #    driver.quit()
 

