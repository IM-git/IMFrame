from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KeyboardActions:
    """
    Here the common keyboard actions.
    """

    def __init__(self, browser):
        self.__browser = browser

    def enter_text(self, text) -> None:
        """Enter text."""
        webdriver.ActionChains(self.__browser).send_keys(text).perform()

    @staticmethod
    def delete_text(element) -> None:
        """Delete text in the element."""
        element.send_keys(Keys.DELETE)

    def click_arrow_up(self) -> None:
        """Click arrow up button."""
        webdriver.ActionChains(self.__browser).send_keys(Keys.ARROW_UP)

    def click_arrow_down(self) -> None:
        """Click arrow down button."""
        webdriver.ActionChains(self.__browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def click_enter(self) -> None:
        """Click 'Enter' button."""
        webdriver.ActionChains(self.__browser).send_keys(Keys.ENTER).perform()

    def click_tab(self) -> None:
        """Click 'TAB' button."""
        webdriver.ActionChains(self.__browser).send_keys(Keys.TAB).perform()

    def do_key_down(self) -> None:
        """Sends a key press only, without releasing it.
           Should only be used with modifier keys
           (Control, Alt and Shift)."""
        webdriver.ActionChains(self.__browser).key_down(Keys.SHIFT)
