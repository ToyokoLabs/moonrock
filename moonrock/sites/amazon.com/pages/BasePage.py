import time


class LocatorMode:
    ID = "id"
    NAME = "name"
    XPATH = "xpath"
    CSS_SELECTOR = "cssSelector"
 
 
class BasePage:
 
    def __init__(self, driver, url=None):
        self.driver = driver

    
    @property
    def body_root(self):
        return self.driver.find_element_by_tag_name('body')
