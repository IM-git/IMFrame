from elements import Elements

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

    def __init__(self, browser: object = None, url: str = None):

        self.browser = ChecksBrowserSettings.checks_the_use_of_singleton(
            browser)
        self.url = url
        self.elements = Elements()
        self.mouse_actions = None
        self.keyboard_actions = None
        self.standard_actions = None

    def check_url(self) -> None:
        """Compares that specified url with the actual url."""
        Logger().info(f"Checks that specified url is: {self.url}.")
        assert self.url == self.get_url(), GlobalErrorMessages.WRONG_PAGE

    def get_url(self) -> str:
        """Use for get current url."""
        return self.browser.current_url

    def open_page(self) -> None:
        """Open a webpage.
        Need to enter the url of the webpage.
        Using string argument."""
        Logger().info(f"Open page: {self.url}.")
        self.browser.get(self.url)
