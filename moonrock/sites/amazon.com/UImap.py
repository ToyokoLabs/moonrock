
# UI Map of page objects

from selenium.webdriver.common.by import By


home_page_map = { 'hello box': (By.CSS_SELECTOR, '#nav-link-accountList'),
    'signin_btn': (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a > span'),
    'user_box': (By.CSS_SELECTOR, '#ap_email'),
    'continue_btn': (By.CSS_SELECTOR, '#continue'),
    'psw_box': (By.CSS_SELECTOR, '#ap_password'),
    'signin_btn': (By.CSS_SELECTOR, '#signInSubmit'),
    }


#nav-link-accountList