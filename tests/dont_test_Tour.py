import time
from .base_test import *

@on_platforms(browsers)
class TestTour(BaseTest):
    '''These tests will test the tour behaves as expected'''

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    def test_tour(self):
        # self.driver.get('http://www.aginsight.sa.gov.au')

        # Click the Take The Tour button
        self.splash.click_Tour_button()

        # Confirm that the splash screen is closed and the tour has started
        assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'
        assert self.splash.tour_screen_is_open(), 'The tour has not started'

        # Verify the tour is displaying the correct first step
        assert self.tour.step_title_is_correct('help-step-1', 'AgInsight Wizard'), 'The first step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-2', 'South Australia highlights'), 'The second step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-3', 'Commodity sectors'), 'The third step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-5', 'Manipulate data layers'), 'The fifth step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-6', 'Tools'), 'The sixth step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-7', 'Explore even more data'), 'The seventh step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-8', 'Regional information'), 'The eighth step is incorrect'

        # Click the next button
        self.tour.click_next_button()
        # Verify the second step is displaying
        assert self.tour.step_title_is_correct('help-step-9', 'Find a location'), 'The ninth step is incorrect'

        # Click the close button
        self.tour.click_close_button()
        # Confirm the tour has closed
        time.sleep(2) # Explicitly wait 2 seconds, to ensure the CSS changes have applied
        assert self.splash.tour_screen_is_open() == False, 'The tour has not closed'

if __name__ == "__main__":
    unittest.main()
