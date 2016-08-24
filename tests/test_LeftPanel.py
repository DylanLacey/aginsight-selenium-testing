from .base_test import *

@on_platforms(browsers)
class TestLeftPanel(BaseTest):
    '''These tests will test the functionality of the left UI panel component'''

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()

    # def test_all_commodity_panels_open_and_close_using_cross(self):
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

    def test_field_crops_layers_panel(self):
        sectors = {
            'Barley': ['Barley Production by Year', 'Land Potential for Barley', 'Get more data'],
            'Beans': ['Beans Production by Year', 'Land Potential for Faba Beans', 'Get more data'],
            'Canola': ['Canola Production by Year', 'Land Potential for Canola', 'Get more data'],
            'Chick Peas': ['Chick Peas Production by Year', 'Land Potential for Chickpeas', 'Get more data'],
            'Lentils': ['Land Potential for Lentils', 'Lentils Production by Year', 'Get more data'],
            'Lupins': ['Land Potential for Lupins', 'Lupins Production by Year', 'Get more data'],
            'Oats': ['Land Potential for Oats', 'Oats Production by Year', 'Get more data'],
            'Peas': ['Land Potential for Field Peas', 'Peas Production by Year', 'Get more data'],
            'Ryecorn': ['Land Potential for Dryland Perennial Rye Grass', 'Land Potential for Irrigated Rye Grass', 'Land Potential for Perennial Rye Grass (High-Value)', 'Rye Production by Year', 'Get more data'],
            'Wheat': ['Wheat Regions', 'Durum Production by Year', 'Grain Storage', 'Land Potential for Wheat', 'Wheat Production by Year', 'Get more data']
        }

        # Open the Field Crops commodity
        self.leftpanel.click_level_one_menu_item('Field Crops')

        # Iterate through the sectors
        for sector in sectors.keys():
            # Open the sector
            self.leftpanel.click_level_two_menu_item(sector)

            # Verify all the layer names are in the layer list
            assert self.leftpanel.verify_layers_exist_within_sector_list(sectors[sector]), 'Not all layers are present in the ' + sector + ' sector layer list'


if __name__ == "__main__":
    unittest.main()
