from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KeyboardActions:
    """Here the common keyboard actions."""

    def __init__(self, browser):
        self.browser = browser

    def _enter_text(self, text):
        """Enter text."""
        return webdriver.ActionChains(self.browser).send_keys(text).perform()

    def _delete_text(self, element):
        """Delete text in the element."""
        return element.send_keys(Keys.DELETE)

    def _click_arrow_up(self):
        """Click arrow up button."""
        return webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_UP)

    def _click_arrow_down(self):
        """Click arrow down button."""
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def _click_enter(self):
        """Click 'Enter' button."""
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.ENTER).perform()

    def _click_tab(self):
        """Click 'TAB' button"""
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.TAB).perform()

    def _do_key_down(self):
        """Sends a key press only, without releasing it.
           Should only be used with modifier keys
           (Control, Alt and Shift)."""
        return webdriver.ActionChains(self.browser).key_down(Keys.SHIFT)

    def _perform(self, value):
        """Performs all stored actions."""
        return value.perform()
