import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
from .BasePage import BasePage
 
 
class HomePage(BasePage):
 
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
 
    @property
    def main_title(self):
        mt = self.driver.find_elements_by_class_name("maintitle")
        return mt[0]

    @property
    def order_buttons(self):
        obs = self.driver.find_elements_by_class_name("orderbutton")
        return obs
