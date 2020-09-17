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
        return self.driver.find_element(By.ID, 'maintitle')

    @property
    def signup_button(self):
        obs = self.driver.find_element(By.CLASS_NAME, "signup")
        return obs

    @property
    def halfbox(self):
        obs = self.driver.find_elements(By.CLASS_NAME, "halfbox")
        return obs