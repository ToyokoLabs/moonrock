"""
Run these tests with:

pytest tests.py

"""

import os
import time
import random
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


    def _test_Home(self):
        home_page = HomePage(driver)
        home_page.validate_title()
        home_page.validate_carousel_items()
        # Check clicking on menues
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        subscribe_page.validate_text()

    @pytest.mark.parametrize("plan",['Kit1', 'Kit6', 'Kit12'])
    def _test_subscribe_to_box(self, plan):
        """
        This test checks an end to end subscription, testing all
        3 plans.
        """
        home_page = HomePage(driver)
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        card = subscribe_page.get_card(plan)
        total_price = subscribe_page.get_total_price(card)
        checkout_page = subscribe_page.click_get_started(card)
        # Test with a valid user
        user = users['valid_user']
        checkout_page.fill_main_form(**user)
        thank_you_page = checkout_page.submit_main_form()
        thank_you_page.check_successful_message(user['first_name'], 
                                                user['last_name'],
                                                plan, 
                                                total_price)


    def _test_subscribe_to_box_validation_error(self):
        """
        This test checks an end to end subscription, 
        with a validation error, after fixing the validation,
        the user should be able to complete the subscription.
        """
        home_page = HomePage(driver)
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        plan = random.choice(['Kit1', 'Kit6', 'Kit12'])
        card = subscribe_page.get_card(plan)
        total_price = subscribe_page.get_total_price(card)
        checkout_page = subscribe_page.click_get_started(card)
        # Get checkout page URL
        url_before_submit = driver.current_url
        # Test with a valid user
        user = users['user_wo_username']
        # Next fill will not complete user_name field
        checkout_page.fill_main_form(**user)
        checkout_page.submit_main_form()
        # Check that the browser is still in the same page
        url_after_submit = driver.current_url
        assert url_before_submit == url_after_submit, \
            "URL before submit: {}.\n URL after submit: {}".\
                format(url_before_submit, url_after_submit)
        checkout_page.check_validation_error('user_name_error')
        # Send the username
        checkout_page.fill_main_form(user_name = user['user_name'])
        thank_you_page = checkout_page.submit_main_form()
        thank_you_page.check_successful_message(user['first_name'], 
                                                user['last_name'],
                                                plan, 
                                                total_price)

    def test_subscribe_to_box_invalid_cc(self):
        """
        This test checks an end to end subscription, 
        with an invalid credit card.
        """
        home_page = HomePage(driver)
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        plan = random.choice(['Kit1', 'Kit6', 'Kit12'])
        card = subscribe_page.get_card(plan)
        checkout_page = subscribe_page.click_get_started(card)
        # Test with a user with invalid CC
        user = users['user_invalid_cc']
        # Next fill will not complete user_name field
        checkout_page.fill_main_form(**user)
        thank_you_page = checkout_page.submit_main_form()
        thank_you_page.check_error_message(user['first_name'], 
                                           user['last_name'],
                                        )

    #def teardown_method(self):
    #    driver.quit()
 

