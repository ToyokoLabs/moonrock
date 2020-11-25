import time
 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

 
from .BasePage import BasePage
from helper import Colors
from UImap import home_page_map
from .SubscribePage import SubscribePage


color = Colors()
 
class HomePage(BasePage):
 
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    @property
    def carousel_items(self):
        items = self.driver.find_elements(*home_page_map['carousel_item'])
        carousel_items = []
        for item in items:
            d = {'title': item.find_element_by_tag_name('h1'),
                 'text': item.find_element_by_tag_name('p'),
                 'button': item.find_element_by_class_name('btn-primary')}
            carousel_items.append(d)
        return carousel_items

    @property
    def logo_title(self):
        logotitle = self.driver.find_element(*home_page_map['pagelogotitle'])
        #a = mt.find_element_by_tag_name('a')
        #if 'Playfair Display' in a.value_of_css_property('font-family'):
        return logotitle

    @property
    def signup_button(self):
        obs = self.driver.find_element(*home_page_map['signup_button'])
        return obs

    @property
    def halfbox(self):
        obs = self.driver.find_elements(*home_page_map['halfbox'])
        return obs

    # Validations

    def validate_title(self):
        # Check that title is displayed
        title = self.logo_title
        assert title.is_displayed, 'Title is not displayed'
        # Check title text
        assert title.text == "MoonRock", 'Title is {}'.format(title.text)
        # Check size
        assert title.value_of_css_property('font-size') == '20px'
        # Check color
        assert title.value_of_css_property('color') == color.WHITE

    def validate_carousel_items(self):
        expected_items = (
            ('MoonRock', 
            'Join us on a voyage of discovery and explore and learn.',
            'Join Us Today',
            'rgba(255, 255, 255, 1)'),
            ('Explore and Learn', 
            'Bringing you everything under the Moon.', 
            'Learn Now',
            'rgba(255, 255, 255, 1)'),
            ('MoonRock Kits', 
            'Your purchase helps the MoonRock bring exciting learning experiences to everyone!.', 
            'Subcribe Today',
            'rgba(255, 255, 255, 1)')
            )
        items = self.carousel_items
        for item, expected in zip(items, expected_items):
            title = item['title'].get_attribute('innerHTML')
            assert title == expected[0], title
            titlecolor = item['title'].value_of_css_property('color')
            assert titlecolor == expected[3], titlecolor 
            description = item['text'].get_attribute('innerHTML')
            assert description == expected[1], description
            button = item['button'].get_attribute('innerHTML')
            assert button == expected[2], color.WHITE

    # Actions

    def go_to_menu_iten(self, menu_item):
        """
        Valid options:
        'Home', 'Explore', 'Learn', 'Subscribe' and 'Contact'
        """
        top_menu_items = self.driver.find_elements(*home_page_map['top_menu_items'])
        top_menu_items = top_menu_items[0].find_elements_by_tag_name('li')
        items_d = {'Home': (0, HomePage(self.driver)), 
                   'Explore': (1,), 
                   'Learn': (2,), 
                   'Subscribe': (3, SubscribePage(self.driver)), 
                   'Contact': (4,)
                   }
        #import pdb; pdb.set_trace()
        chosen_menu_item = top_menu_items[items_d[menu_item][0]]
        chosen_menu_item.find_element_by_tag_name('a').click()
        return items_d[menu_item][1]

