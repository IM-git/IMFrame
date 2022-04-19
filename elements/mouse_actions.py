from selenium import webdriver


class MouseActions:
    """Here the common mouse actions."""

    def __init__(self, browser):
        self._browser = browser

    def _move_to_element(self, element) -> None:
        """Moving the mouse to the middle of an element."""
        webdriver.ActionChains(self._browser).\
            move_to_element(element).perform()

    def _one_click(self, element) -> None:
        """One a click on the element."""
        webdriver.ActionChains(self._browser).click(element).perform()

    def _double_click(self, element) -> None:
        """Double the click on the element."""
        webdriver.ActionChains(
            self._browser).double_click(element).perform()

    def _right_click(self, element) -> None:
        """Right a click on the element."""
        webdriver.ActionChains(self._browser).context_click(element).perform()

    def _select_all_text(self, element) -> None:
        """Doing double clicks for select all text."""
        webdriver.ActionChains(
            self._browser).double_click(element).click().perform()
