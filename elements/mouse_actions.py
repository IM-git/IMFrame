from selenium import webdriver


class MouseActions:
    """
    Here the common mouse actions.
    """

    def __init__(self, browser):
        self.__browser = browser

    def move_to_element(self, element) -> None:
        """Moving the mouse to the middle of an element."""
        webdriver.ActionChains(self.__browser).\
            move_to_element(element).perform()

    def one_click(self, element) -> None:
        """One a click on the element."""
        webdriver.ActionChains(self.__browser).click(element).perform()

    def double_click(self, element) -> None:
        """Double the click on the element."""
        webdriver.ActionChains(
            self.__browser).double_click(element).perform()

    def right_click(self, element) -> None:
        """Right a click on the element."""
        webdriver.ActionChains(self.__browser).context_click(element).perform()

    def select_all_text(self, element) -> None:
        """Doing double clicks for select all text."""
        webdriver.ActionChains(
            self.__browser).double_click(element).click().perform()
