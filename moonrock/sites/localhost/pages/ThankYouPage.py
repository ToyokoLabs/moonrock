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

    def check_successful_message(self, firstname, lastname, plan, totalprice):
        fullname = '{} {}'.format(firstname, lastname)
        kitnumber = plan[3:]
        msg = self.driver.find_element(*thankyou_page_map['msg_heading'])
        assert msg.text == 'Thank you for subscribing {}'.format(fullname), msg.text
        msg = self.driver.find_element(*thankyou_page_map['msg_subtext'])
        assert msg.text == 'We got your order for MoonRock Kit {} at ${}'.\
            format(kitnumber, totalprice), msg.text