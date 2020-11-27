import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
from .BasePage import BasePage
from .ThankYouPage import ThankYouPage
from helper import Colors
from UImap import checkout_page_map

expected_color = Colors()


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

    def check_validation_error(self, error_name):
        """
        Check that there is an error message with the right color
        """
        error = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(
                        checkout_page_map[error_name]
                        )
                )
        #import pdb; pdb.set_trace()
        assert 'is required.' in error.text, error.text
        color = error.value_of_css_property('color')
        assert expected_color.RED_ERROR == color, color
        return self
