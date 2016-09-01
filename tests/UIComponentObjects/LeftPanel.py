from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tests.LocatorObjects import Locators

LeftPanelLocators = Locators.LeftPanelLocators()
SplashPageLocators = Locators.SplashPageLocators()

class LeftPanel(object):
    '''The LeftPanel class contains all methods for interacting with the left UI panel.'''
    def __init__(self, driver):
        self.driver = driver

    def dismiss_splash_page(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dialog-shadow'))
        )

    def verify_no_commodities_are_opened(self):
        '''Verifies that no commodity panels are currently opened.'''
        # Get the menu element
        element = self.driver.find_element_by_id('menu')
        isOpen = True

        try:
            levelTwo = WebDriverWait(self.driver, 3).until (
                EC.presence_of_element_located((By.CSS_SELECTOR, '.level-two.open'))
            )
        except:
            # The WebDriverWait timed out, therefore, no commodity panels are open
            isOpen = False
        return isOpen

    def commodity_panel_is_open(self, commodityToFind):
        '''Verifies that the specified commodity panel is open.'''
        # Get the level-two panel element
        element = self.driver.find_element_by_id('menu')
        levelTwo = WebDriverWait(self.driver, 3).until (
            EC.presence_of_element_located((By.CSS_SELECTOR, '.level-two.open'))
        )

        # Get the title of the opened commodity
        title = levelTwo.find_element(By.CLASS_NAME, 'title')
        return commodityToFind in title.get_attribute('innerHTML')

    def layer_list_for_sector_is_open(self, sectorToFind):
        '''Verifies that the specified layer list for a given sector is open.'''
        # Get the level-three panel element
        element = self.driver.find_element_by_id('menu')
        levelThree = element.find_element(By.CSS_SELECTOR, '.level-three.open')

        # Get the data-parent name, to verify it is the correct sector
        return sectorToFind in levelThree.get_attribute('data-parent')

    def verify_layers_exist_within_sector_list(self, layerList):
        '''Will verify that all layers in the input layerList are showing in the
        current sectors layer list.'''
        # Get the level-three panel element
        element = self.driver.find_element_by_id('menu')
        levelThree = element.find_element(By.CSS_SELECTOR, '.level-three.open')

        # Get the list of layers
        layers = levelThree.find_elements(By.TAG_NAME, 'li')

        listIsValid = True
        for lyr in layers:
            aElement = lyr.find_element(By.TAG_NAME, 'a')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] not in layerList:
                print aElement.get_attribute('innerHTML').split('</span>')[-1]
                listIsValid = False
                break
        return listIsValid

    def verify_layers_exist_within_level_four_menu(self, layerList):
        '''Will verify that the layers in layerList exist within the fourth level
        menu. E.g. the Map Data > Transport > Roads > <List> menu.'''
        # Get the level-four panel element
        element = self.driver.find_element_by_id('menu')
        levelFour = element.find_element(By.CSS_SELECTOR, '.level-four.open')

        # Get the list of layers
        layers = levelFour.find_elements(By.TAG_NAME, 'li')

        listIsValid = True
        for lyr in layers:
            aElement = lyr.find_element(By.TAG_NAME, 'a')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] not in layerList:
                print aElement.get_attribute('innerHTML').split('</span>')[-1]
                listIsValid = False
                break
        return listIsValid

    def verify_regions_exist(self, regionsList):
        '''Verifies that the regions in the regionsList are showing in the menu.'''
        # Get the level-four panel element
        element = self.driver.find_element_by_id('menu')

        # Get the open level-two menu
        levelTwo = element.find_element(By.CSS_SELECTOR, '.level-two.open')

        # Get the regions
        regions = levelTwo.find_elements(By.TAG_NAME, 'li')

        listIsValid = True
        for region in regions:
            aElement = region.find_element(By.TAG_NAME, 'a')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] not in regionsList:
                print aElement.get_attribute('innerHTML').split('</span>')[-1]
                listIsValid = False
                break
        return listIsValid


    def click_level_one_menu_item(self, commodityToFind):
        '''Clicks on the specified commodity item.'''
        # Get the menu element
        element = self.driver.find_element_by_id('menu')

        # Get the level-one DIV
        levelOne = element.find_element(By.CLASS_NAME, 'level-one')

        # Get the level-one menu-items
        menuItems = levelOne.find_elements(By.CSS_SELECTOR, '.menu-item')

        # Iterate through the menu-items until we find the commodity of interest
        for commodity in menuItems:
            if commodity.get_attribute('data-menu') == commodityToFind:
                # Click the commodity open
                commodity.click()
                break

    def click_level_two_menu_item(self, sectorToFind):
        '''Clicks on the specified sector item within the opened commodity.'''
        # Get the menu element
        element = self.driver.find_element_by_id('menu')

        # Wait until at least one of the a-elements is clickable in the opened menu
        WebDriverWait(self.driver, 5).until (
            EC.element_to_be_clickable((By.XPATH, "//nav[@id='menu']/div[contains(@class,'level-two open')]/div[2]/ul/div/div/li/a"))
        )

        # Get the opened commodity
        openedCommodity = element.find_element(By.CSS_SELECTOR, '.level-two.open')

        # Get the list of sector items
        sectorItems = openedCommodity.find_elements(By.TAG_NAME, 'li')

        # Iterate through the sector items until we find the sector of interest
        for sector in sectorItems:
            aElement = sector.find_element(By.TAG_NAME, 'a')
            # We need to click on the span element, otherwise it will sometimes click the
            # level-one menu, which fails
            span = aElement.find_element(By.TAG_NAME, 'span')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] == sectorToFind:
                # Click the sector open
                span.click()
                break

    def click_level_three_menu_item(self, layerType):
        # Get the menu element
        element = self.driver.find_element_by_id('menu')

        # Wait until at least one of the a-elements is clickable in the opened menu
        WebDriverWait(self.driver, 5).until (
            EC.element_to_be_clickable((By.XPATH, "//nav[@id='menu']/div[contains(@class,'level-three parent-open open')]/ul/div/div/li/a"))
        )

        # Get the opened Sector
        openedSector = element.find_element(By.CSS_SELECTOR, '.level-three.open')

        # Get the sector layer items
        sectorLayers = openedSector.find_elements(By.TAG_NAME, 'li')

        # Iterate through the sector layer items until we find the layer of interest
        for lyr in sectorLayers:
            aElement = lyr.find_element(By.TAG_NAME, 'a')
            # We need to click on the span element, otherwise it will sometimes click the
            # level-one menu, which fails
            span = aElement.find_element(By.TAG_NAME, 'span')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] == layerType:
                # Click the sector open
                span.click()
                break

    def click_level_three_layer_item(self, layerName):
        '''Clicks on a specific layer in the opened sector.'''
        # Get the level-three panel element
        element = self.driver.find_element_by_id('menu')
        levelThree = element.find_element(By.CSS_SELECTOR, '.level-three.open')

        # Get the list of layers
        layers = levelThree.find_elements(By.TAG_NAME, 'li')

        # Wait until at least one of the a-elements is clickable in the opened menu
        WebDriverWait(self.driver, 5).until (
            EC.element_to_be_clickable((By.XPATH, "//nav[@id='menu']/div[contains(@class,'level-three parent-open open')]/div/ul/div/div/li/a"))
        )

        for layer in layers:
            aElement = layer.find_element(By.TAG_NAME, 'a')
            if aElement.get_attribute('innerHTML').split('</span>')[-1] == layerName:
                aElement.click()
                break

    def click_level_two_cross_close(self):
        '''Verifies that the cross will close which ever commodity panel is opened.'''
        # Get the menu element
        element = self.driver.find_element_by_id('menu')

        # Get the opened div
        openedCommodity = element.find_element(By.CSS_SELECTOR, '.level-two.open')

        # Get the close button for the opened div
        closeButton = openedCommodity.find_element(*LeftPanelLocators.LEVEL_TWO_CROSS)
        closeButton.click()

    def click_help_button(self):
        '''Clicks the help button to start the tour.'''
        # Get the element and click it
        helpButton = self.driver.find_element(*LeftPanelLocators.HELP_BUTTON)
        helpButton.click()
