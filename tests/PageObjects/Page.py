from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

SplashPageLocators = Locators.SplashPageLocators()

class BasePage(object):
    '''Base class to initialise the base page that will be called from all pages'''
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    '''The Home Page is techincally the only page in AgInsight, as it
       is a single page application. The Home Page class has methods
       to verify the UI components are displaying, not actually to test
       the UI components themselves.'''

class SplashPage(BasePage):
    '''The Splash Page is essentially the Home Page, but we expect that
       the splash screen will be open at this point.'''

    def page_is_displayed(self):
        '''Verified that the splash page is showing'''
        # Need to wait until the new element has displayed.
        # Timeout after 10 seconds
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'welcome'))
        )
        return element.is_displayed()

    def title_is_correct(self, titleText):
        '''Verifies the correct title text appears in the splash page'''
        # Need to wait until the new element has displayed.
        # Timeout after 10 seconds
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'welcome'))
        )
        h1Element = element.find_element_by_tag_name('h1')
        return titleText in h1Element.get_attribute('innerHTML')

    def welcome_element_class_is(self, className):
        '''Verifies the class which is currently applied to the Welcome element'''
        # Need to wait until the new element has displayed.
        # Timeout after 10 seconds
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'welcome'))
        )
        return className in element.get_attribute('class')

    def tour_screen_is_open(self):
        '''Verifies that the tour is open'''
        # Need to wait until the new element has displayed.
        # Timeout after 10 seconds
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'help'))
        )
        return element.is_displayed()

    def click_Explore_Map_button(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

    def click_Tour_button(self):
        '''Clicks the Take The Tour button'''
        element = self.driver.find_element(*SplashPageLocators.TOUR_BUTTON)
        element.click()

    def click_EN_button(self):
        '''Selects the English language'''
        element = self.driver.find_element(*SplashPageLocators.EN_BUTTON)
        element.click()

    def click_ZH_button(self):
        '''Selects the English language'''
        element = self.driver.find_element(*SplashPageLocators.ZH_BUTTON)
        element.click()
