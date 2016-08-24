from .base_test_splash import *

@on_platforms(browsers)
class TestSplashPage(BaseTestSplash):
    '''These tests will test the splash page behaves as expected'''

    @classmethod
    def setup_class(self):
        BaseTestSplash.setup_class()

    def test_splash_page_opened(self):
        #self.driver.get("http://www.aginsight.sa.gov.au")
        # Check the splash page is displayed
        assert self.splash.page_is_displayed(), 'Splash Page not displayed'
        # Checks the title is correct
        assert self.splash.title_is_correct('Welcome to AgInsight South Australia'), 'Incorrect title in Splash Page'

    def test_explore_map_button(self):
        #self.driver.get("http://www.aginsight.sa.gov.au")
        # Click the Explore Map & Data button
        self.splash.click_Explore_Map_button()
        # Confirm that the splash screen has now disappeared
        # The welcome element will have class='dialog', instead of 'dialog open'
        assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'

    def test_take_tour_button(self):
        #self.driver.get("http://www.aginsight.sa.gov.au")
        # Click the Take The Tour button
        self.splash.click_Tour_button()
        # Confirm that the splash screen is closed and the tour has started
        assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'
        assert self.splash.tour_screen_is_open(), 'The tour has not started'

    def test_zh_language(self):
        #self.driver.get("http://www.aginsight.sa.gov.au")
        # Click the ZH button
        self.splash.click_ZH_button()
        # Check the title is now in Chinese
        # Somehow we need to confirm that Chinese text is appearing!!
        assert self.splash.title_is_correct('AgInsight South Australia'), 'Incorrect title for Chinese'

if __name__ == "__main__":
    unittest.main()
