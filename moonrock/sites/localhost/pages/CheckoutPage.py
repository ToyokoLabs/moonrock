import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
from .BasePage import BasePage
from .ThankYouPage import ThankYouPage
from helper import Colors
from UImap import checkout_page_map

color = Colors()
 
class CheckoutPage(BasePage):

    def __init__(self, driver):
        super(CheckoutPage, self).__init__(driver)

    # Actions

    def fill_main_form(self, **data):
        for item in data:
            field = self.driver.find_element(*checkout_page_map[item])
            field.send_keys(data[item])
        """
        select = Select(self.driver.find_element(*checkout_page_map['country']))
        select.select_by_visible_text("United States")
        select = Select(self.driver.find_element(*checkout_page_map['state']))
        select.select_by_visible_text("California")
        """
        return self


    def submit_main_form(self):
        btn = self.driver.find_element(*checkout_page_map['checkout_button'])
        btn.click()
        return ThankYouPage(self.driver)

        