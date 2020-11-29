import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .BasePage import BasePage
from UImap import home_page_map


class HomePage(BasePage):
 
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
 
    def login(self, user, password):
        # locate login link
        hellobox = self.driver.find_element(*home_page_map['hello box'])
        hover = ActionChains(self.driver).move_to_element(hellobox)
        hover.perform()
        time.sleep(5)
        # click on it
        signin = self.driver.find_element(*home_page_map['signin_btn'])
        signin.click()
        time.sleep(10)
        return self

    def search_product(self):

        pass

    def add_first_non_sponsored(self):
        pass

    def buy_products(self):
        pass