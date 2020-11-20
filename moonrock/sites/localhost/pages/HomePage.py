import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
from .BasePage import BasePage
from UImap import home_page_map
 
 
class HomePage(BasePage):
 
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
 
    @property
    def logo_title(self):
        logotitle = self.driver.find_element(*home_page_map['pagelogotitle'])
        # Check properties
        #a = mt.find_element_by_tag_name('a')
        #if 'Playfair Display' in a.value_of_css_property('font-family'):
        #    print('Playfair Display')
        #else:
        #    print('NO Playfair Display')
        return logotitle

    @property
    def carousel_items(self):
        items = self.driver.find_elements(*home_page_map['carousel_item'])
        carousel_items = []
        for item in items:
            title = item.find_element_by_tag_name('h1')
            text = item.find_element_by_tag_name('p')
            button = item.find_element_by_class_name('btn-primary')
            carousel_items.append((title, text, button))
        return carousel_items



    @property
    def signup_button(self):
        obs = self.driver.find_element(*home_page_map['signup_button'])
        return obs

    @property
    def halfbox(self):
        obs = self.driver.find_elements(*home_page_map['halfbox'])
        return obs