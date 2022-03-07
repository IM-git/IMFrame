from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from elements import BaseElement
from elements import Elements
from elements import MouseKeyboardActions
from src import Base
from tools import Logger
from tools import AllureScreenshot


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_element = BaseElement()
        self.elements = Elements()
        self.base = Base()
        self.mouse_keyboard_actions = MouseKeyboardActions()

    def open_page(self, link):
        Logger().info(f"Open page: {link}.")
        self.browser.get(link)

    def get_url(self, browser):
        return browser.current_url

    def get_text(self, browser, locator, element):
        Logger().info(f"Get text from element: {element}.")
        return self.elements.get_text(browser, locator, element)

    def wait_element_to_be_clickable(self, browser, locator, element, time=10):
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = self.base_element.find_element(browser, locator, element)
        return WebDriverWait(browser, time).until(
            EC.element_to_be_clickable(value))

    def check_is_displayed(self, browser, locator, element):
        Logger().info(f"Check is displayed element: {element}.")
        browser.implicitly_wait(self.base.TIME)
        try:
            self.base_element.find_element(browser, locator, element).\
                is_displayed()
        except NoSuchElementException:
            return False
        return True

    def click_element(self, browser, locator, element):
        Logger().info(f"Click element: {element}.")
        return self.elements.click(browser, locator, element)

    def enter_value(self, browser, locator, element, name):
        Logger().info(f"Enter value(Element: {element}, name: {name}).")
        value = self.base_element.find_element(
            browser, locator, element)
        click = self.elements.click(browser, locator, element)
        self.mouse_keyboard_actions._enter_text(browser, name)
