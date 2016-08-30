from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.LocatorObjects import Locators

RightPanelLocators = Locators.RightPanelLocators()
SplashPageLocators = Locators.SplashPageLocators()

class RightPanel(object):
    '''The RightPanel class contains all methods for interacting with the right UI panel.'''
    def __init__(self, driver):
        self.driver = driver

    def dismiss_splash_page(self):
        '''Clicks the Explore Map & Data button'''
        element = self.driver.find_element(*SplashPageLocators.EXPLORE_BUTTON)
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.dialog-shadow'))
        )

    def verify_panel_is_open(self, panelName):
        '''Verifies that the panel specified by panelName is currently open.'''
        # Get the tool element
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, panelName))
        )
        # If the tool is currently open, it's class will be 'tool open'
        return element.get_attribute('class') == 'tool open'

    def verify_panel_is_closed(self, panelName):
        '''Verifies that the panel specified by panelName is currently closed.'''
        # Get the tool element
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='" + panelName + "'][contains(@class, 'tool')]"))
        )
        # If the tool is currently closed, it's class will be 'tool'
        return element.get_attribute('class') == 'tool'

    def verify_reset_is_open(self):
        '''Verfies that the Reset tool is currently open.'''
        # Get the tool element
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'reset-dialog'))
        )
        # If the tool is currenlty open, the class will be 'dialog open'
        return element.get_attribute('class') == 'dialog open'

    def verify_reset_is_closed(self):
        '''Verfies that the Reset tool is currently closed.'''
        # Get the tool element
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'reset-dialog'))
        )
        # If the tool is currenlty open, the class will be 'dialog open'
        return element.get_attribute('class') == 'dialog'

    def verify_layer_is_added_to_data_layers(self, inLayer):
        '''Verifies that the layers in the layerList are currently within the data layers panel.'''
        # Get the tool element, but wait for one of the li's to appear, These
        # will only appear once the layer is loaded
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='layers']/div/div/div/ul/li[contains(@data-layer, '" + inLayer + "')]"))
        )

        return element.get_attribute('data-layer') == inLayer

    def verify_data_layers_components_are_showing(self, parentText, titleText):
        '''This will verify that the data layers panel is showing a toggle,
        cross and expand button for the layer added.'''
        # Get the layers element
        element = self.driver.find_element(By.XPATH, "//div[@id='layers']/div/div/div/ul/li")
        meta = element.find_element(By.CLASS_NAME, 'meta')

        # Verify the parent is correct
        parent = meta.find_element(By.CLASS_NAME, 'parent')
        if parent.get_attribute('innerHTML') != parentText:
            return False

        # Verify the title is correct
        title = meta.find_element(By.CLASS_NAME, 'title')
        if title.get_attribute('innerHTML') != titleText:
            return False

        # Verify a visibility toggle is showing
        toggle = meta.find_element(By.CSS_SELECTOR, '.slide-toggle')
        if toggle.is_displayed() == False:
            return False

        # Verify that a cross to remove layer button is showing
        cross = meta.find_element(By.CLASS_NAME, 'remove')
        if cross.is_displayed() == False:
            return False

        # Verify that a collapse button is showing
        collapse = meta.find_element(By.CLASS_NAME, 'collapse')
        if collapse.is_displayed() == False:
            return False

        # If all tests pass, return True
        return True

    def verify_data_layers_collapsable_components_are_showing(self):
        '''Will verify that the collapable components are visible.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='layers']/div/div/div/ul/li/div[contains(@class, 'controls')]"))
        )
        return element.is_displayed()

    def verify_data_layers_collapsable_components_are_not_showing(self):
        '''Will verify that the collapable components are visible.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@id='layers']/div/div/div/ul/li/div[contains(@class, 'controls')]"))
        )
        return element.is_displayed()

    def verify_data_layers_collapse_sliders_are_showing(self, sliderNames):
        '''Will verify that the input slider names are currently showing in the
        collapse element for the first layer found.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='layers']/div/div/div/ul/li/div[contains(@class, 'controls')]"))
        )

        # Get the individual controls
        controls = element.find_elements(By.CLASS_NAME, 'control')
        allControlsValid = True
        currentControls = []
        for control in controls:
            label = control.find_element(By.TAG_NAME, 'label')
            currentControls.append(label.get_attribute('innerHTML'))
        for name in sliderNames:
            if name not in currentControls:
                allControlsValid = True
                break
        return allControlsValid

    def verify_counter_count(self, number):
        '''Will check that the small red layer counter is displaying
        the correct number of layers, specified by the input number.'''
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(@class, 'layers')]/div[contains(@class, 'count')]"))
        )
        return int(element.get_attribute('innerHTML')) == number

    def verify_counter_count_is_zero(self):
        '''Will check that the small red layer counter not displaying
        and the number is zero'''
        element = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//li[contains(@class, 'layers')]/div[contains(@class, 'count')]"))
        )
        return int(element.get_attribute('innerHTML')) == 0

    def verify_legend_showing_layers(self, inLayers):
        '''Will verify that the legend is showing the inLayers.'''
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='legend'][contains(@class, 'open')]/div/div/div/div[contains(@class, 'layer')]"))
        )
        # The layers
        layers = self.driver.find_element(By.ID, 'legend').find_elements(By.CSS_SELECTOR, '.layer')
        layerTitles = []
        layersAreValid = True
        for lyr in layers:
            title = lyr.find_element(By.CSS_SELECTOR, '.title').get_attribute('innerHTML')
            layerTitles.append(title)
        for lyr in inLayers:
            if lyr not in layerTitles:
                layersAreValid = False
                break
        return layersAreValid

    def verify_select_focus_components_are_visible(self):
        '''Will test that all the select focus compoents are visible.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='identify'][contains(@class, 'open')]"))
        )

        # Get the identify controls
        controls = element.find_element(By.CSS_SELECTOR, '.identify-control').find_elements(By.TAG_NAME, 'a')

        # The Point identify tool should be first
        if controls[0].get_attribute('title') != 'Point':
            return False

        # The Polygon tool is second
        if controls[1].get_attribute('title') != 'Polygon':
            return False

        # The clear button is third
        if controls[2].get_attribute('title') != 'clear':
            return False

        # If all tests passed, return true
        return True

    def verify_bookmark_in_bookmarks(self, bookmarkName):
        '''Will verify that the bookmarkName exists in the bookmark panel.'''
        # element = WebDriverWait(self.driver, 5).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[@id='bookmarks'][contains(@class, 'open')]"))
        # )

        bookmark = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bookmarks'][contains(@class, 'open')]/div/div/div/ul/li[2]"))
        )
        return bookmark.get_attribute('data-bookmark') == bookmarkName

    def insert_bookmark_name(self, text):
        '''Will insert the text into the bookmark name.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='bookmarks-dialog'][contains(@class, 'open')]/div/form/div/input"))
        )
        #textInput = element.find_element(By.TAG_NAME, 'input')
        element.send_keys(text)
        element.click()
        #element.send_keys(Keys.ENTER)
        #self.click_save_bookmark()

    def verify_basemaps_are_showing(self, basemapList):
        '''Verifies that all basemaps are showing.'''
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='basemap'][contains(@class, 'open')]"))
        )

        basemaps = element.find_elements(By.TAG_NAME, 'li')

        currentBasemaps = []
        for basemap in basemaps:
            currentBasemaps.append(basemap.get_attribute('data-name'))
        basemapsAreVaild = True
        for basemap in basemapList:
            if basemap not in currentBasemaps:
                basemapsAreVaild = False
        return basemapsAreVaild

    def click_panel_button(self, panelName):
        '''Clicks open the panel, specified by the panelName.'''
        # Get the tools
        tools = self.driver.find_element(By.ID, 'tools')
        # Get the panel DIV with href element
        panel = tools.find_element(By.CSS_SELECTOR, "div[href*='#tools-" + panelName + "']")
        span = panel.find_element(By.TAG_NAME, 'span')
        span.click()

    def click_panel_cross_button(self):
        '''Clicks the cross button for the currently opened panel.'''
        cross = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((RightPanelLocators.CROSS_BUTTON))
        )
        cross.click()

    def click_reset_cross_button(self):
        '''Clicks the close cross button on the reset dialog.'''
        cross = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((RightPanelLocators.RESET_CROSS_BUTTON))
        )
        cross.click()

    def click_collapse_button_on_first_layer(self):
        '''Finds the first layer and clicks on the collapse button.'''
        collapse = self.driver.find_element(*RightPanelLocators.COLLAPSE_BUTTON)
        collapse.click()

    def click_add_bookmark(self):
        '''Will click the Add Bookmark button in the Bookmarks panel.'''
        # Wait until the bookmarks are open
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((RightPanelLocators.ADD_BOOKMARK))
        )
        button = self.driver.find_element(*RightPanelLocators.ADD_BOOKMARK)
        button.click()

    def click_save_bookmark(self):
        '''Clicks the save bookmark button in the bookmark-dialog.'''
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(RightPanelLocators.SAVE_BOOKMARK)
        )
        button.click()

    def click_reset_map(self):
        '''Clicks the reset button in the reset dialog.'''
        button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(RightPanelLocators.RESET_BUTTON)
        )
        button.click()
