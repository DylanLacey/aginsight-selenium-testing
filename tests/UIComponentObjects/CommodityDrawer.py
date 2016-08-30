from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

CommodityDrawerLocators = Locators.CommodityDrawerLocators()
SplashPageLocators = Locators.SplashPageLocators()

class CommodityDrawer(object):
    '''The CommodityDrawer class contains all methods for interacting with the
    commodity drawers at the bottom of the screen.'''
    def __init__(self, driver):
        self.driver = driver

    def dismiss_splash_page(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dialog-shadow'))
        )

    def overview_button_is_correct(self, commodity):
        # Get the overview button in it's current state
        overviewBtn = self.driver.find_element(*CommodityDrawerLocators.OVERVIEW_BUTTON)

        return overviewBtn.get_attribute('innerHTML') == commodity

    def verify_drawer_is_open(self):
        '''Verifies that the commodity drawer is currently open.'''
        # Get the overview DIV
        overview = self.driver.find_element(By.ID, 'overview')

        # Wait to ensure the panel opens fully
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='overview'][contains(@class, 'panel open')]"))
        )

        # The overview DIV's class will == 'panel open' if currently opened
        return overview.get_attribute('class') == 'panel open'

    def verify_drawer_is_closed(self):
        '''Verifies the commodity drawe is currently closed.'''
        # Get the overview DIV
        overview = self.driver.find_element(By.ID, 'overview')

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='overview'][contains(@class, 'panel')]"))
        )

        # The overview DIV's class will == 'panel' if currently closed
        return overview.get_attribute('class') == 'panel'

    def verify_drawer_title_is(self, inTitle):
        '''Verifies the title in the drawer is the same as the input title.'''
        overview = self.driver.find_element(By.ID, 'overview')

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'executive-summary')]"))
        )

        execSum = overview.find_element(By.CLASS_NAME, 'executive-summary')
        title = execSum.find_element(By.TAG_NAME, 'h1')

        return title.get_attribute('innerHTML') == inTitle

    def new_window_is_open_by_url(self, urlText):
        '''Verifies that a new window with the urlText is open.'''
        # Get the current window and the openend window
        main_window = self.driver.window_handles[0]
        # Wait to make sure the second window has opened
        WebDriverWait(self.driver, 20).until(lambda d: len(d.window_handles) == 2)
        # Get the second window
        disclaimer_window = self.driver.window_handles[1]
        # Switch the browser to display the new window
        self.driver.switch_to_window(disclaimer_window)
        # Get the windows url, wait to make sure it has loaded first
        WebDriverWait(self.driver, 20).until(lambda d: d.current_url != "")
        window_url = self.driver.current_url
        # Close the new window
        self.driver.close()
        # Switch back to the main window
        self.driver.switch_to_window(main_window)
        # Return a true/false that the title is the same as the new windows title
        return urlText in window_url

    def new_window_is_open_by_title(self, inTitle):
        '''Verifies that a new window with the urlText is open.'''
        # Get the current window and the openend window
        main_window = self.driver.window_handles[0]
        # Wait to make sure the second window has opened
        WebDriverWait(self.driver, 20).until(lambda d: len(d.window_handles) == 2)
        # Get the second window
        disclaimer_window = self.driver.window_handles[1]
        # Switch the browser to display the new window
        self.driver.switch_to_window(disclaimer_window)
        # Get the windows url, wait to make sure it has loaded first
        WebDriverWait(self.driver, 20).until(lambda d: d.title != "")
        title = self.driver.title
        # Close the new window
        self.driver.close()
        # Switch back to the main window
        self.driver.switch_to_window(main_window)
        # Return a true/false that the title is the same as the new windows title
        return inTitle in title

    def click_overview_button(self):
        '''Clicks the commodity drawer overview button to open/close.'''
        button = self.driver.find_element(*CommodityDrawerLocators.OVERVIEW_BUTTON)
        button.click()

    def click_vertical_drag(self):
        '''Clicks the vertical drag element to close the drawer.'''
        button = self.driver.find_element(*CommodityDrawerLocators.VERTICAL_DRAG)
        button.click()

    def click_industry_profile_link(self):
        '''Clicks the industry profile link in the current drawer.'''
        button = self.driver.find_element(*CommodityDrawerLocators.INDUSTRY_PROFILE)

        # The element may not be in view, if not scroll into view
        self.driver.execute_script("document.getElementsByClassName('executive-summary')[0].getElementsByTagName('a')[0].scrollIntoView()")
        button.click()

    def click_more_info_link(self):
        '''Clicks on the more information link in the drawer.'''
        button = self.driver.find_element(*CommodityDrawerLocators.MORE_INFORMATION)

        # The element may not be in view, if not scroll into view
        self.driver.execute_script("document.getElementsByClassName('executive-summary')[0].getElementsByTagName('a')[1].scrollIntoView()")

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(CommodityDrawerLocators.MORE_INFORMATION)
        )
        button.click()
