
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
                      'card_title': (By.CSS_SELECTOR, 'div.card-header > h4'),
                      'card_length': (By.CSS_SELECTOR, 'div.card-header > h5'),
                      'card_price':(By.CSS_SELECTOR, 'div.card-body > h1')
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

thankyou_page_map = {'msg_heading': (By.CSS_SELECTOR, 
                                     'div > h1.cover-heading'),
                    'msg_subtext': (By.CSS_SELECTOR, 
                                    'div > div.col-md-6 > p:nth-child(1)')
                                    }

