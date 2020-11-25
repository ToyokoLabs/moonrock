import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
from .BasePage import BasePage
from helper import Colors
from UImap import subscribe_page_map

color = Colors()
 
class SubscribePage(BasePage):

    def __init__(self, driver):
        super(SubscribePage, self).__init__(driver)

    @property
    def title(self):
        #import pdb; pdb.set_trace()
        maintext = self.find_element(*subscribe_page_map['maintext'])
        title = maintext.find_element_by_tag_name('h1')
        return title

    # Validations

    def validate_text(self):
        title = self.title
        #import pdb; pdb.set_trace()
        assert title.text == 'Subscription Boxes', title.text 



