
# UI Map of page objects

from selenium.webdriver.common.by import By


home_page_map = { 'pagelogotitle': (By.CLASS_NAME, 'pagelogotitle'),
    'carousel_item': (By.CLASS_NAME, 'carousel-item'),
    'top_menu_items': (By.CLASS_NAME, 'navbar-nav'),
    #'signup_button' : (By.CLASS_NAME, "signup"),
    #'halfbox' : (By.CLASS_NAME, "halfbox")
}

subscribe_page_map = {'maintext': (By.CLASS_NAME, 'maintext'),
                      'subscribecards': (By.CLASS_NAME, 'card'),
                      'get_started_button': (By.TAG_NAME, 'a'),
                    }

carousel_map = {}

checkout_page_map = {'first_name': (By.ID, 'firstName'),
                    'last_name': (By.ID, 'lastName'),
                    'user_name': (By.ID, 'username'),
                    'address1': (By.ID, 'address'),
                    'country': (By.ID, 'country'),
                    'state': (By.ID, 'state'),
                    'zip': (By.ID, 'zip'),
                    'name_on_card': (By.ID, 'cc-name'),
                    'number_on_card': (By.ID, 'cc-number'),
                    'cvv': (By.ID, 'cc-cvv'),
                    'checkout_button': (By.CSS_SELECTOR, 'button.chkout'),
                    }

thankyou_page_map = {'message_heading': (By.CSS_SELECTOR, 
                                     'div > h1.cover-heading')}

