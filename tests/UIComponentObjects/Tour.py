from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

TourLocators = Locators.TourLocators()

class Tour(object):
    '''The Tour class contains all methods for interacting with the tour.'''
    def __init__(self, driver):
        self.driver = driver

    def step_title_is_correct(self, className, stepTitle):
        '''Verify the first step is showing'''
        # Need to wait until the new element has displayed.
        # Timeout after 3 seconds
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, className))
        )
        h2Element = element.find_element_by_tag_name('h2')
        return stepTitle in h2Element.get_attribute('innerHTML')

    def click_next_button(self):
        '''Clicks the Tour next button'''
        element = self.driver.find_element(*TourLocators.NEXT_BUTTON)
        element.click()

    def click_close_button(self):
        '''Clicks the Tour close button'''
        element = self.driver.find_element(*TourLocators.CLOSE_BUTTON)
        element.click()
