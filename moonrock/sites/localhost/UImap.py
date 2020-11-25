
# UI Map of page objects

from selenium.webdriver.common.by import By


home_page_map = { 'pagelogotitle': (By.CLASS_NAME, 'pagelogotitle'),
    'carousel_item': (By.CLASS_NAME, 'carousel-item'),
    'top_menu_items': (By.CLASS_NAME, 'navbar-nav'),
    #'signup_button' : (By.CLASS_NAME, "signup"),
    #'halfbox' : (By.CLASS_NAME, "halfbox")
}

subscribe_page_map = {'maintext': (By.CLASS_NAME, 'maintext'),
                    }
carousel_map = {}

checkout_map = {}

