from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

HighlightsLocators = Locators.HighlightsLocators()
SplashPageLocators = Locators.SplashPageLocators()

class Highlights(object):
    '''The Highlights class contains all methods for interacting with the highlights.'''
    def __init__(self, driver):
        self.driver = driver

    def dismiss_splash_page(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dialog-shadow'))
        )

    def highlights_is_open(self):
        '''Checks if the highlights compoenent is open.'''
        # Need to wait until the new element has displayed.
        # Timeout after 3 seconds
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, 'highlight'))
        )

        return element.is_displayed()

    def verify_left_section(self, heading):
        '''Verfies that the input heading is showing in the left section of the highlights.'''
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, 'highlight'))
        )

        leftSection = element.find_element(By.CSS_SELECTOR, '.section.section-left')
        leftHeading = leftSection.find_element_by_tag_name('h1')
        return heading in leftHeading.get_attribute('innerHTML')

    def verify_right_section(self, heading):
        '''Verfies that the input heading is showing in the right section of the highlights.'''
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, 'highlight'))
        )

        rightSection = element.find_element(By.CSS_SELECTOR, '.section.section-right')
        rightHeading = rightSection.find_element_by_tag_name('h1')
        return heading in rightHeading.get_attribute('innerHTML')

    def get_news_articles(self):
        '''Verifies that the news article section is populated with articles.'''
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, 'highlight'))
        )

        # Get the right section
        rightSection = element.find_element(By.CSS_SELECTOR, '.section.section-right')

        # Return any articles
        return rightSection.find_elements(By.CLASS_NAME, 'article')

    def verify_graph_heading(self, heading):
        '''Verifies that the input heading is displaying above the graph.'''
        # Need to wait until the new element has displayed.
        # Timeout after 3 seconds
        # First get the open tab
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-content.open'))
        )

        # Now get the highcharts-title
        title = element.find_element_by_class_name('highcharts-title')

        # Now get the text element of the title
        text = title.find_element_by_tag_name('tspan')
        print text.get_attribute('innerHTML')
        return heading in text.get_attribute('innerHTML')

    def verify_below_graph_info(self, heading):
        '''Verifies the heading below the graph area.'''
        # Need to wait until the new element has displayed.
        # Timeout after 3 seconds
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-content.open'))
        )

        h3Element = element.find_element_by_tag_name('h3')
        return heading in h3Element.get_attribute('innerHTML')

    def click_highlights_button(self):
        '''Clicks the Highlights button'''
        element = self.driver.find_element(*HighlightsLocators.OPEN_HIGHLIGHTS)
        element.click()

    def click_cross_close_button(self):
        '''Clicks the cross button'''
        # Get the div which contains the cross button, as there are
        # more than one buttons with the class 'close'
        div = self.driver.find_element_by_id('highlight')
        element = div.find_element(*HighlightsLocators.CLOSE_CROSS)
        element.click()

    def news_link_tab_is_open(self):
        '''Verifies that a new PIRSA tab has opened.'''
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
        news_title = self.driver.title
        return 'PIRSA' in news_title

    def click_dairy_tab_button(self):
        '''Clicks the dairy tab button'''
        element = self.driver.find_element(*HighlightsLocators.DAIRY_TAB)
        element.click()

    def click_horticulture_tab_button(self):
        '''Clicks the horticulture tab button'''
        element = self.driver.find_element(*HighlightsLocators.HORTICULTURE_TAB)
        element.click()

    def click_livestock_tab_button(self):
        '''Clicks the livestock tab button'''
        element = self.driver.find_element(*HighlightsLocators.LIVESTOCK_TAB)
        element.click()

    def click_seafood_tab_button(self):
        '''Clicks the seafood tab button'''
        element = self.driver.find_element(*HighlightsLocators.SEAFOOD_TAB)
        element.click()

    def click_wine_tab_button(self):
        '''Clicks the wine tab button'''
        element = self.driver.find_element(*HighlightsLocators.WINE_TAB)
        element.click()

    def click_news_link(self):
        '''Clicks on the first news link (Read More) found.'''
        element = self.driver.find_element(*HighlightsLocators.NEWS_LINK)
        element.click()
