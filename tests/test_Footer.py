from .base_test import *

@on_platforms(browsers)
class TestFooter(BaseTest):
    '''These tests will test the functionality of the Footer component'''

    # TODO: Need a way to test the Contact Us opens an email? No way to achieve
    # this with Selenium.

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    def test_change_coord_sys(self):
        # Get the current coordinate system
        coordSys = self.footer.get_current_coord_sys()

        # Click the coordinate toggle button
        self.footer.click_coordinate_toggle_button()

        # Verify the coordinate system has changed, by passing in the old coordSys
        assert self.footer.verify_coord_sys(coordSys) == False, 'Coordinate System did not change'

    def test_take_tour_link(self):
        # Click the TAKE TOUR link
        self.footer.click_take_tour_link()

        # Verify the tour has opened
        assert self.splash.tour_screen_is_open(), 'Tour screen did not open correctly'

    def test_disclaimer_link(self):
        # Click the DISCLAIMER link
        self.footer.click_disclaimer_link()

        # A new window should open, with the disclaimer, we will try to switch
        # the driver to the new window and test the title
        assert self.footer.new_window_is_open('Disclaimer - PIRSA'), 'Disclaimer page is not correct'

    def test_copyright_link(self):
        # Click the COPYRIGHT link
        self.footer.click_copyright_link()

        # A new window should open, with the copyright information, we will try to switch
        # the driver to the new window and test the title
        assert self.footer.new_window_is_open('AgInsight SA Copyright - PIRSA'), 'Copyright page is not correct'

if __name__ == "__main__":
    unittest.main()
