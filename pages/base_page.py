from elements import Elements

from src import Base
from src import GlobalErrorMessages

from tools import Logger
from tools import DataSettings
from tools import ChecksBrowserSettings

DATA = DataSettings.config_data()


class BasePage:
    """
    BasePage combines all main commands
    in the common class.
    """

    def __init__(self, browser=None, url=None):

        self.browser = ChecksBrowserSettings.checks_the_use_of_singleton(
            browser)
        self.url = url
        self.mouse_actions = None
        self.keyboard_actions = None
        self.elements = Elements()
        self.base = Base()

    def check_url(self):
        """Compares that specified url with the actual url."""
        assert self.url == self.get_url(), GlobalErrorMessages.WRONG_PAGE

    # def enter_value(self, locator: str, element: str, name) -> None:
    #     """Will be entered value in specified element."""
    #     Logger().info(f"Enter value(Element: {element}, name: {name}).")
    #     self.elements.click(self.browser, locator, element)
    #     self.keyboard_actions._enter_text(name)

    def get_url(self) -> str:
        """Use for get current url."""
        return self.browser.current_url

    def open_page(self) -> None:
        """Open a webpage.
        Need to enter the url of the webpage.
        Using string argument."""
        Logger().info(f"Open page: {self.url}.")
        self.browser.get(self.url)
