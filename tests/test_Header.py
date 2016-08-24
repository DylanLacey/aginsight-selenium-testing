from .base_test import *

@on_platforms(browsers)
class TestHeader(BaseTest):
    '''These tests will test the functionality of the Header component'''

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    def test_geocoder_results(self):
        '''This test will verify that the geocoder is returning results.
        It does not verify that the map zooms to the correct location.'''
        self.header.dismiss_splash_page()

        # Send a geocoder search to the location search
        self.header.location_search('Adelaide')

        # Verify the geocoder has returned results
        assert self.header.verify_location_search_suggestions() > 0, 'Geocoder did not return any results'

    def test_gov_of_sa_link(self):
        self.header.dismiss_splash_page()
        
        # Click the Gov of SA image link
        self.header.click_gov_of_sa_image()

        # A new window should open, with the sa.gov.au website, we will try to switch
        # the driver to the new window and test the title
        assert self.header.new_window_is_open('sa.gov.au'), 'Govt of SA link page is incorrect'

    def test_south_australia_link(self):
        self.header.dismiss_splash_page()

        # Click the South Aus image link
        self.header.click_south_australia_image()

        # A new window should open, with the southaustralia.com website, we will try to switch
        # the driver to the new window and test the title
        assert self.header.new_window_is_open('Visit South Australia'), 'South Australia link page is not correct'

    def test_food_wine_link(self):
        self.header.dismiss_splash_page()

        # Click the Food Wine image link
        self.header.click_food_wine_image()

        # A new window should open, with the PIRSA website, we will try to switch
        # the driver to the new window and test the title
        assert self.header.new_window_is_open('Premium Food & Wine'), 'Food and Wine link page is not correct'

if __name__ == "__main__":
    unittest.main()
