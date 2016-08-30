#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class SplashPageLocators(object):
    '''A class for splash page locators.'''
    EXPLORE_BUTTON = (By.CSS_SELECTOR, '.explore')
    TOUR_BUTTON = (By.CSS_SELECTOR, '.tour')
    EN_BUTTON = (By.CSS_SELECTOR, 'li.lang-en')
    ZH_BUTTON = (By.CSS_SELECTOR, 'li.lang-zh')

class TourLocators(object):
    ''' A class for tour locators.'''
    NEXT_BUTTON = (By.LINK_TEXT, 'Next')
    CLOSE_BUTTON = (By.LINK_TEXT, 'Close')

class FooterLocators(object):
    '''A class for footer locators.'''
    COORD_TOGGLE = (By.CSS_SELECTOR, '.slide-toggle')
    CONTACT_US_LINK = (By.LINK_TEXT, 'CONTACT US')
    TAKE_TOUR_LINK = (By.LINK_TEXT, 'TAKE TOUR')
    DISCLAIMER_LINK = (By.LINK_TEXT, 'DISCLAIMER')
    COPYRIGHT_LINK = (By.LINK_TEXT, '©COPYRIGHT')

class HeaderLocators(object):
    '''A class for header locators.'''
    GOV_OF_SA_LINK = (By.CSS_SELECTOR, "a[href*='www.sa.gov.au']")
    SA_LINK = (By.CSS_SELECTOR, "a[href*='www.southaustralia.com']")
    FOOD_WINE_LINK = (By.CSS_SELECTOR, "a[href*='www.foodwine.sa.gov.au']")

class HighlightsLocators(object):
    '''A class for highlights locators.'''
    OPEN_HIGHLIGHTS = (By.CSS_SELECTOR, "a[href*='openHightlight']") # TODO: Remove spelling error 'hightlight' in codebase
    DAIRY_TAB = (By.CSS_SELECTOR, "a[href*='#dairy']")
    HORTICULTURE_TAB = (By.CSS_SELECTOR, "a[href*='#horticulture']")
    LIVESTOCK_TAB = (By.CSS_SELECTOR, "a[href*='#livestock']")
    SEAFOOD_TAB = (By.CSS_SELECTOR, "a[href*='#seafood']")
    WINE_TAB = (By.CSS_SELECTOR, "a[href*='#wine']")
    CLOSE_CROSS = (By.CLASS_NAME, 'close')
    NEWS_LINK = (By.LINK_TEXT, 'READ MORE')

class LeftPanelLocators(object):
    '''A class for left UI panel locators.'''
    LEVEL_TWO_CROSS = (By.CLASS_NAME, 'close')
    HELP_BUTTON = (By.LINK_TEXT, '?')

class RightPanelLocators(object):
    '''A class for the right UI panel locators.'''
    CROSS_BUTTON = (By.XPATH, "//div[contains(@class, 'tool open')]/a")
    RESET_CROSS_BUTTON = (By.XPATH, "//div[@id='reset-dialog'][contains(@class, 'dialog open')]/a/span")
    COLLAPSE_BUTTON = (By.XPATH, "//div[@id='layers']/div/div/div/ul/li/div/span[contains(@class, 'collapse')]")
    ADD_BOOKMARK = (By.CSS_SELECTOR, "a[href*='#addbookmark']")
    SAVE_BOOKMARK = (By.XPATH, "//div[@id='bookmarks-dialog']/div/form/div[2]/button")
    RESET_BUTTON = (By.CSS_SELECTOR, "a[href*='reset']")

class CommodityDrawerLocators(object):
    '''A class for commodity drawer locators.'''
    OVERVIEW_BUTTON = (By.XPATH, "//div[@id='overview']/ul/li/span")
    VERTICAL_DRAG = (By.CLASS_NAME, 'ap-drag-vertical')
    INDUSTRY_PROFILE = (By.XPATH, "//div[contains(@class, 'executive-summary')]/a")
    MORE_INFORMATION = (By.XPATH, "//div[contains(@class, 'executive-summary')]/a[2]")
