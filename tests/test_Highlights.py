from .base_test import *

@on_platforms(browsers)
class TestHighlights(BaseTest):
    '''These tests will test the functionality of the Highlights component'''

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

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

    def test_news_article_link(self):
        self.highlights.dismiss_splash_page()

        # Click on the highlights button
        self.highlights.click_highlights_button()
        self.highlights.highlights_is_open()

        # Click on a news link (the first one selenium finds)
        self.highlights.click_news_link()

        assert self.highlights.news_link_tab_is_open(), 'The news link click did not open a new tab'

    # def test_dairy_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights button
    #     self.highlights.click_highlights_button()
    #
    #     # Click on the Dairy tab in the graph
    #     self.highlights.click_dairy_tab_button()
    #
    #     # Verify that the headings are displaying correctly (need to specify unicode string)
    #     assert self.highlights.verify_graph_heading("China's growing dairy demand"), 'Graph not displaying the correct Dairy heading'
    #     assert self.highlights.verify_below_graph_info('Dairy'), 'The info below the graph is not displaying Dairy'
    #
    # def test_horticulture_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
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
    #
    #     # Click on the livestock tab
    #     self.highlights.click_livestock_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading('Global Demand Growth for Animal Protein'), 'Graph not displaying the correct Livestock heading'
    #     assert self.highlights.verify_below_graph_info('Livestock'), 'The info below the graph is not displaying Livestock'
    #
    # def test_seafood_tab(self):
    #     self.highlights.dismiss_splash_page()
    #
    #     # Click on the highlights butotn
    #     self.highlights.click_highlights_button()
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
    #
    #     # Click on the Wine tab
    #     self.highlights.click_wine_tab_button()
    #
    #     # Verify that the headings are displaying correctly
    #     assert self.highlights.verify_graph_heading('Global wine demand by region'), 'Graph not displaying the correct Wine heading'
    #     assert self.highlights.verify_below_graph_info('Wine'), 'The info below the graph is not displaying Wine'

if __name__ == "__main__":
    unittest.main()
