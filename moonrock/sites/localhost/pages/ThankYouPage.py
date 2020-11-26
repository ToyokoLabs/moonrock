import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
from .BasePage import BasePage
from helper import Colors
from UImap import thankyou_page_map

color = Colors()
 
class ThankYouPage(BasePage):
    
    def __init__(self, driver):
        super(ThankYouPage, self).__init__(driver)

    def check_successful_message(self, firstname, lastname):
        fullname = '{} {}'.format(firstname, lastname)
        msg = self.driver.find_element(*thankyou_page_map['message_heading'])
        assert msg.text == 'Thank you for subscribing {}'.format(fullname), msg.text
