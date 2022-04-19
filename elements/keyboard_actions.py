from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KeyboardActions:
    """Here the common keyboard actions."""

    def __init__(self, browser):
        self._browser = browser

    def _enter_text(self, text) -> None:
        """Enter text."""
        webdriver.ActionChains(self._browser).send_keys(text).perform()

    @staticmethod
    def _delete_text(element) -> None:
        """Delete text in the element."""
        element.send_keys(Keys.DELETE)

    def _click_arrow_up(self) -> None:
        """Click arrow up button."""
        webdriver.ActionChains(self._browser).send_keys(Keys.ARROW_UP)

    def _click_arrow_down(self) -> None:
        """Click arrow down button."""
        webdriver.ActionChains(self._browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def _click_enter(self) -> None:
        """Click 'Enter' button."""
        webdriver.ActionChains(self._browser).send_keys(Keys.ENTER).perform()

    def _click_tab(self) -> None:
        """Click 'TAB' button"""
        webdriver.ActionChains(self._browser).send_keys(Keys.TAB).perform()

    def _do_key_down(self) -> None:
        """Sends a key press only, without releasing it.
           Should only be used with modifier keys
           (Control, Alt and Shift)."""
        webdriver.ActionChains(self._browser).key_down(Keys.SHIFT)

    #   Need to move to a separate file/class(mb, create decorator or delete)
    @staticmethod
    def _perform(value) -> None:
        """Performs all stored actions."""
        value.perform()
