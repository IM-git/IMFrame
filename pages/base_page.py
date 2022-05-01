from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from elements import BaseElement
from elements import Elements
from elements import MouseActions
from elements import KeyboardActions
from src import Base
from tools import Logger
from tools import AllureScreenshot


class BasePage:
    """BasePage combines all main commands
    in the common class."""

    def __init__(self, browser):
        self.browser = None
        # self.browser = browser
        # self.base_element = None
        self.base_element = BaseElement()
        self.elements = Elements()
        self.base = Base()
        self.mouse_actions = None
        self.keyboard_actions = None
        # self.mouse_actions = MouseActions(browser)
        # self.keyboard_actions = KeyboardActions(browser)

    def __browser(self):
        return

    def _base_element(self):
        """Initialize the class only when necessary."""
        pass

    def _mouse_actions(self):
        """Initialize the class only when necessary."""
        pass

    def keyboard_actions(self):
        """Initialize the class only when necessary."""
        pass

    def open_page(self, url: str) -> None:
        """Open a webpage.
        Need to enter the url of the webpage.
        Using string argument."""
        Logger().info(f"Open page: {url}.")
        self.browser.get(url)

    def get_url(self) -> str:
        """Use for get current url."""
        return self.browser.current_url

    def get_text(self, locator: str, element: str):
        """Use for get element text."""
        Logger().info(f"Get text from element: {element}.")
        return self.elements.get_text(self.browser, locator, element)

    def wait_element_to_be_clickable(self,
                                     locator: str,
                                     element: str,
                                     time: int = 10) -> None:
        """Will wait the element specified amount of time."""
        Logger().info(f"Wait element to be clickable(Element: {element}).")
        value = self.base_element.find_element(self.browser, locator, element)
        WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable(value))

    def check_is_displayed(self, locator: str, element: str) -> bool:
        """Wait specified time or while file will be displayed."""
        Logger().info(f"Check is displayed element: {element}.")
        self.browser.implicitly_wait(self.base.TIME)
        try:
            self.base_element.find_element(self.browser, locator, element).\
                is_displayed()
        except NoSuchElementException:
            return False
        return True

    def click_element(self, locator: str, element: str) -> None:
        """Will be clicked the specified element."""
        Logger().info(f"Click element: {element}.")
        self.elements.click(self.browser, locator, element)

    def enter_value(self,
                    locator: str,
                    element: str,
                    name) -> None:
        """Will be entered value in specified element."""
        Logger().info(f"Enter value(Element: {element}, name: {name}).")
        self.base_element.find_element(
            self.browser, locator, element)
        self.elements.click(self.browser, locator, element)
        self.keyboard_actions._enter_text(name)
