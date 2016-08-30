from .base_test import *
import time

@on_platforms(browsers)
class TestAgInsight(BaseTest):
    '''These tests will test all of AgInsight.'''

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    # '''--- These tests will test the splash page behaves as expected ---'''
    # def test_splash_page_opened(self):
    #     # Check the splash page is displayed
    #     assert self.splash.page_is_displayed(), 'Splash Page not displayed'
    #     # Checks the title is correct
    #     assert self.splash.title_is_correct('Welcome to AgInsight South Australia'), 'Incorrect title in Splash Page'
    #
    # def test_explore_map_button(self):
    #     # Click the Explore Map & Data button
    #     self.splash.click_Explore_Map_button()
    #     # Confirm that the splash screen has now disappeared
    #     # The welcome element will have class='dialog', instead of 'dialog open'
    #     assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'
    #
    # def test_take_tour_button(self):
    #     # Click the Take The Tour button
    #     self.splash.click_Tour_button()
    #     # Confirm that the splash screen is closed and the tour has started
    #     assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'
    #     assert self.splash.tour_screen_is_open(), 'The tour has not started'
    #
    # def test_zh_language(self):
    #     # Click the ZH button
    #     self.splash.click_ZH_button()
    #     # Check the title is now in Chinese
    #     # Somehow we need to confirm that Chinese text is appearing!!
    #     assert self.splash.title_is_correct('AgInsight South Australia'), 'Incorrect title for Chinese'
    #
    # '''--- These tests will test the functionality of the Footer component ---'''
    # # TODO: Need a way to test the Contact Us opens an email? No way to achieve
    # # this with Selenium.
    # def test_change_coord_sys(self):
    #     self.footer.dismiss_splash_page()
    #
    #     # Get the current coordinate system
    #     coordSys = self.footer.get_current_coord_sys()
    #
    #     # Click the coordinate toggle button
    #     self.footer.click_coordinate_toggle_button()
    #
    #     # Verify the coordinate system has changed, by passing in the old coordSys
    #     assert self.footer.verify_coord_sys(coordSys) == False, 'Coordinate System did not change'
    #
    # def test_take_tour_link(self):
    #     self.footer.dismiss_splash_page()
    #
    #     # Click the TAKE TOUR link
    #     self.footer.click_take_tour_link()
    #
    #     # Verify the tour has opened
    #     assert self.splash.tour_screen_is_open(), 'Tour screen did not open correctly'
    #
    # def test_disclaimer_link(self):
    #     self.footer.dismiss_splash_page()
    #
    #     # Click the DISCLAIMER link
    #     self.footer.click_disclaimer_link()
    #
    #     # A new window should open, with the disclaimer, we will try to switch
    #     # the driver to the new window and test the title
    #     assert self.footer.new_window_is_open('Disclaimer - PIRSA'), 'Disclaimer page is not correct'
    #
    # def test_copyright_link(self):
    #     self.footer.dismiss_splash_page()
    #
    #     # Click the COPYRIGHT link
    #     self.footer.click_copyright_link()
    #
    #     # A new window should open, with the copyright information, we will try to switch
    #     # the driver to the new window and test the title
    #     assert self.footer.new_window_is_open('AgInsight SA Copyright - PIRSA'), 'Copyright page is not correct'
    #
    # '''--- These tests will test the functionality of the Header component ---'''
    # def test_geocoder_results(self):
    #     '''This test will verify that the geocoder is returning results.
    #     It does not verify that the map zooms to the correct location.'''
    #     self.header.dismiss_splash_page()
    #
    #     # Send a geocoder search to the location search
    #     self.header.location_search('Adelaide')
    #
    #     # Verify the geocoder has returned results
    #     assert self.header.verify_location_search_suggestions() > 0, 'Geocoder did not return any results'
    #
    # def test_gov_of_sa_link(self):
    #     self.header.dismiss_splash_page()
    #
    #     # Click the Gov of SA image link
    #     self.header.click_gov_of_sa_image()
    #
    #     # A new window should open, with the sa.gov.au website, we will try to switch
    #     # the driver to the new window and test the title
    #     assert self.header.new_window_is_open('sa.gov.au'), 'Govt of SA link page is incorrect'
    #
    # def test_south_australia_link(self):
    #     self.header.dismiss_splash_page()
    #
    #     # Click the South Aus image link
    #     self.header.click_south_australia_image()
    #
    #     # A new window should open, with the southaustralia.com website, we will try to switch
    #     # the driver to the new window and test the title
    #     assert self.header.new_window_is_open('Visit South Australia'), 'South Australia link page is not correct'
    #
    # def test_food_wine_link(self):
    #     self.header.dismiss_splash_page()
    #
    #     # Click the Food Wine image link
    #     self.header.click_food_wine_image()
    #
    #     # A new window should open, with the PIRSA website, we will try to switch
    #     # the driver to the new window and test the title
    #     assert self.header.new_window_is_open('Premium Food & Wine'), 'Food and Wine link page is not correct'
    #
    # '''--- These tests will test the functionality of the Highlights component ---'''
    # def test_highlights_open_and_close(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #
    #     # Verify the highlights component is open
    #     assert self.highlights.highlights_is_open(), 'Highlights compoenent did not open'
    #
    #     # Click on the highlights button again to close()
    #     self.highlights.click_highlights_button()
    #
    #     # Verify the highlights compoent has closed
    #     assert self.highlights.highlights_is_closed(), 'Highlights compoenent did not close'
    #
    # def test_highlights_click_cross_to_close(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #
    #     # Verify the highlights component is open
    #     assert self.highlights.highlights_is_open(), 'Highlights compoenent did not open'
    #
    #     # Click on the cross button to close the highlights window
    #     self.highlights.click_cross_close_button()
    #
    #     # Verify the highlights compoent has closed
    #     assert self.highlights.highlights_is_closed(), 'Highlights compoenent did not close'
    #
    # def test_sections_are_displaying_correctly(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #
    #     assert self.highlights.verify_left_section('OPPORTUNITIES'), 'OPPORTUNITIES is not displaying in the left section'
    #     assert self.highlights.verify_right_section('NEWS'), 'NEWS is not displaying in the right section'
    #
    # def test_news_articles_are_showing(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #
    #     assert len(self.highlights.get_news_articles()) > 0, 'No news articles are showing'
    #
    # def test_news_article_link(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on a news link (the first one selenium finds)
    #     self.highlights.click_news_link()
    #
    #     assert self.highlights.news_link_tab_is_open(), 'The news link click did not open a new tab'
    #
    # def test_dairy_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on the Dairy tab in the graph
    #     self.highlights.click_dairy_tab_button()
    #
    #     # Verify that the headings are displaying correctly (need to specify unicode string)
    #     assert self.highlights.verify_graph_heading(u"China's growing dairy demand"), 'Graph not displaying the correct Dairy heading'
    #     assert self.highlights.verify_below_graph_info('Dairy'), 'The info below the graph is not displaying Dairy'
    #
    # def test_horticulture_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on the Horticulture tab
    #     self.highlights.click_horticulture_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading('Global growth trend in export trade value for horticulture'), 'Graph not displaying the correct Horticulture heading'
    #     assert self.highlights.verify_below_graph_info('Horticulture'), 'The info below the graph is not displaying Horticulture'
    #
    # def test_livestock_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on the livestock tab
    #     self.highlights.click_livestock_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading(u'Global Demand Growth for Animal Protein'), 'Graph not displaying the correct Livestock heading'
    #     assert self.highlights.verify_below_graph_info('Livestock'), 'The info below the graph is not displaying Livestock'
    #
    # def test_seafood_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on the seafood tab
    #     self.highlights.click_seafood_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading('Global growth trend in export trade value for seafood'), 'Graph not displaying the correct Seafood heading'
    #     assert self.highlights.verify_below_graph_info('Seafood'), 'The info below the graph is not displaying Seafood'
    #
    # def test_wine_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
    #     self.highlights.highlights_is_open()
    #
    #     # Click on the Wine tab
    #     self.highlights.click_wine_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading(u'Global wine demand by region'), 'Graph not displaying the correct Wine heading'
    #     assert self.highlights.verify_below_graph_info('Wine'), 'The info below the graph is not displaying Wine'
    #
    # '''--- These tests will test the tour behaves as expected ---'''
    # def test_tour(self):
    #     # Click the Take The Tour button
    #     self.splash.click_Tour_button()
    #
    #     # Confirm that the splash screen is closed and the tour has started
    #     assert self.splash.welcome_element_class_is('dialog'), 'The Welcome screen is still open'
    #     assert self.splash.tour_screen_is_open(), 'The tour has not started'
    #
    #     # Verify the tour is displaying the correct first step
    #     assert self.tour.step_title_is_correct('help-step-1', 'AgInsight Wizard'), 'The first step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-2', 'South Australia highlights'), 'The second step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-3', 'Commodity sectors'), 'The third step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-5', 'Manipulate data layers'), 'The fifth step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-6', 'Tools'), 'The sixth step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-7', 'Explore even more data'), 'The seventh step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-8', 'Regional information'), 'The eighth step is incorrect'
    #
    #     # Click the next button
    #     self.tour.click_next_button()
    #     # Verify the second step is displaying
    #     assert self.tour.step_title_is_correct('help-step-9', 'Find a location'), 'The ninth step is incorrect'
    #
    #     # Click the close button
    #     self.tour.click_close_button()
    #     # Confirm the tour has closed
    #     time.sleep(2) # Explicitly wait 2 seconds, to ensure the CSS changes have applied
    #     assert self.splash.tour_screen_is_open() == False, 'The tour has not closed'
    #
    # '''--- These tests will test the functionality of the bottom commodity drawers ---'''
    # # TODO: Is there a way to test the download XLS/PDF links in the drawer?
    # def test_overview_tab_changes_to_commodity_name(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     commodities = ['Dairy', 'Field Crops', 'Forestry', 'Horticulture', 'Livestock', 'Seafood', 'Wine']
    #
    #     for com in commodities:
    #         # Click on the commodity to change the overview button
    #         self.leftpanel.click_level_one_menu_item(com)
    #
    #         # Verify the overview button has changed text
    #         assert self.comdrawer.overview_button_is_correct(com), 'The overview button in the commodity drawer is not correct for: ' + com
    #
    # def test_commodity_drawer_opens_and_closes(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     commodities = ['Dairy', 'Field Crops', 'Forestry', 'Horticulture', 'Livestock', 'Seafood', 'Wine']
    #
    #     for com in commodities:
    #         # Click on the commodity to change the commodity drawer
    #         self.leftpanel.click_level_one_menu_item(com)
    #         # We need to wait for the drawer to change commodity
    #         time.sleep(1)
    #         # Click on the overview button to open the drawer
    #         self.comdrawer.click_overview_button()
    #
    #         # Verify the commodity drawer has opened
    #         assert self.comdrawer.verify_drawer_is_open(), 'The commodity drawer for ' + com + ' did not open correctly'
    #         # We need to wait for the tab to fully open
    #         time.sleep(1)
    #         # CLick on the overview button to close the drawer
    #         self.comdrawer.click_overview_button()
    #
    #         # verify the drawer has closed
    #         assert self.comdrawer.verify_drawer_is_closed(), 'The commodity drawer for ' + com + ' did not close correctly'
    #
    # def test_commodity_drawer_closes_with_vertical_drag(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     commodities = ['Dairy', 'Field Crops', 'Forestry', 'Horticulture', 'Livestock', 'Seafood', 'Wine']
    #
    #     for com in commodities:
    #         # Click on the commodity to change the commodity drawer
    #         self.leftpanel.click_level_one_menu_item(com)
    #         # We need to wait for the drawer to change commodity
    #         time.sleep(1)
    #         # Click on the overview button to open the drawer
    #         self.comdrawer.click_overview_button()
    #         time.sleep(1)
    #         # Click on the vertical drag to close
    #         self.comdrawer.click_vertical_drag()
    #
    #         # Verify the drawer is now closed
    #         assert self.comdrawer.verify_drawer_is_closed(), 'The commodity drawer for ' + com + ' did not close correctly using the Vertical Drag'
    #
    # def test_dairy_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Dairy Sector'), 'Dairy drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('Dairy-Opportunities-in-South-Australia'), 'Dairy Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Dairy More Information link did not work correctly'
    #
    # def test_field_crops_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Field Crops')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Field Crops Sector'), 'Field Crops drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('AgriBusiness_Opportunities_in_SA_A4'), 'Field Crops Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Field Crops More Information link did not work correctly'
    #
    # def test_forestry_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Forestry')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Forestry Sector'), 'Forestry drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('Blueprint-Future-South-Australian-Forest-Wood-Products-Industry2014-2040'), 'Forestry Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Forestry More Information link did not work correctly'
    #
    # def test_horticulture_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Horticulture')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Horticulture Sector'), 'Horticulture drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('Horticulture_-_Invest_South_Australia'), 'Horticulture Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Horticulture More Information link did not work correctly'
    #
    # def test_livestock_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Livestock')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Livestock Sector'), 'Livestock drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('PIRSA-Livestock-investment-teaser'), 'Livestock Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Livestock More Information link did not work correctly'
    #
    # def test_seafood_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Seafood')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Seafood Sector'), 'Seafood drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('Seafood_Brochure_Final'), 'Seafood Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Seafood More Information link did not work correctly'
    #
    # def test_wine_drawer_info_is_correct(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     self.leftpanel.click_level_one_menu_item('Wine')
    #
    #     # Open the commodity drawer
    #     self.comdrawer.click_overview_button()
    #
    #     # Check the title is correct
    #     assert self.comdrawer.verify_drawer_title_is('Wine Sector'), 'Wine drawer title is incorrect'
    #     time.sleep(1)
    #     # Click on the Industry Profile link
    #     self.comdrawer.click_industry_profile_link()
    #     # Verify the new windows is open by using part of the URL
    #     assert self.comdrawer.new_window_is_open_by_url('Wine-Opportunities-South-Australia'), 'Wine Industry Profile link did not work correctly'
    #
    #     # Click on the More Information link
    #     self.comdrawer.click_more_info_link()
    #     # Verify the new window is open by using part of the title
    #     assert self.comdrawer.new_window_is_open_by_title('PIRSA'), 'Wine More Information link did not work correctly'
    #
    # '''--- These tests will test the functionality of the left UI panel component ---'''
    # # TODO: Can the commodities, sectors and layers be read from a config file? Potentially the LayerDefs file?
    # def test_all_commodity_panels_open_and_close_using_cross(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     commodities = ['Dairy', 'Field Crops', 'Forestry', 'Horticulture', 'Livestock', 'Seafood', 'Wine']
    #
    #     for commodity in commodities:
    #         # Click open the commodity
    #         self.leftpanel.click_level_one_menu_item(commodity)
    #
    #         # Verify the panel has opened
    #         assert self.leftpanel.commodity_panel_is_open(commodity), commodity + ' commodity panel did not open'
    #
    #         # Close the panel
    #         self.leftpanel.click_level_two_cross_close()
    #
    #         # Verify that it closed
    #         assert self.leftpanel.verify_no_commodities_are_opened() == False, 'There is a commodity panel which is opened and shouldnt be'
    #
    # def test_all_commodity_panels_open_and_close_using_commodity_button(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     commodities = ['Dairy', 'Field Crops', 'Forestry', 'Horticulture', 'Livestock', 'Seafood', 'Wine']
    #
    #     for commodity in commodities:
    #         # Open the commodity panel
    #         self.leftpanel.click_level_one_menu_item(commodity)
    #
    #         # Verify the panel has opened
    #         assert self.leftpanel.commodity_panel_is_open(commodity), commodity + ' commodity panel did not open'
    #
    #         # Now click the commodity panel again to close it
    #         self.leftpanel.click_level_one_menu_item(commodity)
    #
    #         # Verify that it closed
    #         assert self.leftpanel.verify_no_commodities_are_opened() == False, 'There is a commodity panel which is opened and shouldnt be'
    #
    # def test_dairy_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     layerNames = ['Dairy Regions', 'Dairy Farms', 'Dairy Potential', 'Dairy Processors', 'Dairy Production by Year', 'Get more data']
    #
    #     # Open the Dairy commodity
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #
    #     # Open the only Dairy sector
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #
    #     # Verify all of the layer names are in the layer list
    #     assert self.leftpanel.verify_layers_exist_within_sector_list(layerNames), 'Not all layers are present in the Dairy sector layer list'
    #
    # def test_field_crops_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     sectors = {'Barley': ['Barley Production by Year', 'Land Potential for Barley', 'Get more data'],
    #         'Beans': ['Beans Production by Year', 'Land Potential for Faba Beans', 'Get more data'],
    #         'Canola': ['Canola Production by Year', 'Land Potential for Canola', 'Get more data'],
    #         'Chick Peas': ['Chick Peas Production by Year', 'Land Potential for Chickpeas', 'Get more data'],
    #         'Lentils': ['Land Potential for Lentils', 'Lentils Production by Year', 'Get more data'],
    #         'Lupins': ['Land Potential for Lupins', 'Lupins Production by Year', 'Get more data'],
    #         'Oats': ['Land Potential for Oats', 'Oats Production by Year', 'Get more data'],
    #         'Peas': ['Land Potential for Field Peas', 'Peas Production by Year', 'Get more data'],
    #         'Ryecorn': ['Land Potential for Dryland Perennial Rye Grass', 'Land Potential for Irrigated Rye Grass', 'Land Potential for Perennial Rye Grass (High-Value)', 'Rye Production by Year', 'Get more data'],
    #         'Wheat': ['Wheat Regions', 'Durum Production by Year', 'Grain Storage', 'Land Potential for Wheat', 'Wheat Production by Year', 'Get more data']}
    #
    #     # Open the Field Crops commodity
    #     self.leftpanel.click_level_one_menu_item('Field Crops')
    #
    #     # Iterate through the sectors
    #     for sector in sectors.keys():
    #         # Open the sector
    #         self.leftpanel.click_level_two_menu_item(sector)
    #
    #         # Verify all the layer names are in the layer list
    #         assert self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]), 'Not all layers are present in the ' + sector + ' sector layer list'
    #
    # def test_forestry_layers_panel(self):
    #     '''There is nothing to test here, as there are no sub-menus for Forestry.'''
    #     assert 1 == 1
    #
    # def test_horticulture_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     # TODO: this tese will fail until we can work out a way to scroll the screen.
    #     # Some elements are not clickable otherwise!
    #
    #     sectors = {'Almonds': ['Almond Regions', 'Land Potential for Almonds', 'Get more data'],
    #         'Apples': ['Land Potential for Apples', 'Get more data'],
    #         'Carrots': ['Land Potential for Carrots', 'Get more data'],
    #         'Cherries': ['Land Potential for Cherries', 'Get more data'],
    #         'Citrus': ['Land Potential for Citrus', 'Get more data'],
    #         'Olives for Oil': ['Land Potential for Olives', 'Get more data'],
    #         'Onions': ['Land Potential for Onions', 'Get more data'],
    #         'Pears': ['Land Potential for Pears', 'Get more data'],
    #         'Potatoes': ['Land Potential for Potatoes', 'Get more data'],
    #         'Sweet Corn': ['Land Potential for Maize', 'Get more data'],
    #         'Table Olives': ['Land Potential for Olives', 'Get more data']}
    #
    #     # Open the Horticulture commodity
    #     self.leftpanel.click_level_one_menu_item('Horticulture')
    #
    #     failedTests = []
    #
    #     # Iterate through the sectors
    #     for sector in sectors.keys():
    #         # Open the sector
    #         try:
    #             # We will manually maintain failed tests, because we can't scroll the screeen
    #             # as such, we expect some tests to fail, but others to pass
    #             self.leftpanel.click_level_two_menu_item(sector)
    #             if self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]) == False:
    #                 failedTests.append(sector)
    #         except:
    #             failedTests.append(sector)
    #
    #     # Verify all the tests passed, otherwise print out the failed sectors
    #     assert len(failedTests) == 0, 'Not all secotrs passed layer testing. Failed sectors are: ' + ','.join(failedTests)
    #
    # def test_livestock_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     sectors = {'Beef': ['Beef Abattoirs', 'Beef Processors', 'Beef Saleyards', 'Dips and Spelling Yards', 'Feedlot Potential', 'Showgrounds', 'Get more data'],
    #         'Chicken Meat': ['Chicken Meat Regions', 'Chicken Meat Potential', 'Chicken Meat Processors', 'Get more data']}
    #
    #     # Open the Livestock commodity
    #     self.leftpanel.click_level_one_menu_item('Livestock')
    #
    #     # Iterate through the sectors
    #     for sector in sectors.keys():
    #         # Open the sector
    #         self.leftpanel.click_level_two_menu_item(sector)
    #
    #         # Verify all the layer names are in the layer list
    #         assert self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]), 'Not all layers are present in the ' + sector + ' sector layer list'
    #
    # def test_seafood_layers_panel(self):
    #     '''There is nothing to test here, as there are no sub-menus for Seafood.'''
    #     assert 1 == 1
    #
    # def test_wine_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     sectors = {'Wine Grapes': ['Wine Regions', 'Wine Sub-Regions', 'Land Potential for Grape Vines', 'Land Potential for Grape Vines (Mechanically Harvested)', 'Vineyards', 'Wine Zones', 'Get more data']}
    #
    #     # Open the Wine commodity
    #     self.leftpanel.click_level_one_menu_item('Wine')
    #
    #     # Iterate through the sectors
    #     for sector in sectors.keys():
    #         # Open the sector
    #         self.leftpanel.click_level_two_menu_item(sector)
    #
    #         # Verify all the layer names are in the layer list
    #         assert self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]), 'Not all layers are present in the ' + sector + ' sector layer list'
    #
    # def test_map_data_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     sectors = {'Annual Climate Averages': ['Areal Actual Evapotranspiration', 'Areal Potential Evapotranspiration', 'Daily Maximum Temperature', 'Daily Mean Temperature', 'Daily Minimum Temperature', 'Daily Rel. Humidity at 3pm', 'Daily Rel. Humidity at 9am',
    #         'Daily Sunshine Hours', 'Days with Rainfall &gt; 1 mm', 'Noon Clear-Sky UV Index', 'Pan Evaporation', 'Potential Frost Days (Min. Temp. &lt; +2)', 'Potential Frost Days (Min. Temp. &lt; 0)', 'Potential Frost Days (Min. Temp. &lt; -2)', 'Potential Frost Days (Min. Temp. &lt; -5)',
    #         'Rainfall (Apr. to Oct.)', 'Total Rainfall'],
    #         'Electricity': ['Power Stations', 'Power Substations', 'SubTransmission and HV Overhead Lines', 'SubTransmission and HV Underground Lines', 'Transmission Lines'],
    #         'Hydrology': ['Irrigation Areas', 'Irrigation Divisions', 'Prescribed Surface Water Areas', 'Prescribed Water Resource Areas', 'Prescribed Wells Areas', 'River Murray Protection Area', 'Shallow Groundwater Depth', 'Shallow Groundwater Salinity', 'Shallow Groundwater Yield', 'Water Mains'],
    #         'Land Administration': ['Aquaculture Application Leases', 'Aquaculture Application Licences', 'Aquaculture Leases', 'Aquaculture Licences', 'Aquaculture Zones', 'Dog Fence', 'Great Australian Bight Marine Park', 'Land Development Planning Zones', 'Land Development Policy Areas', 'Local Government Areas', 'National Parks and Reserves',
    #         'Port &amp; Harbour Limits', 'Primary Production Priority Areas', 'Properties', 'Property Landuse', 'Regional Development Australia Regions', 'South Australia Marine Park Network', 'Valuation ($ per Hectare)'],
    #         'National Production Statistics': ['Value of Agricultural Production (2012-13)', 'Value of Agricultural Production (2011-12)', 'Value of Agricultural Production (2010-11)', 'Value of Agricultural Production per km2 (2012-13)', 'Value of Agricultural Production per km2 (2011-12)', 'Value of Agricultural Production per km2 (2010-11)'],
    #         'Soil': ['Biophysical Regions', 'Biophysical Subregions', 'Kangaroo Island Land Zones', 'Land Systems', 'Land Types', 'Soil Characterisation Sites', 'Soil Landscapes', 'Chemistry', 'Drainage and Irrigation', 'Erosion', 'Misc. Land Potential', 'Moisture', 'Physical Condition', 'Salinity', 'Soil Type Attributes', 'Surface Attributes'],
    #         'Transport': ['Airports &amp; Airstrips', 'Port Locations', 'Rail', 'Road']}
    #
    #     # Open the Horticulture commodity
    #     self.leftpanel.click_level_one_menu_item('All Data')
    #
    #     failedTests = []
    #
    #     # Iterate through the sectors
    #     for sector in sectors.keys():
    #         # Open the sector
    #         try:
    #             # We will manually maintain failed tests, because we can't scroll the screeen
    #             # as such, we expect some tests to fail, but others to pass
    #             self.leftpanel.click_level_two_menu_item(sector)
    #             if self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]) == False:
    #                 failedTests.append(sector)
    #         except:
    #             failedTests.append(sector)
    #
    #     # Verify all the tests passed, otherwise print out the failed sectors
    #     assert len(failedTests) == 0, 'Not all secotrs passed layer testing. Failed sectors are: ' + ','.join(failedTests)
    #
    # def test_road_layers_panel(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     roadTypes = ['All Other Vehicle Restrictions', 'Approval for Higher Mass Limits (HML)', 'B-Double Restrictions', 'Connector Roads', 'Gazetted B-Double Routes', 'Gazetted Road Train Routes', 'Main Roads', 'Major Highways', 'Minor Roads', 'Road Train Restrictions',
    #         'Structures and Clearances', 'Tracks &amp; Unknown Class']
    #
    #     # Open the Map Data Tab
    #     self.leftpanel.click_level_one_menu_item('All Data')
    #
    #     # Open the Transport level two menu
    #     self.leftpanel.click_level_two_menu_item('Transport')
    #
    #     # Open the Roads level three menu
    #     self.leftpanel.click_level_three_menu_item('Road')
    #
    #     # Verify all the layers are present for Road
    #     assert self.leftpanel.verify_layers_exist_within_level_four_menu(roadTypes), 'Level four menu for Transport > Roads is not showing correct layers'
    #
    # def test_regions_panel_layers(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     regions = ['Adelaide Hills, Fleurieu and Kangaroo Island', 'Barossa, Light and Lower North', 'Far North', 'Limestone Coast', 'Murraylands and Riverland', 'Whyalla and Eyre Peninsula', 'Yorke and Mid North', 'Clear Region']
    #
    #     # Open the Regions Tab
    #     self.leftpanel.click_level_one_menu_item('Regions')
    #
    #     # Verify all the layers are present in the Regions menu
    #     assert self.leftpanel.verify_regions_exist(regions), 'Regions are missing from the Regions panel'
    #
    # def test_help_button_starts_tour(self):
    #     self.leftpanel.dismiss_splash_page()
    #
    #     # Click on the help button
    #     self.leftpanel.click_help_button()
    #
    #     # Verify the tour has started using the SplashPage
    #     assert self.splash.tour_screen_is_open(), 'Tour did not open from help button'
    #
    # '''--- These tests will test the functionality of the right UI panel ---'''
    # def test_all_right_panel_menus_open_and_close(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     panels = ['layers', 'legend', 'identify', 'bookmarks', 'basemap']
    #
    #     for panel in panels:
    #         # Click open the panel
    #         self.rightpanel.click_panel_button(panel)
    #
    #         # Verify the panel has opened
    #         assert self.rightpanel.verify_panel_is_open(panel), 'The panel: ' + panel + ' did not open correctly'
    #
    #         # Click again to close the panel
    #         self.rightpanel.click_panel_button(panel)
    #
    #         # Verify the panel is now closed
    #         assert self.rightpanel.verify_panel_is_closed(panel), 'The panel: ' + panel + ' did not close correctly'
    #
    # def test_all_panels_close_with_cross(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     panels = ['layers', 'legend', 'identify', 'bookmarks', 'basemap']
    #
    #     for panel in panels:
    #         # Click open the panel
    #         self.rightpanel.click_panel_button(panel)
    #         self.rightpanel.verify_panel_is_open(panel)
    #         # Need to explicitly wait here, otherwise we may click
    #         # another element
    #         time.sleep(0.5)
    #         # Click the cross to close the panel
    #         self.rightpanel.click_panel_cross_button()
    #
    #         # Verify the panel is now closed
    #         assert self.rightpanel.verify_panel_is_closed(panel), 'The panel: ' + panel + ' did not close correctly using the cross button'
    #
    # def test_reset_panel_menu_opens_and_closes(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     panel = 'reset'
    #
    #     # Click open the reset panel
    #     self.rightpanel.click_panel_button(panel)
    #
    #     # Verify the panel has opened
    #     assert self.rightpanel.verify_reset_is_open(), 'The panel: ' + panel + ' did not open correctly'
    #
    #     # Click again to close the panel
    #     self.rightpanel.click_panel_button(panel)
    #
    #     # Verify the panel is now closed
    #     assert self.rightpanel.verify_reset_is_closed(), 'The panel: ' + panel + ' did not close correctly'
    #
    # def test_reset_dialog_closes_with_cross(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     panel = 'reset'
    #
    #     # Click open the reset panel
    #     self.rightpanel.click_panel_button(panel)
    #     self.rightpanel.verify_reset_is_open()
    #
    #     # Click the reset dialog cross to close the panel
    #     self.rightpanel.click_reset_cross_button()
    #
    #     # Verify the panel is now closed
    #     assert self.rightpanel.verify_reset_is_closed(), 'The panel: ' + panel + ' did not close correctly using the cross button'
    #
    # def test_data_layers_add_layers(self):
    #     '''Add layers to the map and test that the layers
    #     are added to the Data Layers panel.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Regions')
    #     # Turn on the Dairy Farms layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Farms')
    #
    #     # Open the Data Layers panel
    #     self.rightpanel.click_panel_button('layers')
    #     # Verify that the two layers have been added
    #     assert self.rightpanel.verify_layer_is_added_to_data_layers('DairyFrm'), 'Layers did not add to Data Layers correctly'
    #     assert self.rightpanel.verify_layer_is_added_to_data_layers('DairyReg'), 'Layers did not add to Data Layers correctly'
    #
    # def test_data_layers_components(self):
    #     '''Add a layer to the map and verify that the data layers panel shows the correct components.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Production by Year')
    #     # Open the Data Layers panel
    #     self.rightpanel.click_panel_button('layers')
    #     self.rightpanel.verify_layer_is_added_to_data_layers('DairyProd')
    #
    #     assert self.rightpanel.verify_data_layers_components_are_showing('Dairy', u'Dairy Production by Year'), 'Parts of the Data Layers panel are not showing correctly'
    #
    # def test_data_layers_collapse_button(self):
    #     '''Add a layer to the map and ensure we can expand the collapse button.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Production by Year')
    #     # Open the Data Layers panel
    #     self.rightpanel.click_panel_button('layers')
    #     self.rightpanel.verify_layer_is_added_to_data_layers('DairyProd')
    #     self.rightpanel.click_collapse_button_on_first_layer()
    #     assert self.rightpanel.verify_data_layers_collapsable_components_are_showing(), 'Collapsable components are not showing'
    #
    #     # Click again to close
    #     self.rightpanel.click_collapse_button_on_first_layer()
    #     assert self.rightpanel.verify_data_layers_collapsable_components_are_not_showing() == False, 'Collapsable components are showing when they shouldnt be'
    #
    # def test_data_layers_collapse_shows_year_slider(self):
    #     '''Add a layer to the map and verify that the data layers panel shows the year slider.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Production by Year')
    #     # Open the Data Layers panel
    #     self.rightpanel.click_panel_button('layers')
    #     self.rightpanel.verify_layer_is_added_to_data_layers('DairyProd')
    #     self.rightpanel.click_collapse_button_on_first_layer()
    #
    #     assert self.rightpanel.verify_data_layers_collapse_sliders_are_showing(['Year', 'Opacity']), 'The sliders are not showing within the collapse element'
    #
    # def test_data_layers_collapse_shows_filter_slider(self):
    #     '''Add a layer to the map and verify that the data layers panel shows the filter slider.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Potential')
    #     # Open the Data Layers panel
    #     self.rightpanel.click_panel_button('layers')
    #     self.rightpanel.verify_layer_is_added_to_data_layers('DairyPot')
    #     self.rightpanel.click_collapse_button_on_first_layer()
    #
    #     assert self.rightpanel.verify_data_layers_collapse_sliders_are_showing(['Data', 'Opacity']), 'The sliders are not showing within the collapse element'
    #
    # def test_data_layers_counter(self):
    #     '''Will test the small red circle count symbol, which should show the
    #     number of layers currently in the map.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Regions')
    #     # Turn on the Dairy Farms layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Farms')
    #
    #     # Verify that the counter is now showing 2
    #     assert self.rightpanel.verify_counter_count(2), 'The counter is showing the incorrect number'
    #
    # def test_legend_shows_layers(self):
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Regions')
    #     # Turn on the Dairy Farms layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Farms')
    #     # Open the legend panel
    #     self.rightpanel.click_panel_button('legend')
    #
    #     # Verify the legend is showing the two layers
    #     assert self.rightpanel.verify_legend_showing_layers(['Dairy Regions', 'Dairy Farms']), ' The legend is not showing the correct layer information'
    #
    # def test_select_focus_components_are_showing(self):
    #     '''This will verify that the select focus panel has the correct components.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the identify panel
    #     self.rightpanel.click_panel_button('identify')
    #
    #     # Verify the components are all showing
    #     assert self.rightpanel.verify_select_focus_components_are_visible(), 'The select focus panel is not display all components'

    # def test_add_bookmark(self):
    #     '''This will test that we can add a bookmark. Note, we are not actually
    #     testing the validity of a bookmark - just the workflow to add them.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the bookmarks panel
    #     self.rightpanel.click_panel_button('bookmarks')
    #     # Need to explicitly wait for the panel to open
    #     time.sleep(0.5)
    #     self.rightpanel.click_add_bookmark()
    #     self.rightpanel.insert_bookmark_name('selenium')
    #     time.sleep(0.5)
    #
    #     # TODO: The save button is not working when testing locally.
    #
    #     self.rightpanel.click_save_bookmark()
    #     time.sleep(0.5)
    #     # Veirfy the bookmark is added
    #     assert self.rightpanel.verify_bookmark_in_bookmarks('selenium'), 'The bookmark did not add to the bookmarks panel'

    def test_all_basemaps_are_visible(self):
        '''Toggle the basemaps.'''
        self.comdrawer.dismiss_splash_page()

        # Open the basemaps panel
        self.rightpanel.click_panel_button('basemap')
        time.sleep(2)
        basemaps = ['Imagery', 'Street Map', 'Light Grey', 'Dark Grey', 'Location SA Streetmap', 'Location SA Topographic']
        # Verify the basemaps are all present
        assert self.rightpanel.verify_basemaps_are_showing(basemaps), 'The Basemap gallery is not displaying properly'

    # def test_reset_map(self):
    #     '''Reset the map, first add some layers, then verify they are removed.'''
    #     self.comdrawer.dismiss_splash_page()
    #
    #     # Open the Dairy layers
    #     self.leftpanel.click_level_one_menu_item('Dairy')
    #     self.leftpanel.click_level_two_menu_item('Dairy')
    #     # Turn on the Dairy Regions layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Regions')
    #     # Turn on the Dairy Farms layer
    #     self.leftpanel.click_level_three_layer_item('Dairy Farms')
    #     # Open the reset panel
    #     self.rightpanel.click_panel_button('reset')
    #
    #     # Verify the reset panel opened
    #     self.rightpanel.verify_reset_is_open()
    #     # Reset the map
    #     self.rightpanel.click_reset_map()
    #
    #     # Verify they the layers is now zero
    #     assert self.rightpanel.verify_counter_count_is_zero(), 'The reset function did not work correctly'

if __name__ == "__main__":
    unittest.main()
