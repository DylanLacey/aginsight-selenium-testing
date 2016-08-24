from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

HeaderLocators = Locators.HeaderLocators()
SplashPageLocators = Locators.SplashPageLocators()

class Header(object):
    '''The Header class contains all methods for interacting with the header.'''
    def __init__(self, driver):
        self.driver = driver

    def dismiss_splash_page(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dialog-shadow'))
        )

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

    def location_search(self, address):
        '''This method will send the input address into the location search'''
        # Get the input address element
        element = self.driver.find_element_by_id('header-search')
        # Get the input form elment
        inputElement = element.find_element_by_tag_name('input')
        # Send the text into the input form
        inputElement.send_keys(address)

    def verify_location_search_suggestions(self):
        '''Verifies that the geocoder is showing suggestions'''
        # Get the suggestions element
        # Need to wait until the new element has displayed.
        # Timeout after 3 seconds
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.search-suggestions'))
        )
        # Get the list of suggestions
        suggestions = element.find_elements(By.TAG_NAME, 'li')
        return len(suggestions)

    def click_gov_of_sa_image(self):
        '''Clicks the Government of SA Image link button'''
        element = self.driver.find_element(*HeaderLocators.GOV_OF_SA_LINK)
        element.click()

    def click_south_australia_image(self):
        '''Clicks the South Australia image link'''
        element = self.driver.find_element(*HeaderLocators.SA_LINK)
        element.click()

    def click_food_wine_image(self):
        '''Clicks the Food and Wine image link'''
        element = self.driver.find_element(*HeaderLocators.FOOD_WINE_LINK)
        element.click()
