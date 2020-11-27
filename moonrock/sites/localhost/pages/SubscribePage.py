import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
from .BasePage import BasePage
from helper import Colors
from UImap import subscribe_page_map
from .CheckoutPage import CheckoutPage

color = Colors()
 
class SubscribePage(BasePage):

    def __init__(self, driver):
        super(SubscribePage, self).__init__(driver)

    @property
    def title(self):
        maintext = self.find_element(*subscribe_page_map['maintext'])
        title = maintext.find_element_by_tag_name('h1')
        return title

    def get_card(self, plan):
        """
        """
        cards = self.driver.find_elements(*subscribe_page_map['subscribecards'])
        d = {'Kit1': 0, 'Kit6': 1, 'Kit12': 2}
        return cards[d[plan]]

    def get_total_price(self, card):
        """
        Given a card, calculate total price (without discounts)
        """
        length = card.find_element(*subscribe_page_map['card_price'])
        price = length.text.split(' ')[0]
        assert price[0] == '$', 'Unit is {} and should be $'.format(price[0])
        price = int(price[1:])
        lapse = card.find_element(*subscribe_page_map['card_length'])
        lapse_amount, lapse_unit = lapse.text.split(' ')
        lapse_amount = int(lapse_amount)
        if 'Month' in lapse_unit:
            total_price = lapse_amount * price
        elif 'Year' in lapse_unit:
            total_price = lapse_amount * 12 * price
        return total_price



    def click_get_started(self, card):
        checkout = card.find_element(*subscribe_page_map['get_started_button'])
        checkout.click()
        return CheckoutPage(self.driver)


    # Validations

    def validate_text(self):
        title = self.title.text
        #import pdb; pdb.set_trace()
        assert title == 'Subscription Boxes', title



