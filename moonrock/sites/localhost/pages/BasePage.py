import time


class LocatorMode:
    ID = "id"
    NAME = "name"
    XPATH = "xpath"
    CSS_SELECTOR = "cssSelector"
    TAG = 'tag name'
    CLASS = 'class name'
 
 
class BasePage:
 
    def __init__(self, driver, url=None):
        self.driver = driver

    
    @property
    def body_root(self):
        return self.driver.find_element_by_tag_name('body')

    # Actions

    def find_element(self, locatorMode, Locator):
        """
        Given a locator, find an element.
        Return: Element
        """
        element = None
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)
        elif locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)
        elif locatorMode == LocatorMode.CSS_SELECTOR: 
            element = self.driver.find_element_by_css_selector(Locator)
        elif locatorMode == LocatorMode.TAG: 
            element = self.driver.find_element_by_tag_name(Locator)
        elif locatorMode == LocatorMode.CLASS: 
            element = self.driver.find_element_by_class_name(Locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element