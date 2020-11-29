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

from config import DRIVER_PATH, URL, USER, PASSWORD
from pages.HomePage import HomePage


class TestMainElements():
 
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(URL)


    def test_Home(self):
        home_page = HomePage(driver)
        home_page.login(USER, PASSWORD)
        home_page.validate_carousel_items()
        # Check clicking on menues
        subscribe_page = home_page.go_to_menu_iten('Subscribe')
        subscribe_page.validate_text()