from selenium import webdriver


class MouseActions:
    """Here the common mouse actions."""

    def __init__(self, browser):
        self.browser = browser

    def _move_to_element(self, element):
        """Moving the mouse to the middle of an element."""
        return webdriver.ActionChains(self.browser).\
            move_to_element(element).perform()

    def _one_click(self, element):
        """One a click on the element."""
        return webdriver.ActionChains(self.browser). \
            click(element).perform()

    def _double_click(self, element):
        """Double the click on the element."""
        return webdriver.ActionChains(self.browser). \
            double_click(element).perform()

    def _right_click(self, element):
        """Right a click on the element."""
        return webdriver.ActionChains(self.browser). \
            context_click(element).perform()

    def _select_all_text(self, element):
        """Doing double clicks for select all text."""
        return webdriver.ActionChains(self.browser).\
            double_click(element).click().perform()
