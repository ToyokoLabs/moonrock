
# UI Map of page objects

from selenium.webdriver.common.by import By


home_page_map = { 'maintitle': (By.ID, 'maintitle'),
    'signup_button' : (By.CLASS_NAME, "signup"),
    'halfbox' : (By.CLASS_NAME, "halfbox")
}

carousel_map = {}

checkout_map = {}