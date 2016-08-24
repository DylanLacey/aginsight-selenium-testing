from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

FooterLocators = Locators.FooterLocators()

class Footer(object):
    '''The Footer class contains all methods for interacting with the footer.'''
    def __init__(self, driver):
        self.driver = driver

    def get_current_coord_sys(self):
        '''Method to return the current coordinate system showing'''
        element = self.driver.find_element_by_css_selector('.slide-toggle-label')
        return element.get_attribute('innerHTML')

    def verify_coord_sys(self, oldCoordSys):
        '''Method to check the oldCoordSys passed in, is not currently showing'''
        element = self.driver.find_element_by_css_selector('.slide-toggle-label')
        return oldCoordSys in element.get_attribute('innerHTML')

    def new_window_is_open(self, title):
        '''Method to verify that the disclaimer window has opened in the browser'''
        # Get the current window and the openend window
        main_window = self.driver.window_handles[0]
        # Wait to make sure the second window has opened
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)
        # Get the second window
        disclaimer_window = self.driver.window_handles[1]
        # Switch the browser to display the new window
        self.driver.switch_to_window(disclaimer_window)
        # Get the windows title, wait to make sure it has loaded first
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")
        disclaimer_title = self.driver.title
        # Switch back to the main window
        self.driver.switch_to_window(main_window)
        # Return a true/false that the title is the same as the new windows title
        return title in disclaimer_title

    def click_coordinate_toggle_button(self):
        '''Clicks the Coordinate toggle button'''
        element = self.driver.find_element(*FooterLocators.COORD_TOGGLE)
        element.click()

    def click_contact_us_link(self):
        '''Clicks the Contact Us link'''
        element = self.driver.find_element(*FooterLocators.CONTACT_US_LINK)
        element.click()

    def click_take_tour_link(self):
        '''Clicks the Take Tour link'''
        element = self.driver.find_element(*FooterLocators.TAKE_TOUR_LINK)
        element.click()

    def click_disclaimer_link(self):
        '''Clicks the Disclaimer link'''
        element = self.driver.find_element(*FooterLocators.DISCLAIMER_LINK)
        element.click()

    def click_copyright_link(self):
        '''Clicks the Copyright link'''
        element = self.driver.find_element(*FooterLocators.COPYRIGHT_LINK)
        element.click()
